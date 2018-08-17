# NVDA Keyboard Event Capture for Mozilla Firefox
#This file is covered by the GNU General Public License.
#See the file COPYING.txt for more details.
#Copyright (C) 2018 Fernando Durgam <fdurgam@gmail.com>
#Preferencias/Opciones de Cursor de Revision seguir foco del sistema=false
#Preferencia /modo navegagacion/todo focos =false
#

import ui
import api
import browseMode
import speech
import sys
from finders.interactionEvent.eventoAccesibility import *
#from finders.interactionEvent.navigationByKeyH import NavigationByKeyH1
#from finders.interactionEvent.navigationByKeyH import NavigationByKeyH
#from finders.eventoAccesibility import NavigationByKeyH
#from interactionEvent.eventoInteraccion import evento
#from interactionEvent.navigationByKeyH import otra
#from interactionEvent.navigationBykey import *
def modoNavegacion():
 		try:
 			focus = api.getFocusObject()
 			vbuf=focus.treeInterceptor
 			if vbuf.passThrough:
 				return False
 			return True
 	 	except:
			ui.message("Error modo navegacion")


class dispacher():
	
			
	def event(self,inputGesture, gesture, listEvent, url):
		try: 
			ui.message("el gesto es")
			ui.message(inputGesture)
			#ui.message(str(gesture))
			if inputGesture=="h":
				return self.script_nav_prox_header(gesture,listEvent, url)
			if inputGesture=="1":
				return self.script_nav_prox_header(gesture,listEvent, url)
			if inputGesture=="l":
				return self.script_nav_prox_list(gesture,listEvent, url)
			
		except:
			ui.message("Error al despacher evento")	
			
 		
	def script_nav_prox_header(self, gesture, listEvent,url):
		try:
			ui.message("El evento es del tipo buscado")
			#x=NavigationByKeyH(self,"nombre","foco","obj","www.google.com")
			ui.message("Si import")
			ui.message("Presionaste h")
			obj=api.getNavigatorObject().treeInterceptor
			ui.message("evento")
			browseMode.BrowseModeTreeInterceptor.script_nextHeading(obj,gesture)
			ui.message("Objeto Foco")
			objFoco=api.getFocusObject()
			ui.message("Objeto Navegado")
			objNavegado=api.getNavigatorObject()
			speech.speakObject(objNavegado)
			ui.message("Creando evento")
			x= NavigationByKeyH("NavigationByKeyH", objFoco, objNavegado, listEvent, url)
			ui.message("evento creado")
			return x
		except:
			ui.message("Error al crear el evento")
		#ui.message("cargando evento")
	
	def script_nav_prox_list(self, gesture, listEvent,url):
		try:
			obj=api.getNavigatorObject().treeInterceptor
			browseMode.BrowseModeTreeInterceptor.script_nextList(obj,gesture)
			ui.message("Presionaste L")
			ui.message("Objeto Foco")
			objFoco=api.getFocusObject()
			ui.message("Objeto Navegado")
			objNavegado=api.getNavigatorObject()
			return NavigationByKeyL("NavigationByKeyL", objFoco, objNavegado, listEvent, url)
		except:
			ui.message("Error al crear el evento")
	
	def mensaje(self):
		ui.message("mensaje leido")



if __name__== '__main__':
	x=dispacher()
	x.event("h")
