## Party Moder

![PartyMode](https://raw.githubusercontent.com/aerth/plugin.audio.partymoder/master/resources/icon.png)

It can be tough finding the "Party Mode" music feature in Kodi.

This addon makes it easy to launch music party mode smart playlist.

Here is `.kodi/userdata/autoexec.py` to start party mode on boot (after loading library)

```
import xbmc

# autostart partymoder
xbmc.executebuiltin('XBMC.RunScript(plugin.audio.partymoder)')

```
