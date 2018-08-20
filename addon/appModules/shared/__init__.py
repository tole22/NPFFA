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
	
	def event(self,direction,inputGesture, gesture, listEvent, url):
		try: 
			ui.message("el gesto es")
			ui.message(inputGesture)
			obj=api.getNavigatorObject().treeInterceptor
			#ui.message(str(gesture))
			if inputGesture=="h":
				if direction=="next":
					browseMode.BrowseModeTreeInterceptor.script_nextHeading(obj,gesture)
				if direction=="previous":
					browseMode.BrowseModeTreeInterceptor.script_previousHeading(obj,gesture)
				return NavigationByKeyH("NavigationByKeyH", listEvent, url)
			if inputGesture=="l":
				if direction=="next":
					browseMode.BrowseModeTreeInterceptor.script_nextList(obj,gesture)
				return NavigationByKeyL("NavigationByKeyL", listEvent, url)
			if inputGesture=="i":
				if direction=="next":
					browseMode.BrowseModeTreeInterceptor.script_nextListItem(obj,gesture)
				return None
			if inputGesture=="t":
				if direction=="next":
					browseMode.BrowseModeTreeInterceptor.script_nextTable(obj,gesture)
				return None
			if inputGesture=="k":
				if direction=="next":
					browseMode.BrowseModeTreeInterceptor.script_nextLink(obj,gesture)
				return None
			if inputGesture=="n":
				if direction=="next":
					browseMode.BrowseModeTreeInterceptor.script_nextNotLinkBlock(obj,gesture)
				return None
			if inputGesture=="f":
				if direction=="next":
					browseMode.BrowseModeTreeInterceptor.script_nextFormField(obj,gesture)
				return None
			if inputGesture=="u":
				if direction=="next":
					browseMode.BrowseModeTreeInterceptor.script_nextUnvisitedLink(obj,gesture)
				return None
			if inputGesture=="v":
				if direction=="next":
					browseMode.BrowseModeTreeInterceptor.script_nextVisitedLink(obj,gesture)
				return None
			if inputGesture=="e":
				if direction=="next":
					browseMode.BrowseModeTreeInterceptor.script_nextEdit(obj,gesture)
				return None
			if inputGesture=="b":
				if direction=="next":
					browseMode.BrowseModeTreeInterceptor.script_nextButton(obj,gesture)
				return None
			if inputGesture=="x":
				if direction=="next":
					browseMode.BrowseModeTreeInterceptor.script_nextCheckBox(obj,gesture)
				return None
			if inputGesture=="c":
				if direction=="next":
					browseMode.BrowseModeTreeInterceptor.script_nextComboBox(obj,gesture)
				return None
			if inputGesture=="r":
				if direction=="next":
					browseMode.BrowseModeTreeInterceptor.script_nextRadioButton(obj,gesture)
				return None
			if inputGesture=="q":
				if direction=="next":
					browseMode.BrowseModeTreeInterceptor.script_nextBlockQuote(obj,gesture)
				return None
			if inputGesture=="s":
				if direction=="next":
					browseMode.BrowseModeTreeInterceptor.script_nextSeparator(obj,gesture)
				return None
			if inputGesture=="m":
				if direction=="next":
					browseMode.BrowseModeTreeInterceptor.script_nextFrame(obj,gesture)
				return None
			if inputGesture=="g":
				if direction=="next":
					browseMode.BrowseModeTreeInterceptor.script_nextGraphic(obj,gesture)
				return None
			if inputGesture=="d":
				if direction=="next":
					browseMode.BrowseModeTreeInterceptor.script_nextLandmark(obj,gesture)
				return None
			if inputGesture=="o":
				if direction=="next":
					browseMode.BrowseModeTreeInterceptor.script_nextEmbeddedObject(obj,gesture)
				return None
			if inputGesture=="1":
				if direction=="next":
					browseMode.BrowseModeTreeInterceptor.script_nextHeading1(obj,gesture)
				return None
			if inputGesture=="2":
				if direction=="next":
					browseMode.BrowseModeTreeInterceptor.script_nextHeading2(obj,gesture)
				return None
			if inputGesture=="3":
				if direction=="next":
					browseMode.BrowseModeTreeInterceptor.script_nextHeading3(obj,gesture)
				return None
			if inputGesture=="4":
				if direction=="next":
					browseMode.BrowseModeTreeInterceptor.script_nextHeading4(obj,gesture)
				return None
			if inputGesture=="5":
				if direction=="next":
					browseMode.BrowseModeTreeInterceptor.script_nextHeading5(obj,gesture)
				return None
			if inputGesture=="6":
				if direction=="next":
					browseMode.BrowseModeTreeInterceptor.script_nextHeading6(obj,gesture)
				return None
			ui.message("no existe class evento para este gesto")
			return None
		except:
			ui.message("Error al despacher evento")
			


if __name__== '__main__':
	x=dispacher()
	x.event("h")
