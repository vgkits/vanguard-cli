import click

from vgkits.vanguard import detectDeviceConfig, calculateFlashLookup

brains = [
    "vanguard",
    "vanguard+rainbow",
    "python",
    "javascript",
    "basic",
    "lua",
    "forth",
    "micropython",
    "micropython+blinka",
    "circuitpython",
    "espruino",
    "nodemcu",
    "punyforth",
]


@click.command()
@click.argument("target", type=click.Choice(brains + [""]), default="")
@click.option("--release", "-r", help="Upload specific release of TARGET firmware")
@click.option("--port", "-p", help="The serial UART port to use")
@click.option("--baud", "-b", help="The serial UART speed to use")
@click.option("--erase", "-e", type=bool, help="Activate/deactivate erasing")
@click.option("--flash", "-f", type=bool, help="Activate/deactivate flashing")
@click.option("--device", "-d", help="Treat as known device (suppress auto-detection)")
@click.option("--input", "-i", type=click.Path(exists=True), help="Path to a firmware image file")
def main(*a, **k):
    """Replaces firmware with latest firmware named TARGET"""
    k = dict((name,value) for name, value in k.items() if value is not None and value is not "")
    run(*a, **k)


def calculateImageFile(target, release):
    targetAliases = {
        None: "vanguard",
        "vanguard": "vanguard+rainbow",
        "python": "micropython",
        "javascript": "espruino",
        "basic": "esp8266basic",
        "forth": "punyforth",
        "lua": "nodemcu",
    }
    if target in targetAliases:
        target = targetAliases[target]
        return calculateImageFile(target, release)
    else:
        import os, re
        from collections import namedtuple
        from vgkits.vanguard import calculateDataDir

        FirmwareData = namedtuple("ImageData", "path base name release")

        firmwareDir = calculateDataDir("firmware")
        firmwarePattern = re.compile("(" + re.escape(target) + ")-?v?([0-9].*)\.bin")
        firmwares = list()
        for root, dirnames, filenames in os.walk(firmwareDir):
            for filename in filenames:
                filePath = os.path.join(root, filename)
                fileMatch = firmwarePattern.search(filePath)
                if fileMatch:
                    firmwares.append(FirmwareData(path=filePath, base=fileMatch[0], name=fileMatch[1], release=fileMatch[2]))

        if len(firmwares) > 0:
            if release is not None: # accept only matching release
                for firmware in firmwares:
                    if firmware.release == release:
                        return firmware.path
                else:
                    return None
            else: # choose latest by semver order
                order = sorted(firmwares, key=lambda image:[int(part) for part in image.release.split(".")], reverse=True)
                return order[0].path

        raise FileNotFoundError("No image matching {} available".format(target))


#TODO erase=False default is a workaround until https://github.com/espressif/esptool/pull/314 is merged into pip
def run(target=None, release=None, port=None, baud=1500000, erase=True, flash=True, device=None, input=None):

    if target is not None and input is not None:
        raise click.BadOptionUsage("Cannot use --input {} as well as target {}".format(input, target))
    elif target is None and input is None:
        target = "vanguard"

    from vgkits import esptool
    from vgkits.vanguard import ensurePort, emulateInvocation

    port = ensurePort(port)

    # erase board
    if erase:
        eraseLookup = dict(port=port,baud=baud)
        eraseCommand = "esptool.py --port ${port} erase_flash"
        emulateInvocation(eraseCommand, eraseLookup)
        esptool.main()

    # flash board
    if flash:
        if device is None:
            deviceConfig = detectDeviceConfig(port)

            flashLookup = calculateFlashLookup(deviceConfig=deviceConfig)
        else:
            flashLookup = calculateFlashLookup(deviceName=device)

        path = calculateImageFile(target, release) if target is not None else input

        if flashLookup is not None:
            # locate target firmware
            flashLookup.update(
                port=port,
                baud=baud,
                path=path
            )

            flashCommand = "esptool.py --port ${port} --baud ${baud} write_flash --flash_mode ${flash_mode} --flash_size ${flash_size} 0 ${path}"
            emulateInvocation(flashCommand, flashLookup)
            esptool.main()
        else:
            click.echo("Device doesn't match known flashing configuration", err=True)