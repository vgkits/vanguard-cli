This documents future capabilities of the Vanguard tools due to be implemented.

* rsync
* regime
* bundle

Configuring a startup regime with 'regime'
------------------------------------------

You can configure a **main.py** file on your Vanguard board, which will
be launched when it powers up.

`vanguard regime vgkits.project.rainbow.paint` - installs the python
script **vgkits/project/rainbow/paint.py** from the Vanguard board's
internal filesystem as the **main.py** startup regime.

Uploading file collections to Vanguard with 'bundle'
----------------------------------------------------

You can upload bundles of files to your Vanguard board, to provide
specific python modules or files. For example you can upload the bundle
for the [Vanguard Rainbow
project](https://vgkits.org/blog/projects/rainbow/) by running...

    vanguard bundle vgkits-rainbow

This single command is equivalent to performing the following
commands...

`vanguard bundle vgkits-default-modules` - installs the default vgkits
modules

`vanguard bundle vgkits-replserver` - configures servers for WebREPL
HTML page + REPL over Websocket

`vanguard regime vgkits.project.rainbow.paint` - configures servers for
WebREPL HTML page + REPL over Websocket

Uploading file collections to Vanguard with 'bundle'
----------------------------------------------------

You can upload bundles of files to your Vanguard board, to provide
specific python modules or files. For example you can upload the bundle
for the Vanguard Rainbow project by running...

    vanguard bundle vgkits-rainbow

This single command is equivalent to performing the following
commands...

`vanguard bundle vgkits-default-modules` - installs the default vgkits
modules `vanguard bundle vgkits.project.rainbow.paint` - installs the
`vanguard bundle vgkits-replserver` - configures servers for WebREPL
HTML page + REPL over Websocket

Configuring a startup regime
----------------------------

You can configure a **main.py** file on your Vanguard board, which will
be launched when it powers up.
