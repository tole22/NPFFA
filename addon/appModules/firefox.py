# NVDA Keyboard Event Capture for Mozilla Firefox
#This file is covered by the GNU General Public License.
#See the file COPYING.txt for more details.
#Copyright (C) 2018 Fernando Durgam <fdurgam@gmail.com>

from nvdaBuiltin.appModules import firefox
from NVDAObjects.IAccessible.mozilla import Dialog, IAccessible
import addonHandler
import scriptHandler
import globalCommands
import controlTypes
import api
import ui
import winUser
import speech
import gui
import wx
import tones
from datetime import datetime
from threading import Timer
import shared

addonHandler.initTranslation()

class AppModule(firefox.AppModule):

	tbDialog = None
	notificationHistory = []

	#TRANSLATORS: category for Firefox input gestures
	scriptCategory = _("mozilla Firefox")

	def event_gainFocus(self, obj, nextHandler):
                tones.beep(256, 200)
                ui.message("Fernando Durgam")
		nextHandler()

	def script_status(self, gestur):
		ui.message(_("Gesto capturado"))
		nextHandler()
	#TRANSLATORS: message shown in Input gestures dialog for this script
	script_status.__doc__ = _("Reads the status bar. If pressed twice quickly, copies it to clipboard.")
	
	__gestures = {
		"kb(desktop):NVDA+End": "status",
		"kb(laptop):NVDA+Shift+End": "status",
		"kb:NVDA+F8": "status",
		"kb(desktop):NVDA+A": "status",
		"kb(laptop):NVDA+Control+A": "status",
		"kb:NVDA+Control+N": "status",
		"kb:t": "status",
		"kb:h": "status"
	}
