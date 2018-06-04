import click

__app__ = "vanguard"

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

def guessPort():
    import platform
    ostype = platform.system()
    if ostype == 'Linux':
        return "/dev/ttyUSB0"
    elif ostype == 'Darwin':
        return "/dev/cu.wchusbserial630"
    elif ostype == 'Windows':
        return None


def ensurePort(port):
    if port is None:
        port = guessPort()
    validPorts = getValidPorts()
    if port is None or port not in validPorts:
        port = selectPort()
    return port


def closePort(port):
    import serial
    ser = serial.Serial()
    ser.port = port
    ser.close()


def getValidPorts():
    from serial.tools.list_ports import comports
    return [info.device for info in comports()]


def selectPort():
    port = None
    from six.moves import input
    validPorts = getValidPorts()

    defaultPort = guessPort()

    message = "Type the number of the device: "
    if defaultPort is not None:
        if defaultPort not in validPorts:
            print("No device {}. Plugged in? Drivers installed?".format(defaultPort))
            defaultPort = None

    numValidPorts = len(validPorts)

    if numValidPorts > 0:

        if numValidPorts == 1:
            defaultPort = validPorts[0]

        if defaultPort is not None:
            message += "({}) ".format(defaultPort)

        while port is None:
            for index, item in enumerate(validPorts):
                print("{} : {}".format(index, item))

            try:
                choice = input(message)
                if choice == "":
                    if defaultPort is not None:
                        port = defaultPort
                else:
                    port = validPorts[int(choice)]
            except ValueError:
                print("Cannot accept {}".format(choice))
                pass

        return port
    else:
        raise RuntimeError("No valid serial ports available.\nIs your device plugged in? Drivers installed?")

def calculateAppDir(*descendantDirs):
    """Get the path of the preferred user config directory for vanguard"""
    import click
    return click.get_app_dir(__app__)


def calculateDataDir(*descendantDirs):
    """Get the path of the package 'data' directory distributed with vanguard"""
    from os import path
    scriptDir = path.dirname(path.abspath(__file__))
    pathStrings = [scriptDir, "data"]
    pathStrings.extend(descendantDirs)
    return path.join(*pathStrings)


def emulateInvocation(commandPattern, commandLookup):
    import sys
    import string
    try:
        command = string.Template(commandPattern).substitute(commandLookup)
        print("Running '" + command + "'")
        sys.argv = command.split()
    except KeyError as e:
        raise RuntimeError("Invocation '" + commandPattern + "' missing value: " + str(e))


def extractBackreference(pattern, text):
    import re
    return re.search(pattern, text, re.MULTILINE).group(1)

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

from vgkits.vanguard.shell import main as shellMain
from vgkits.vanguard.brainwash import main as brainwashMain
from vgkits.vanguard.braindump import main as braindumpMain
main = click.Group(chain=True)
main.add_command(shellMain, "shell")
main.add_command(brainwashMain, "brainwash")
main.add_command(braindumpMain, "braindump")