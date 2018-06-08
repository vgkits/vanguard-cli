import click

# TODO consider centralising option clusters like https://stackoverflow.com/questions/40182157/python-click-shared-options-and-flags-between-commands

@click.command()
@click.option("--port", "-p")
@click.option("--baud", "-b")
@click.option("--echo", "echo", flag_value=True, default=None)
@click.option("--no-echo", "echo", flag_value=False, default=None)
@click.option("--raw", "raw", flag_value=True, default=None)
@click.option("--line", "raw", flag_value=False, default=None)
@click.option("--eol")
def main(*a, **k):
    k = dict((name,value) for name, value in k.items() if value is not None)
    run(*a, **k)


def run(port=None, baud=115200, echo=False, raw=True, eol=None):
    import os
    from vgkits import miniterm
    from vgkits.vanguard import ensurePort, emulateInvocation
    port = ensurePort(port)

    click.clear()
    click.echo(click.style("Launching Miniterm to connect to Vanguard Python Shell", fg="green"))

    minicomLookup = dict(
        port=port,
        baud=baud,
        eol={'\n': 'CR', '\r\n': 'CRLF'}.get(os.linesep) if eol is None else eol,
        echo="--echo" if echo else "",
        raw="--raw" if raw else "",
    )
    minicomCommand = "serial.tools.miniterm ${raw} ${echo} --eol ${eol} --encoding ascii ${port} ${baud}"
    emulateInvocation(minicomCommand, minicomLookup)
    miniterm.main()