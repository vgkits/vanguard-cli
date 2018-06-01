VGkits' Vanguard Tools
======================

The vgkits-vanguard package will be published via Pip, and provides
simple short commands for configuring and connecting to the python shell
on VGkits' Vanguard boards.

Once development of vanguard-tools is complete, assuming you have pip3
(part of Python3), you will be able to run just...

::

    pip3 install vgkits-vanguard

...to install the Vanguard Tools. Then all the commands below will be
available. If you don't yet have Pip3 installed in your laptop, then
`visit these instructions <https://vgkits.org/blog/pip3-howto/>`__

Getting a Python Prompt on Vanguard with 'shell'
------------------------------------------------

After `installing the Vanguard
tools <https://vgkits.org/blog/vanguard-tools-howto/>`__ with pip, you
can connect to the python shell prompt on the Vanguard board over USB on
Windows, MacOS or Linux, by running...

::

    vanguard shell

This auto-detects the Vanguard's USB device and your operating system's
Terminal configuration. Then it launches
`miniterm <http://pyserial.readthedocs.io/en/latest/tools.html#module-serial.tools.miniterm>`__
with the proper parameters to connect your
`terminal <https://vgkits.org/blog/what-is-a-terminal/>`__ to the
`python shell <https://vgkits.org/blog/what-is-the-python-shell/>`__.

Configuring a startup regime with 'regime'
------------------------------------------

You can configure a ***main.py*** file on your Vanguard board, which
will be launched when it powers up.

``vanguard regime vgkits.project.rainbow.paint`` - installs the python
script at **vgkits/project/rainbow/paint.py** as ***main.py***

Uploading file collections to Vanguard with 'bundle'
----------------------------------------------------

You can upload bundles of files to your Vanguard board, to provide
specific python modules or files. For example you can upload the bundle
for the `Vanguard Rainbow
project <https://vgkits.org/blog/projects/rainbow/>`__ by running...

::

    vanguard bundle vgkits-rainbow

This single command is equivalent to performing the following
commands...

``vanguard bundle vgkits-default-modules`` - installs the default vgkits
modules

``vanguard bundle vgkits-replserver`` - configures servers for WebREPL
HTML page + REPL over Websocket

``vanguard regime vgkits.project.rainbow.paint`` - configures servers
for WebREPL HTML page + REPL over Websocket

Upgrading your Vanguard with 'brainwash'
----------------------------------------

After some experiments, you may wish to wipe your Vanguard board to get
a clean start. You can wipe the board and re-install micropython by
running...

::

    vanguard brainwash

You may wish to wipe your Vanguard board to get a clean start after your
experiments. You may wish to install a newer version of Micropython, or
wipe and install a replacement 'operating system' on your Vanguard board
such as CircuitPython,
`Espruino <http://www.espruino.com/EspruinoESP8266>`__ (to write code in
`Javascript <https://en.wikipedia.org/wiki/JavaScript>`__) or
`Punyforth <https://github.com/zeroflag/punyforth>`__ (to write code in
the
`Forth <https://en.wikipedia.org/wiki/Forth_(programming_language)>`__
language). This can be achieved by...

``vanguard brainwash python`` - installs default *python* firmware
(equivalent to ``vanguard brainwash micropython``)

``vanguard brainwash javascript`` - the default *javascript* firmware
(equivalent to ``vanguard brainwash espruino``)

``vanguard brainwash forth`` - the default *forth* firmware (equivalent
to ``vanguard brainwash punyforth``)

``vanguard brainwash lua`` - the default *lua* firmware (equivalent to
``vanguard brainwash nodemcu``)

``vanguard brainwash micropython`` - `latest
micropython <https://micropython.org/download#esp8266>`__ firmware
release from the firmwares folder

``vanguard brainwash circuitpython`` - `latest
circuitpython <https://github.com/adafruit/circuitpython/releases/latest>`__
firmware release from the firmwares folder

``vanguard brainwash espruino`` - `latest
espruino <https://www.espruino.com/binaries/>`__ firmware release found
in 'flash/firmwares' folder

``vanguard brainwash punyforth`` - `latest
punyforth <https://github.com/zeroflag/punyforth/tree/master/arch/esp8266/bin>`__
firmware release found in 'flash/firmwares' folder

``vanguard brainwash nodemcu`` - latest
`NodeMCU <https://github.com/nodemcu/nodemcu-firmware>`__ (eLua)
firmware release found in 'flash/firmwares' folder

Uploading file collections to Vanguard with 'bundle'
----------------------------------------------------

You can upload bundles of files to your Vanguard board, to provide
specific python modules or files. For example you can upload the bundle
for the Vanguard Rainbow project by running...

::

    vanguard bundle vgkits-rainbow

This single command is equivalent to performing the following
commands...

``vanguard bundle vgkits-default-modules`` - installs the default vgkits
modules ``vanguard bundle vgkits.project.rainbow.paint`` - installs the
``vanguard bundle vgkits-replserver`` - configures servers for WebREPL
HTML page + REPL over Websocket

Configuring a startup regime
----------------------------

You can configure a ***main.py*** file on your Vanguard board, which
will be launched when it powers up.

The 'vanguard' command
----------------------

The vgkits-vanguard Pypi package (installed via pip) installs a
'vanguard' command in a local folder. If for any reason running just 'vanguard'
is not available to you you can run the equivalent command like ``python -m vgkits.vanguard.tool``).
