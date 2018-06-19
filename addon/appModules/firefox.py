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
import browseMode

addonHandler.initTranslation()

class AppModule(firefox.AppModule):

	tbDialog = None
	notificationHistory = []
	#sleepMode = True

	#TRANSLATORS: category for Firefox input gestures
	scriptCategory = _("mozilla Firefox")
		
	def event_caret(self, obj, nextHandler):#self:insciad de AppModuel, obj: objeto nvda donde activo evetno, nextHandler: funcion que propaga el even
                try:
                 	#ui.message("evento: Caret move")
                  	#self.activatePosition()
                  	focus = api.getFocusObject()
                  	vbuf=focus.treeInterceptor
                  	#ui.message("Modo de navegacion")
                  	if not vbuf.passThrough:
                  		ui.message("Desplazamiento en navegacion")
                  		#obt=browseMode.currentNVDAObject
                  		#speech.speakObject(obt)
                  	foco=api.getFocusObject()
                   	navegador=api.getNavigatorObject()
                 	if foco!=navegador:
                		ui.message("son distintos")
                		ui.message("evento: Caret move")
                 	if obj.role != controlTypes.ROLE_TABLE:
                  		tones.beep(256, 200)
                  		ui.message("el objeto foco es: ")
                  		speech.speakObject(foco)
                		ui.message("el navedado es: ")
                  		speech.speakObject(navegador)
                  		ui.message("el objeto es")
                  		speech.speakObject(obj)
                  		ui.message("El self es")
                  		speeck.speakObject(self)
                	   	speech.cancelSpeech
                except:
                	pass
                nextHandler()

	def event_liveRegionChange(self, obj, nextHandler):
		ui.message("navigator")
		speech.speakObject(obj)
		ui.sessage("el self es")
		speech.speakObject(self)
		nextHandler()

 	def event_treeInterceptor_gainFocus(self):
 		ui.message("Ganaste foco")
 	
 	def modoNavegacion(self):
 		focus = api.getFocusObject()
		vbuf=focus.treeInterceptor
		if vbuf.passThrough:
			return False
		return True
		
 	def script_status(self, gesture):
		try:
			#Averigua si el modo de navegacion esta activodo
			focus = api.getFocusObject()
			vbuf=focus.treeInterceptor
			ui.message("Modo de navegacion")
			if not vbuf.passThrough:
				ui.message("Activado")
			else:
				ui.message("Desactivado")
				#ver vbuf.getScript("kb:b")
			#browseMode.reportPassThrough
			#ui.message(_("Gesto capturado"))
		except:
			ui.message("Error")
	#TRANSLATORS: message shown in Input gestures dialog for this script
	script_status.__doc__ = _("Reads the status bar. If pressed twice quickly, copies it to clipboard.")
	
	__gestures = {
		"kb(desktop):NVDA+End": "status",
		"kb(laptop):NVDA+Shift+End": "status",
		"kb:NVDA+F8": "status",
		"kb(desktop):NVDA+A": "status",
		"kb(laptop):NVDA+Control+A": "status",
		"kb:NVDA+Control+N": "status",
		"kb:tt": "status",#ir a proximo encabezado
		"kb:l": "status",#ir a proxima lista
		"kb:i": "status",#ir a proximo elemento de lista
		"kb:i": "status",#ir a proxima tabla
		"kb:b": "status",#ir a proxima tabla
		"kb:o": "status"
	}