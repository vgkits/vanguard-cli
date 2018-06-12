import click

@click.command()
@click.option("--port", "-p")
@click.option("--baud", "-b")
@click.option("--device", "-d")
@click.option("--output", "-o")
def main(*a, **k):
    k = dict((name,value) for name, value in k.items() if value is not None and value is not "")
    run(*a, **k)

def run(port=None, baud=1500000, device=None, output="brainfreeze.bin"):
    from vgkits import esptool
    from vgkits.vanguard import ensurePort, detectDeviceConfig, calculateFlashLookup, emulateInvocation

    port = ensurePort(port)

    if device is None:
        deviceConfig = detectDeviceConfig(port)

        flashLookup = calculateFlashLookup(deviceConfig=deviceConfig)
    else:
        flashLookup = calculateFlashLookup(deviceName=device)

    flashSize = flashLookup["flash_size"]
    if type(flashSize) is str and flashSize[-2:] == "MB":
        count = int(flashSize[:-2]) * 0x100000
        count = hex(count)

    if flashLookup is not None:
        # locate target firmware
        flashLookup.update(
            port=port,
            baud=baud,
            output=output,
            count=count,
        )

        flashCommand = "esptool.py --port ${port} --baud ${baud} read_flash 0 ${count} ${output}"
        emulateInvocation(flashCommand, flashLookup)
        esptool.main()
