import click


__version__ = "0.2.0"
__app__ = "vanguard"


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
    return port


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

from vgkits.vanguard.shell import main as shellMain
from vgkits.vanguard.brainwash import main as brainwashMain
main = click.Group(chain=True)
main.add_command(shellMain, "shell")
main.add_command(brainwashMain, "brainwash")
