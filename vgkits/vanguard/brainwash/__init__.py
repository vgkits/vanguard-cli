import click

from vgkits.vanguard import emulateInvocation, extractBackreference

brains = [
    "vanguard",
    "python",
    "javascript",
    "lua",
    "forth",
    "micropython",
    "circuitpython",
    "espruino",
    "nodemcu",
    "punyforth",
]

boards = {
    "nodemcu_m": {
        "manufacturer": "51",
        "device": "4014",
        "flash_size": "1MB",
        "flash_mode":"dout",
    },
    "esp01_1M": {
        "manufacturer": "ef",
        "device": "4014",
        "flash_size": "1MB",
        "flash_mode":"dio",
    },
    "nodemcu_v2_amica": {
        "manufacturer": "ef",
        "device": "4016",
        "flash_size": "4MB",
        "flash_mode": "qio", # Pretty sure NodeMCU v2 is qio
    },
}

@click.command()
@click.argument("target", type=click.Choice(brains + [""]), default="")
@click.option("--release", "-r")
@click.option("--port", "-p")
@click.option("--baud", "-b")
@click.option("--erase", "-e")
@click.option("--device", "-d")
def main(*a, **k):
    k = dict((name,value) for name, value in k.items() if value is not None and value is not "")
    run(*a, **k)


def calculateImageFile(target, release):
    if target is None:
        return calculateImageFile("vanguard")
    elif target == "python":
        return calculateImageFile("micropython")
    elif target == "javascript":
        return calculateImageFile("espruino")
    elif target == "lua":
        return calculateImageFile("nodemcu")
    elif target == "forth":
        return calculateImageFile("punyforth")
    else:
        import os, re
        from collections import namedtuple
        from vgkits.vanguard import calculateDataDir

        ImageData = namedtuple("ImageData", "path base name release")

        imageDir = calculateDataDir("firmware")
        imagePattern = re.compile("(" + target + ")-?v?([0-9].*)\.bin")
        images = list()
        for root, dirnames, filenames in os.walk(imageDir):
            for filename in filenames:
                filePath = os.path.join(root, filename)
                fileMatch = imagePattern.search(filePath)
                if fileMatch:
                    images.append(ImageData(path=filePath, base=fileMatch[0], name=fileMatch[1], release=fileMatch[2]))

        if len(images) > 0:
            if release is not None: # accept only matching release
                for image in images:
                    if image.release == release:
                        return image.path
                else:
                    return None
            else: # choose latest by semver order
                order = sorted(images, key=lambda image:image.release.split("."), reverse=True)
                return order[0].path

        raise FileNotFoundError("No image matching {} available".format(target))


def detectDeviceConfig(port):
    import sys
    import io
    import esptool
    oldOut = sys.stdout
    newOut = io.StringIO()
    emulateInvocation("esptool.py --port ${port} flash_id", dict(port=port))
    try:
        sys.stdout = newOut
        esptool.main()
    finally:
        sys.stdout = oldOut

    printed = newOut.getvalue()
    return {
        "chip": extractBackreference("^Chip is (\w+)$", printed),
        "manufacturer": extractBackreference('^Manufacturer: (\w+)$', printed),
        "device": extractBackreference('^Device: (\w+)$', printed),
        "flash_size": extractBackreference('^Detected flash size: (\w+)$', printed),
    }


def calculateFlashLookup(deviceName=None, deviceConfig=None):
    if deviceName:
        return boards[deviceName]
    elif deviceConfig:
        for name,lookup in boards.items():
            if all([lookup[key]==deviceConfig[key] for key in ["manufacturer", "device", "flash_size"]]):
                return lookup
        else:
            return None
    else:
        raise RuntimeError("Requires deviceName or deviceConfig argument to be provided")

def run(target="vanguard", release=None, port=None, baud=1500000, erase=True, device=None):
    import esptool
    from vgkits.vanguard import ensurePort, emulateInvocation

    # populate missing parameters
    port = ensurePort(port)


    # erase board
    if erase:
        eraseLookup = dict(port=port,baud=baud)
        eraseCommand = "esptool.py --port ${port} --baud ${baud} erase_flash"
        emulateInvocation(eraseCommand, eraseLookup)
        esptool.main()


    # flash board
    if device is None:
        deviceConfig = detectDeviceConfig(port)
        flashLookup = calculateFlashLookup(deviceConfig=deviceConfig)
    else:
        flashLookup = calculateFlashLookup(deviceName=device)

    if flashLookup is not None:
        # locate target firmware
        flashLookup.update(
            port=port,
            baud=baud,
            image_path=calculateImageFile(target, release)
        )

        flashCommand = "esptool.py --port ${port} --baud ${baud} write_flash --flash_mode ${flash_mode} --flash_size ${flash_size} 0 ${image_path}"
        emulateInvocation(flashCommand, flashLookup)
        esptool.main()