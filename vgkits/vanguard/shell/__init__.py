import click

# TODO consider centralising option clusters like https://stackoverflow.com/questions/40182157/python-click-shared-options-and-flags-between-commands

@click.command()
@click.option("--port", "-p", default=None)
@click.option("--baud", "-b", default=None)
def main(*a, **k):
    k = dict((name,value) for name, value in k.items() if value is not None)
    run(*a, **k)

def run(port=None, baud=115200):
    import os
    from serial.tools import miniterm
    from vgkits.vanguard import ensurePort, emulateInvocation
    port = ensurePort(port)

    click.clear()
    click.echo(click.style("Launching Miniterm to connect to Vanguard Python Shell", fg="green"))

    minicomLookup = dict(
        port=port,
        baud=baud,
        eol={'\n': 'CR', '\r\n': 'CRLF'}.get(os.linesep),
    )
    minicomCommand = "serial.tools.miniterm --raw --eol ${eol} --encoding ascii ${port} ${baud}"
    emulateInvocation(minicomCommand, minicomLookup)
    miniterm.main()