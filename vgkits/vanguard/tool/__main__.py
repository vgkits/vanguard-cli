import click

from vgkits.vanguard.shell import main as shellMain
from vgkits.vanguard.brainwash import main as brainwashMain
"""
from vgkits.vanguard.bundle import main as bundleMain
from vgkits.vanguard.regime import main as regimeMain
"""

toolGroup = click.Group()
toolGroup.add_command(shellMain, "shell")
toolGroup.add_command(brainwashMain, "brainwash")
"""
toolGroup.add_command(bundleMain, "bundle")
toolGroup.add_command(regimeMain, "regime")
"""

if __name__ == "__main__":
    toolGroup()

"""
@cli.command()
def help():
    click.launch("https://vgkits.org/blog/vanguard-tools-intro/")
"""
