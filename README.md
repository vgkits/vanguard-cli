# VGkits' Vanguard Tools

The vgkits-vanguard package is published via [Pip3](https://vgkits.org/blog/what-is-pip3/) giving users simple short commands for configuring [Vanguard boards](https://vgkits.org/blog/projects/vanguard/) and connecting to a Vanguard board's built-in python shell.

Run this ***pip3*** command from a [terminal](https://vgkits.org/blog/what-is-a-terminal/) to install the tools.

    pip3 install vgkits-vanguard

If you don't yet have pip3, (which is installed as part of Python3) then [follow these instructions](https://vgkits.org/blog/pip3-howto/) to install it on your laptop.

See below for the commands you can run after the tools are installed.

## shell : send python commands over USB

Connect to the python shell prompt on the Vanguard board over USB on Windows, MacOS or Linux, by running...

    vanguard shell

This auto-detects the Vanguard's USB device and your operating system's Terminal configuration. Then it launches [miniterm](http://pyserial.readthedocs.io/en/latest/tools.html#module-serial.tools.miniterm) with the proper parameters to connect your [terminal](https://vgkits.org/blog/what-is-a-terminal/) to the [python
shell](https://vgkits.org/blog/what-is-the-python-shell/).

## brainwash : upgrade your board

After some experiments, you can wipe your Vanguard board to get a clean start by running...

    vanguard brainwash

This is equivalent to `vanguard brainwash vanguard` to install latest Micropython plus VGkits' pre-installed libraries. However, you can use ***brainwash*** to wipe and install a different 'operating system' on your Vanguard board such as a clean [Micropython](https://micropython.org/download#esp8266) build, [CircuitPython](https://github.com/adafruit/circuitpython), [Espruino](http://www.espruino.com/EspruinoESP8266) (to write code in [Javascript](https://en.wikipedia.org/wiki/JavaScript)) or [Punyforth](https://github.com/zeroflag/punyforth) (to write code in the [Forth](https://en.wikipedia.org/wiki/Forth_(programming_language)) language). 

There are even [Basic](https://www.esp8266basic.com/) and [LISP](http://www.ulisp.com/show?21T5) interpreters designed to run on this processor!


`vanguard brainwash python` - installs default *python* firmware (equivalent to `vanguard brainwash micropython`)

`vanguard brainwash javascript` - the default *javascript* firmware (equivalent to `vanguard brainwash espruino`)

`vanguard brainwash lua` - the default *lua* firmware (equivalent to `vanguard brainwash nodemcu`)

`vanguard brainwash basic` - the default *basic* firmware (equivalent to `vanguard brainwash esp8266basic`)

`vanguard brainwash forth` - the default *forth* firmware (equivalent to `vanguard brainwash punyforth`) 

`vanguard brainwash micropython` - [latest micropython](https://micropython.org/download#esp8266) release from the firmwares folder

`vanguard brainwash circuitpython` - [latest circuitpython](https://github.com/adafruit/circuitpython/releases/latest) release from the firmwares folder

`vanguard brainwash espruino` - [latest espruino](https://www.espruino.com/binaries/) release from the firmwares folder

`vanguard brainwash esp8266basic` - latest [ESP8266Basic](https://www.esp8266basic.com/) release from the firmwares folder

`vanguard brainwash nodemcu` - latest [NodeMCU](https://github.com/nodemcu/nodemcu-firmware) (eLua) release from the firmwares folder

`vanguard brainwash punyforth` - [latest punyforth](https://github.com/zeroflag/punyforth/tree/master/arch/esp8266/bin) release from the firmwares folder. ***N.B.*** To connect to Punyforth try `vanguard shell --line --echo --eol CRLF` as per [this issue](https://github.com/zeroflag/punyforth/issues/41)

## brainfreeze : back up the board's current configuration

After investing time in uploading libraries, writing and testing scripts on your board, you can save an 'image' of your operating system including any installed files by running...

```
vanguard brainfreeze
```

This creates a file ***brainfreeze.bin*** in the current folder. We suggest you rename this file to *somethingelse.bin* to help you remember the configuration you saved. Use that file to restore your board to the same configuration at a later time by running...

```
vanguard brainwash --input somethingelse.bin
```

## put : upload main.py or python module

If there is a main.py file in the current working directory, you can upload it using...

```
vanguard put
```

If you wanted to put a module on the board, for example a the [bmp180.py](https://github.com/cefn/micropython-bmp180/blob/master/bmp180.py) file to module to use a BMP180 pressure sensor, place the file in the current working directory, then run...

```
vanguard put bmp180.py
```

You will then be able to successfully `import bmp180` from the Vanguard board, and [run the example](https://github.com/cefn/micropython-bmp180/blob/master/README.md).


## rm : remove main.py or python module

If you no longer want the main.py startup script, then run...

```
vanguard rm main.py
```

...and the Vanguard board will no longer run your script on powerup.

## see : launch a file explorer

Every terminal has a 'current working directory', the folder it is currently using to create or find files. To see the contents of this folder, run...

```
vanguard see
```

...to open a graphical file explorer showing the current directory.

Use the terminal command `cd` (change directory) to change the directory by typing in different paths. For example `cd Desktop` will change the directory to a subfolder called Desktop.


## Troubleshooting

The vgkits-vanguard Pypi package (installed via pip) should install a 'vanguard' command into a local folder, which can be run on Windows, Mac OS or Linux using just **vanguard**.

If for any reason **vanguard** is not available you can run instead...

    python -m vgkits.vanguard

...or to force the use of Python3...

    python3 -m vgkits.vanguard
    
If you encounter this issue, probably your path is not properly set up to include the files installed by pip3. Try following [these instructions](https://vgkits.org/blog/pip3-config-howto/) to fix it.
