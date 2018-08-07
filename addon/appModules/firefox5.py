# NVDA Keyboard Event Capture for Mozilla Firefox
#This file is covered by the GNU General Public License.
#See the file COPYING.txt for more details.
#Copyright (C) 2018 Fernando Durgam <fdurgam@gmail.com>
#Preferencias/Opciones de Cursor de Revision seguir foco del sistema=false
#Preferencia /modo navegagacion/todo focos =false
#

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
import textInfos
import browseMode
from conexiones import eventoAccesibility
from conexiones import logger
from conexiones import finders
import configPlugin
import sys
from conexiones import parser

addonHandler.initTranslation()

class AppModule(firefox.AppModule):
	
	finders=[]
	event=[]
	def event_NVDAObject_init(self,obj):
		sys.path.append('C:\\Python27\\Lib')
		if obj.role == controlTypes.ROLE_WINDOW:
			self.finders=[]
			self.finders.append(finders.finder_NavigationBetweenHeader("Buscador de Header"))
			self.finders.append(finders.finder_NavigationBetweenList("Buscador de listas"))
	
	def ignorar_gesto(self, gesto):
 		api.getFocusObject().treeInterceptor.script_collapseOrExpandControl(gesto)
 		
	def finderEvent(self,finderEvent,listEvent):
		for finder in finderEvent:
			finder.approbes(listEvent,self.logger)
	
	def event_gainFocus(self, obj, nextHandler):
		try:
			ui.message("Nombre de producto")
			#ui.message(self.productName)
			#ui.message(self.appModuleName)
			#speech.cancelSpeech()
			if obj.role==controlTypes.ROLE_DOCUMENT:
				ui.message("obj.role")
				ui.message(str(obj.__class__.__name__))
			if obj.role==controlTypes.ROLE_APPLICATION:
				ui.message("rol aplicacion")
			pagina=parser.parser('http://192.168.1.110/accesibilidad2/modonavegacion.php')
			#ui.message(self.pagina.getPagina())
			#self.server=configPlugin.getServer()
			#self.token= configPlugin.getToken()
			self.server=pagina.getServer()
			self.token=pagina.getToken()
			self.logger=logger.logger(self.server, self.token, False)
		except:
			ui.message("Error")						
		nextHandler()

 	def modoNavegacion(self):
 		focus = api.getFocusObject()
		vbuf=focus.treeInterceptor
		if vbuf.passThrough:
			return False
		return True
	
	def newEvent(self,event):
		'''compara antes de agregar el evetno lo compara con el ultimo recibido
		si son iguales no se produjo navegacion
		caso contrario lo agrega a la lista
		'''
		try:
			equivalent=False
			if self.event:
				ultimo=self.event[-1].navegado
				ui.message("comparando ultimo evento")
				#if ultimo.__ne__(self,objNavegado):
				if ultimo==event.navegado:
					ui.message("iguales")
					equivalent=True
				else:
					ui.message("no iguales")
			if not equivalent:
				self.event.append(event)
		except:
			ui.message("Error al cargar evento")	
	
	def script_nav_prox_header(self, gesture):
		try:
			if self.modoNavegacion():
				ui.message("Presionaste h")
				obj=api.getNavigatorObject().treeInterceptor
				ui.message("evento")
				browseMode.BrowseModeTreeInterceptor.script_nextHeading(obj,gesture)
				ui.message("Objeto Foco")
				objFoco=api.getFocusObject()
				ui.message("Objeto Navegado")
				objNavegado=api.getNavigatorObject()
				speech.speakObject(objNavegado)
				evento=eventoAccesibility.NavigationByKeyH("NavigationByKeyH", objFoco, objNavegado, self.event)
				self.newEvent(evento)
			else:
				self.ignorar_gesto(gesture)
		except:
			ui.message("Error")	
			
	def script_nav_prox_headerH1(self, gesture):
		try:
			if self.modoNavegacion():
				obj=api.getNavigatorObject().treeInterceptor
				browseMode.BrowseModeTreeInterceptor.script_nextHeading(obj,gesture)
				ui.message("Presionaste h")
				ui.message("Objeto Foco")
				objFoco=api.getFocusObject()
				speech.speakObject(objFoco)
				ui.message("Objeto Navegado")
				objNavegado=api.getNavigatorObject()
				speech.speakObject(objNavegado)
				evento=eventoAccesibility.NavigationByKeyH("NavigationByKeyH", objFoco, objNavegado)
				if evento.approves:
					ui.message("evento")
					ui.message(evento.evento(self.logger))
			else:
				self.ignorar_gesto(gesture)
		except:
			ui.message("Error")	
	
	def script_nav_prox_list(self, gesture):
		try:
			if self.modoNavegacion():
				obj=api.getNavigatorObject().treeInterceptor
				browseMode.BrowseModeTreeInterceptor.script_nextList(obj,gesture)
				ui.message("Presionaste L")
				ui.message("Objeto Foco")
				objFoco=api.getFocusObject()
				ui.message("Objeto Navegado")
				objNavegado=api.getNavigatorObject()
				evento=eventoAccesibility.NavigationByKeyL("NavigationByKeyL", objFoco, objNavegado, self.event)
				self.newEvent(evento)
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

 	def script_config(self, gesture):
 			try:
 				token=configPlugin.getToken()
 				server=configPlugin.getServer()
 				ui.message("presinaste t")
 				directorio=configPlugin.directorio()
 				ui.message(str(directorio))
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
			ui.message("Cantida de eventos")
			ui.message(str(len(self.event)))
			ui.message("Cantindad de Buscadores")
			ui.message(str(len(self.finders)))
			self.finderEvent(self.finders, self.event)
		except:
			ui.message("Error")
	
	__gestures = {
		"kb:h": "nav_prox_header",
		"kb:shift+h": "nav_previous_header",
		"kb:NVDA+F8": "status",
		"kb(desktop):NVDA+A": "status",
		"kb(laptop):NVDA+Control+A": "status",
		"kb:NVDA+Control+N": "status",
		"kb:t": "config",
		"kb:1": "nav_prox_headerH1",
		"kb:l": "nav_prox_list",
		"kb:o": "status"
	}

