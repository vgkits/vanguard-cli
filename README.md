# VGkits' Vanguard Tools

The vgkits-vanguard package is published via Pip, and provides simple short commands for configuring and connecting to the python shell on VGkits' Vanguard boards.

## Connecting Vanguard's Python Prompt with 'shell'

To get to the python shell prompt on the Vanguard over USB on Windows, MacOS or Linux, you can run...

```
vanguard shell
```

This auto-detects the Vanguard's USB device and your operating system's Terminal configuration. Then it launches [miniterm](http://pyserial.readthedocs.io/en/latest/tools.html#module-serial.tools.miniterm) with the proper parameters to connect your [terminal](https://vgkits.org/blog/what-is-a-terminal/) to the [python shell](https://vgkits.org/blog/what-is-the-python-shell/).

## Upgrading Vanguard with 'brainwash'

You may wish to wipe your Vanguard board to get a clean start after your experiments. You may wish to install a newer version of Micropython, or  wipe and install a replacement 'operating system' on your Vanguard board such as CircuitPython, [Espruino](http://www.espruino.com/EspruinoESP8266) (to write code in [Javascript](https://en.wikipedia.org/wiki/JavaScript)) or [Punyforth](https://github.com/zeroflag/punyforth) (to write code in the [Forth](https://en.wikipedia.org/wiki/Forth_(programming_language)) language). This can be achieved by...

`vanguard brainwash` - installs default firmware (equivalent to `vanguard brainwash python`)
`vanguard brainwash python` - installs default _python_ firmware (equivalent to `vanguard brainwash micropython`)
`vanguard brainwash javascript` - the default _javascript_ firmware (equivalent to `vanguard brainwash espruino`)
`vanguard brainwash micropython` - latest micropython firmware release from the firmwares folder
`vanguard brainwash circuitpython` - latest circuitpython firmware release from the firmwares folder
`vanguard brainwash espruino` - latest espruino firmware release found in 'flash/firmwares' folder
`vanguard brainwash punyforth` - latest punyforth firmware release found in 'flash/firmwares' folder


## Bundling files

You can upload bundles of files to your Vanguard board, to provide specific python modules or files.

## The 'vanguard' command

The vgkits-vanguard Pypi package (installed via pip) installs a 'vanguard' command (equivalent to `python3 -m vgkits.vanguard`) .

VGkits' tools to connect to Vanguard Shell, update Vanguard firmware.
