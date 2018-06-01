import click

from vgkits.vanguard.shell import main as shellMain
from vgkits.vanguard.brainwash import main as brainwashMain
"""
from vgkits.vanguard.bundle import main as bundleMain
from vgkits.vanguard.regime import main as regimeMain
"""

main = click.Group(chain=True)
main.add_command(shellMain, "shell")
main.add_command(brainwashMain, "brainwash")
"""
toolGroup.add_command(bundleMain, "bundle")
toolGroup.add_command(regimeMain, "regime")
"""

if __name__ == "__main__":
    main()

"""
@cli.command()
def help():
    click.launch("https://vgkits.org/blog/vanguard-tools-intro/")
"""
