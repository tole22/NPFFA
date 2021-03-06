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
import re
import gui
import wx
import os
import tones
import datetime
from threading import Timer
import textInfos
import browseMode
from conexiones import logger
from conexiones import xpathInstance
import shared.finders
import configPlugin
import dispatcher2
import sys
import browseMode
import shared
from shared.valizas import eventoValiza


addonHandler.initTranslation()

class AppModule(firefox.AppModule):
	
	finders=[]
	event=[]
	roles=[]
	thread=None
	def event_NVDAObject_init(self,obj):
		try:
			#ui.message("init")
			#ui.message(str(obj.role))
			#ui.message("role")
			#ui.message(str(xpathInstance.tagHtml(obj.role)))
			self.roles.append(str(obj.role))
			x=1
		except:
			ui.message("Error en init")
	
	def ignorar_gesto(self, gesto):
 		api.getFocusObject().treeInterceptor.script_collapseOrExpandControl(gesto)
 		
	def finderEvent(self,finderEvent,Event):
		try:
			for finder in finderEvent:
				eventoAccesibilidad=finder.approbes(Event)
				if eventoAccesibilidad:
					ui.message(eventoAccesibilidad.name)
		except:
			ui.message("Error finder event")						
		
	def config(self,obj):
		try:
			ui.message("Cargar configuracion")
			dirPython=configPlugin.getDirPython()
			sys.path.append(dirPython)
			self.finders=[]
			self.event=[]
			ui.message("carga")
			#if not self.thread:
			#	self.thread=self.newHilo()
			ui.message("dir python")
			self.script_url('u')
			url="http://"+ str(self.url)
			ui.message("carga")
			from conexiones import parser
			ui.message("carga")
			pagina=parser.parser(url)
			server=pagina.getServer()
			token=pagina.getToken()
			self.server=server
			self.token=token
			self.logger=logger.logger(self.server, self.token, False)
			self.xpathInstance=xpathInstance.XpathInstance("")
			self.finders=shared.finders.getFinders(self.logger,self.xpathInstance,url)
			self.dispacher=dispatcher2.dispatcher()
			ui.message("Bien cargada")
		except:
			ui.message("Error en config")
	
	def procesarCola(self):
		try:
			if len(self.event)>0:
				timeActual=datetime.datetime.now()
				timeEvent=self.event[-1].getTimeStamp()
				eps=timeActual-timeEvent
				if eps>datetime.timedelta(seconds=20):
					for finder in self.finders:
						valiza=eventoValiza("valizaCierre",self.url)
						finder.valiza(valiza)
						self.reset()
			self.thread=self.newHilo()
		except:
			ui.message("error en procesarCola")
	
	def newHilo(self):
		try:
			import threading
			hilo=threading.Timer(40.0, self.procesarCola)
			hilo.setName("Procesador de Colas")
			hilo.start()
			return hilo
		except:
			ui.message("error en new hilo")
		
	def event_gainFocus(self, obj, nextHandler):
		try:
			if obj.role==controlTypes.ROLE_DOCUMENT:
				self.procesarCola()
			if obj.role==controlTypes.ROLE_FRAME:
				self.config(obj)
			nextHandler()
		except:
			ui.message("Error en gain focus")	
	
	def reset(self):
		self.event=[]						
		
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
			equivalent=False
			if self.event:
				ultimo=self.event[-1].navegado
				if ultimo==event.navegado:
					equivalent=True
			if not equivalent:
				self.event.append(event)
				self.finderEvent(self.finders,event)		
		except:
			ui.message("Error al cargar evento")
			
	def script_dispatchEventNext(self, gesture):
		try:	
			ui.message("despachar evento")
			if dispatcher2.modoNavegacion():
				evento=self.dispacher.event("next",gesture.mainKeyName, gesture, self.event, self.url)
				if evento:
					self.newEvent(evento)
			else:
				ui.message("se ignora evento")
				self.ignorar_gesto(gesture)
		except:
			ui.message("Error en evento")		
			
	def script_dispatchEventPrevious(self, gesture):
		try:
			if dispatcher2.modoNavegacion():
				evento=self.dispacher.event("previous",gesture.mainKeyName,gesture, self.event, self.url)
				if evento:
					self.newEvent(evento)
			else:
				self.ignorar_gesto(gesture)
		except:
			ui.message("Error en evento")		
	
 	def script_config(self, gesture):
 			try:
 				token=configPlugin.getToken()
 				server=configPlugin.getServer()
 				directorio=configPlugin.directorio()
		 	except:
					ui.message("Error")
 	
 	def script_procesar(self, gesture):
 		try:
 			self.procesarCola()
 		except:
 			ui.message("Error en procesar")
 		
 	def script_status(self, gesture):
		try:
			params={"threatName":"roles","url":self.url,"xpaths":self.roles}
			self.logger.logEven("roles",params,False)
			ui.message("Cantindad de Buscadores")
			ui.message(str(len(self.finders)))
			focus = api.getFocusObject()
			vbuf=focus.treeInterceptor
			ui.message("Modo de navegacion")
			if self.modoNavegacion():
				ui.message("Activado")
			else:
				ui.message("Desactivado")
			ui.message("Cantida de eventos")
			for f in self.finders:
				ui.message(f.name)
				ui.message(str(len(f.listEvent)))
			ui.message("tatal de eventos")
			ui.message(str(len(self.event)))
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
			securInfo  = _("Insecure connection") if not securInfo   else securInfo
			url=secInfoButton.next.value  
			self.url=url
		
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
		"kb:h": "dispatchEventNext",
		"kb:shift+h": "dispatchEventPrevious",
		"kb:l": "dispatchEventNext",
		"kb:shift+l": "dispatchEventPrevious",
		"kb:i": "dispatchEventNext",
		"kb:shift+i": "dispatchEventPrevious",
		"kb:t": "dispatchEventNext",
		"kb:shift+t": "dispatchEventPrevious",
		"kb:k": "dispatchEventNext",
		"kb:shift+k": "dispatchEventPrevious",
		"kb:n": "dispatchEventNext",
		"kb:shift+k": "dispatchEventPrevious",
		"kb:f": "dispatchEventNext",
		"kb:shift+f": "dispatchEventPrevious",
		"kb:u": "dispatchEventNext",
		"kb:shift+u": "dispatchEventPrevious",
		"kb:v": "dispatchEventNext",
		"kb:shift+v": "dispatchEventPrevious",
		"kb:e": "dispatchEventNext",
		"kb:shift+e": "dispatchEventPrevious",
		"kb:b": "dispatchEventNext",
		"kb:shift+b": "dispatchEventPrevious",
		"kb:x": "dispatchEventNext",
		"kb:shift+x": "dispatchEventPrevious",
		"kb:c": "dispatchEventNext",
		"kb:shift+c": "dispatchEventPrevious",
		"kb:r": "dispatchEventNext",
		"kb:shift+r": "dispatchEventPrevious",
		"kb:q": "dispatchEventNext",
		"kb:shift+q": "dispatchEventPrevious",
		"kb:s": "dispatchEventNext",
		"kb:shift+s": "dispatchEventPrevious",
		"kb:m": "dispatchEventNext",
		"kb:shift+m": "dispatchEventPrevious",
		"kb:g": "dispatchEventNext",
		"kb:shift+g": "dispatchEventPrevious",
		"kb:d": "dispatchEventNext",
		"kb:shift+d": "dispatchEventPrevious",
		"kb:o": "dispatchEventNext",
		"kb:shift+o": "dispatchEventPrevious",
		"kb:1": "dispatchEventNext",
		"kb:shift+1": "dispatchEventPrevious",
		"kb:2": "dispatchEventNext",
		"kb:shift+2": "dispatchEventPrevious",
		"kb:3": "dispatchEventNext",
		"kb:shift+3": "dispatchEventPrevious",
		"kb:4": "dispatchEventNext",
		"kb:shift+4": "dispatchEventPrevious",
		"kb:5": "dispatchEventNext",
		"kb:shift+5": "dispatchEventPrevious",
		"kb:6": "dispatchEventNext",
		"kb:shift+6": "dispatchEventPrevious",
		"kb:p": "status",
		"kb:a": "script_url"
	}
	
