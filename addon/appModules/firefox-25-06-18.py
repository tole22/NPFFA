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
from conexiones import eventoAccesibility
from conexiones import logger
#import requests

addonHandler.initTranslation()

class AppModule(firefox.AppModule):

	def ignorar_gesto(self, gesto):
 		ui.message("reenviar")
 		api.getFocusObject().treeInterceptor.script_collapseOrExpandControl(gesto)
 		
	def event_gainFocus(self, obj, nextHandler):
		try:
			ui.message("Cerando Logger")
			self.token= logger.token()
			self.server=logger.server()
			self.logger=logger.logger(self.server, self.token, False)
			pagina=self.obj.rootNVDAObject.HTMLNocd.document
			nodo=NVDAObjects.IAccessible.MSHTML.locateHTMLElementByID(pagina,'id=token')
			speech.speakObject(nodo)
		except:
			ui.message("Error")						
		nextHandler()

 	def modoNavegacion(self):
 		focus = api.getFocusObject()
		vbuf=focus.treeInterceptor
		if vbuf.passThrough:
			return False
		return True
	
	def script_nav_prox_header(self, gesture):
		try:
			obj=api.getNavigatorObject().treeInterceptor
			if self.modoNavegacion():
				ui.message("Presionaste h")
				evento=eventoAccesibility.NavigationByKey("h")
				self.logger.prueba()
				browseMode.BrowseModeTreeInterceptor.script_nextHeading(obj,gesture)
			else:
				self.ignorar_gesto(gesture)
		except:
			ui.message("Error")	
			
	def script_nav_previous_header(self, gesture):
		try:
			if self.modoNavegacion():
				ui.message("Presionaste shift + h")
				obj=api.getNavigatorObject().treeInterceptor
				browseMode.BrowseModeTreeInterceptor.script_previousHeading(obj,gesture)
			else:	
				self.ignorar_gesto(gesture)
		except:
			ui.message("Error")
 	
 	def script_status(self, gesture):
		try:
			focus = api.getFocusObject()
			vbuf=focus.treeInterceptor
			ui.message("Modo de navegacion")
			if self.modoNavegacion():
				ui.message("Activado")
			else:
				ui.message("Desactivado")
		except:
			ui.message("Error")
	
	__gestures = {
		"kb:h": "nav_prox_header",
		"kb:shift+h": "nav_previous_header",
		"kb:NVDA+F8": "status",
		"kb(desktop):NVDA+A": "status",
		"kb(laptop):NVDA+Control+A": "status",
		"kb:NVDA+Control+N": "status",
		"kb:t": "status",
		"kb:o": "status"
	}
