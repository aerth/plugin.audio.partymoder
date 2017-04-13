# partymoder xbmc add-on
# Copyright 2017  aerth <aerth@riseup.net>
# Released under the terms of the MIT License

import xbmc

xbmc.executebuiltin('xbmc.PlayerControl(Partymode(music)', True)
xbmc.executebuiltin('xbmc.PlayerControl(repeatall)', True)
xbmc.executebuiltin("Action(Fullscreen)", True)
