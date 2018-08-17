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
			obj=api.getNavigatorObject().treeInterceptor
			#ui.message(str(gesture))
			if inputGesture=="h":
				browseMode.BrowseModeTreeInterceptor.script_nextHeading(obj,gesture)
				return NavigationByKeyH("NavigationByKeyH", listEvent, url)
			if inputGesture=="1":
				browseMode.BrowseModeTreeInterceptor.script_nextHeading(obj,gesture)
				return finders.interactionEvent.eventoAccesibility.NavigationByKeyH1("NavigationByKeyH", listEvent, url)
			if inputGesture=="l":
				browseMode.BrowseModeTreeInterceptor.script_nextList(obj,gesture)
				return NavigationByKeyL("NavigationByKeyL", listEvent, url)
		except:
			ui.message("Error al despacher evento")	


if __name__== '__main__':
	x=dispacher()
	x.event("h")
