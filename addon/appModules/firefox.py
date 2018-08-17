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
import textInfos
import browseMode
#from interactionEvent.eventoAccesibility import *
#from interactionEvent.eventoInteraccion import evento
#from interactionEvent.navigationByKeyH import otra
#from interactionEvent.navigationBykey import *
from conexiones import logger
#from conexiones import finders
import shared.finders
import configPlugin
import sys
import shared
#from shared.finders.interactionEvent.eventoAccesibility import *
from conexiones import parser


addonHandler.initTranslation()

class AppModule(firefox.AppModule):
	
	finders=[]
	event=[]
	def event_NVDAObject_init(self,obj):
		try:
			x=1
			#ui.message("Iniciando configuracion")
			#if obj.role == controlTypes.ROLE_WINDOW:
			#	self.finders=[]
			#	self.finders.append(finders.finder_NavigationBetweenHeader("Buscador de Header"))
			#	self.finders.append(finders.finder_NavigationBetweenList("Buscador de listas"))
		except:
			ui.message("Error en init")
	
	def ignorar_gesto(self, gesto):
 		api.getFocusObject().treeInterceptor.script_collapseOrExpandControl(gesto)
 		
	def finderEvent(self,finderEvent,listEvent):
		try:
			for finder in finderEvent:
				ui.message("procesando finder")
				ui.message(finder.name)
				finder.approbes(listEvent,self.logger)
		except:
			ui.message("Error finder event")						
		
	
	def event_gainFocus(self, obj, nextHandler):
		try:
			ui.message("Cargar configuracion")
			self.dispacher=shared.dispacher()
			if obj.role==controlTypes.ROLE_FRAME:
				ui.message("dir python")
				ui.message(configPlugin.getDirPython())
				dirPython=configPlugin.getDirPython()
				sys.path.append(dirPython)
				self.finders=[]
				self.event=[]
				self.finders=shared.finders.getFinders()
				self.script_url('u')
				ui.message(self.url)
				url="http://"+self.url
				pagina=parser.parser(url)
				ui.message("url")
				ui.message(url)
				ui.message("Direccion server")
				server=pagina.getServer()
				ui.message(server)
				token=pagina.getToken()
				ui.message("token")
				ui.message(token)
				self.server=server
				self.token=token
				ui.message("cargando Logger")
				self.logger=logger.logger(self.server, self.token, False)
			nextHandler()
		except:
			ui.message("Error en gain focus")						
		
 	def modoNavegacion(self):
 		try:
 			focus = api.getFocusObject()
 			vbuf=focus.treeInterceptor
 			if vbuf.passThrough:
 				return False
 			return True
 	 	except:
			ui.message("Error modo navegacion")
 		
 	def newEvent(self,event):
		'''compara antes de agregar el evetno lo compara con el ultimo recibido
		si son iguales no se produjo navegacion
		caso contrario lo agrega a la lista
		'''
		try:
			ui.message("Agreando evento")
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
				#if isinstance(event,NavigationByKeyH):
				#	ui.message("es insancia de NavigationByKeyH ")
				self.event.append(event)
				ui.message("evento agregado")
		except:
			ui.message("Error al cargar evento")
			
	def script_dispatchEvent(self, gesture):
		try:
			if shared.modoNavegacion():
				ui.message(gesture.mainKeyName)
				evento=self.dispacher.event(gesture.mainKeyName,gesture, self.event, self.url)
				ui.message("cargando evento")
				if evento:
					self.newEvent(evento)
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
			ui.message("Error en status")
			
	def script_url(self, gesture):
		if not self.inMainWindow():
			#TRANSLATORS: message spoken by NVDA when the focus is not in the main Firefox window
			ui.message(_("Not available here"))
			return
		path = (("id", "nav-bar"), ("id", "urlbar"), ("id", "identity-box",))
		secInfoButton = self.searchObject(path)
		if secInfoButton:
			securInfo = secInfoButton.description # This has changed in FF 57. Keeping this line for compatibility with earlier versions.
			try: # This one is for FF 57 and later.
				securInfo = secInfoButton.firstChild.next.name if secInfoButton.firstChild.next.IA2Attributes["id"] == "connection-icon" else ""
				if securInfo:
					owner = " ".join([o.name for o in filter(lambda o: o.role == controlTypes.ROLE_STATICTEXT, secInfoButton.recursiveDescendants)])
					securInfo = "%s, %s" % (owner, securInfo) if owner else securInfo
			except:
				pass
			#TRANSLATORS: this connection is using http, not https
			securInfo  = _("Insecure connection") if not securInfo   else securInfo  
			url = secInfoButton.next.value
			#ui.message("direccion")
			self.url=url
			#ui.message(self.url)
			#ui.message("%s (%s)" % (url, securInfo))
		#ui.message (_("Direccion No Disponible"))
		
	def searchObject(self, path):
		obj = api.getForegroundObject()
		for milestone in path:
			obj = self.searchAmongTheChildren(milestone, obj)
			if not obj:
				return
		return obj

	def searchAmongTheChildren(self, id, into):
		if not into:
			return(None)
		key, value = id
		obj = into.firstChild
		if key in obj.IA2Attributes.keys():
			if obj.IA2Attributes[key] == value:
				return(obj)
		while obj:
			if key in obj.IA2Attributes.keys():
				if obj.IA2Attributes[key] == value:
					break
			obj = obj.next
		return(obj)
	
	def inMainWindow(self):
		try:
			if api.getForegroundObject().IA2Attributes["id"]!="main-window":
				return False
		except (AttributeError, KeyError):
				return False
		return True	
	#Los gestos son del tipo keyboardHandler.KeyBoardImputGesture
	__gestures = {
		"kb:h": "dispatchEvent",
		"kb:1": "dispatchEvent",
		"kb:shift+h": "dispatchEvent",
		"kb:t": "dispatchEvent",
		"kb:1": "dispatchEvent",
		"kb:2": "dispatchEvent",
		"kb:5": "dispatchEvent",
		"kb:l": "dispatchEvent",
		"kb:u": "dispatchEvent",
		"kb:o": "status"
	}
	
