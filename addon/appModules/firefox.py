# NVDA Keyboard Event Capture for Mozilla Firefox
#This file is covered by the GNU General Public License.
#See the file COPYING.txt for more details.
#Copyright (C) 2018 Fernando Durgam <fdurgam@gmail.com>

from nvdaBuiltin.appModules import firefox
from NVDAObjects.IAccessible.mozilla import Dialog, IAccessible
import addonHandler
import scriptHandler
import globalCommands.commands
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
from conexiones.eventoAccesibility import navigationByKey

addonHandler.initTranslation()

class AppModule(firefox.AppModule):

	tbDialog = None
	notificationHistory = []
	#sleepMode = True

	#TRANSLATORS: category for Firefox input gestures
	scriptCategory = _("mozilla Firefox")	
 	
 	def ignorar_gesto(self,gesto):
 		ui.message("reenviar")
		api.getFocusObject().treeInterceptor.script_collapseOrExpandControl(gesto)
 		
 	
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
 	
	def script_nav_prox_table(self,gesture):
		try:
			if self.modoNavegacion():
				ui.message("Presionaste t")
				obj=api.getNavigatorObject().treeInterceptor
				browseMode.BrowseModeTreeInterceptor.script_nextTable(obj,gesture)
			else:
				self.ignorar_gesto(gesture)
		except:
			ui.message("Error")
			
	def script_nav_previous_table(self,gesture):
		try:
			if self.modoNavegacion():
				ui.message("Presionaste shift + t")
				obj=api.getNavigatorObject().treeInterceptor
				browseMode.BrowseModeTreeInterceptor.script_previousTable(obj,gesture)
			else:
				self.ignorar_gesto(gesture)
		except:
			ui.message("Error")
			
	def script_nav_prox_list(self,gesture):
		try:
			if self.modoNavegacion():
				ui.message("Presionaste l")
				obj=api.getNavigatorObject().treeInterceptor
				browseMode.BrowseModeTreeInterceptor.script_nextList(obj,gesture)
			else:
				self.ignorar_gesto(gesture)
		except:
			ui.message("Error")
 	
	def script_nav_previous_list(self,gesture):
		try:
			if self.modoNavegacion():
				#focus = api.getFocusObject()
				ui.message("Presionaste Shift + l")
				obj=api.getNavigatorObject().treeInterceptor
				browseMode.BrowseModeTreeInterceptor.script_previousList(obj,gesture)
			else:
				self.ignorar_gesto(gesture)
		except:
			ui.message("Error")
			
	def script_nav_prox_linc(self,gesture):
		try:
			if self.modoNavegacion():
				#focus = api.getFocusObject()
				ui.message("Presionaste k")
				obj=api.getNavigatorObject().treeInterceptor
				browseMode.BrowseModeTreeInterceptor.script_nextLink(obj,gesture)
			else:
				self.ignorar_gesto(gesture)	
		except:
			ui.message("Error")
			
 	def script_nav_previous_linc(self,gesture):
		try:
			if self.modoNavegacion():
				#focus = api.getFocusObject()
				ui.message("Presionaste Shift + k")
				obj=api.getNavigatorObject().treeInterceptor
				browseMode.BrowseModeTreeInterceptor.script_previousList(obj,gesture)
			else:
				self.ignorar_gesto(gesture)	
		except:
			ui.message("Error")
			
	def script_nav_prox_FromField(self,gesture):
		try:
			if self.modoNavegacion():
				#focus = api.getFocusObject()
				ui.message("Presionaste e")
				obj=api.getNavigatorObject().treeInterceptor
				browseMode.BrowseModeTreeInterceptor.script_nextFormField(obj,gesture)
			else:
				self.ignorar_gesto(gesture)	
		except:
			ui.message("Error")
			
	def script_nav_previous_FromField(self,gesture):
		try:
			if self.modoNavegacion():
				#focus = api.getFocusObject()
				ui.message("Presionaste shift + e")
				obj=api.getNavigatorObject().treeInterceptor
				browseMode.BrowseModeTreeInterceptor.script_previousFormField(obj,gesture)
			else:
				self.ignorar_gesto(gesture)
		except:
			ui.message("Error")

 	def script_nav_prox_Frame(self,gesture):
		try:
			if self.modoNavegacion():
				#focus = api.getFocusObject()
				ui.message("Presionaste m")
				obj=api.getNavigatorObject().treeInterceptor
				browseMode.BrowseModeTreeInterceptor.script_nextFrame(obj,gesture)
			else:
				self.ignorar_gesto(gesture)	
		except:
			ui.message("Error")
 	
 	def script_nav_previous_Frame(self,gesture):
		try:
			if self.modoNavegacion():
				#focus = api.getFocusObject()
				ui.message("Presionaste shift + m")
				obj=api.getNavigatorObject().treeInterceptor
				browseMode.BrowseModeTreeInterceptor.script_previousFrame(obj,gesture)
			else:
				self.ignorar_gesto(gesture)	
		except:
			ui.message("Error")
			
	def script_nav_next_unvisitedLink(self,gesture):
		try:
			if self.modoNavegacion():
				#focus = api.getFocusObject()
				ui.message("Presionaste u")
				commands.script_navigatorObject_nextInFlow(gesture)
			else:
				self.ignorar_gesto(gesture)		
		except:
			ui.message("Error")
 	
 	def script_nav_previous_unvisitedLink(self,gesture):
		try:
			if self.modoNavegacion():
				#focus = api.getFocusObject()
				ui.message("Presionaste shift + u")
				command.script_navigatorObject_previousInFlow(gesture)
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
	#TRANSLATORS: message shown in Input gestures dialog for this script
	script_status.__doc__ = _("Reads the status bar. If pressed twice quickly, copies it to clipboard.")
	
	__gestures = {
		"kb:h": "nav_prox_header",
		"kb:shift+h": "nav_previous_header",
		"kb:t": "nav_prox_table",
		"kb:shift+t": "nav_previous_table",
		"kb:l": "nav_prox_list",
		"kb:shift+l": "nav_previous_list",
		"kb:k": "nav_prox_linc",
		"kb:shift+k": "nav_previous_linc",
		"kb:e": "nav_prox_FromField",
		"kb:shift+e": "nav_previous_FromField",
		"kb:m": "nav_prox_Frame",
		"kb:shift+m": "nav_previous_Frame",
		"kb:u": "nav_next_unvisitedLink",
		"kb:shift+u": "nav_previous_unvisitedLink",
		"kb:o": "status"
	}
