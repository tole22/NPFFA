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
import treeInterceptorHandler
from treeInterceptorHandler import TreeInterceptor
from conexiones import xpathInstance
from shared.finders.interactionEvent.eventoInteraccion import evento
from shared.finders.interactionEvent.navigationByKeyH import NavigationByKeyH
from shared.finders.interactionEvent.navigationByKeyL import NavigationByKeyL
from shared.finders.interactionEvent.navigationByKeyI import NavigationByKeyI
from shared.finders.interactionEvent.navigationByKeyT import NavigationByKeyT
from shared.finders.interactionEvent.navigationByKeyK import NavigationByKeyK
from shared.finders.interactionEvent.navigationByKeyS import NavigationByKeyS
from shared.finders.interactionEvent.navigationByKeyN import NavigationByKeyN
from shared.finders.interactionEvent.navigationByKeyF import NavigationByKeyF
from shared.finders.interactionEvent.navigationByKeyU import NavigationByKeyU
from shared.finders.interactionEvent.navigationByKeyV import NavigationByKeyV
from shared.finders.interactionEvent.navigationByKeyE import NavigationByKeyE
from shared.finders.interactionEvent.navigationByKeyB import NavigationByKeyB
from shared.finders.interactionEvent.navigationByKeyX import NavigationByKeyX
from shared.finders.interactionEvent.navigationByKeyC import NavigationByKeyC
from shared.finders.interactionEvent.navigationByKeyR import NavigationByKeyR
from shared.finders.interactionEvent.navigationByKeyQ import NavigationByKeyQ

def modoNavegacion():
 		try:
 			focus = api.getFocusObject()
 			vbuf=focus.treeInterceptor
 			if vbuf.passThrough:
 				return False
 			return True
 	 	except:
			ui.message("Error modo navegacion")

class dispatcher():
	def __init__(self):
		pass
	
	def event(self, direction, inputGesture, gesture, listEvent, url):
		try: 
			if api.getNavigatorObject():
				previo=api.getNavigatorObject()
				obj=api.getNavigatorObject().treeInterceptor
				navegadoPrevio=api.getNavigatorObject()
			if api.getFocusObject():
				focoPrevio=api.getFocusObject()
			ui.message("event")
			if inputGesture=="h":
				if direction=="next":
					browseMode.BrowseModeTreeInterceptor.script_nextHeading(obj,gesture)
				if direction=="previous":
					browseMode.BrowseModeTreeInterceptor.script_previousHeading(obj,gesture)
			if inputGesture=="l":
				if direction=="next":
					browseMode.BrowseModeTreeInterceptor.script_nextList(obj,gesture)
				if direction=="previous":
					browseMode.BrowseModeTreeInterceptor.script_previousList(obj,gesture)
			if inputGesture=="i":
				if direction=="next":
					browseMode.BrowseModeTreeInterceptor.script_nextListItem(obj,gesture)
				if direction=="previous":
					browseMode.BrowseModeTreeInterceptor.script_previousListItem(obj,gesture)
			if inputGesture=="t":
				if direction=="next":
					browseMode.BrowseModeTreeInterceptor.script_nextTable(obj,gesture)
				if direction=="previous":
					browseMode.BrowseModeTreeInterceptor.script_previousTable(obj,gesture)
			if inputGesture=="k":
				if direction=="next":
					browseMode.BrowseModeTreeInterceptor.script_nextLink(obj,gesture)
				if direction=="previous":
					browseMode.BrowseModeTreeInterceptor.script_previousLink(obj,gesture)
			if inputGesture=="n":
				if direction=="next":
					browseMode.BrowseModeTreeInterceptor.script_nextNotLinkBlock(obj,gesture)
				if direction=="previous":
					browseMode.BrowseModeTreeInterceptor.script_previousNotLinkBlock(obj,gesture)
			if inputGesture=="f":
				if direction=="next":
					browseMode.BrowseModeTreeInterceptor.script_nextFormField(obj,gesture)
				if direction=="previous":
					browseMode.BrowseModeTreeInterceptor.script_previoustFormField(obj,gesture)
			if inputGesture=="u":
				if direction=="next":
					browseMode.BrowseModeTreeInterceptor.script_nextUnvisitedLink(obj,gesture)
				if direction=="previous":
					browseMode.BrowseModeTreeInterceptor.script_previousUnvisitedLink(obj,gesture)
			if inputGesture=="v":
				if direction=="next":
					browseMode.BrowseModeTreeInterceptor.script_nextVisitedLink(obj,gesture)
				if direction=="previous":
					browseMode.BrowseModeTreeInterceptor.script_previousVisitedLink(obj,gesture)
			if inputGesture=="e":
				if direction=="next":
					browseMode.BrowseModeTreeInterceptor.script_nextEdit(obj,gesture)
				if direction=="previous":
					browseMode.BrowseModeTreeInterceptor.script_previousEdit(obj,gesture)
			if inputGesture=="b":
				if direction=="next":
					browseMode.BrowseModeTreeInterceptor.script_nextButton(obj,gesture)
				if direction=="previous":
					browseMode.BrowseModeTreeInterceptor.script_previousButton(obj,gesture)
			if inputGesture=="x":
				if direction=="next":
					browseMode.BrowseModeTreeInterceptor.script_nextCheckBox(obj,gesture)
				if direction=="previous":
					browseMode.BrowseModeTreeInterceptor.script_previousCheckBox(obj,gesture)
			if inputGesture=="c":
				if direction=="next":
					browseMode.BrowseModeTreeInterceptor.script_nextComboBox(obj,gesture)
				if direction=="previous":
					browseMode.BrowseModeTreeInterceptor.script_previousComboBox(obj,gesture)
			if inputGesture=="r":
				if direction=="next":
					browseMode.BrowseModeTreeInterceptor.script_nextRadioButton(obj,gesture)
				if direction=="previous":
					browseMode.BrowseModeTreeInterceptor.script_previousRadioButton(obj,gesture)
			if inputGesture=="q":
				if direction=="next":
					browseMode.BrowseModeTreeInterceptor.script_nextBlockQuote(obj,gesture)
				if direction=="previous":
					browseMode.BrowseModeTreeInterceptor.script_previousBlockQuote(obj,gesture)
			if inputGesture=="s":
				if direction=="next":
					browseMode.BrowseModeTreeInterceptor.script_nextSeparator(obj,gesture)
				if direction=="previous":
					browseMode.BrowseModeTreeInterceptor.script_previousSeparator(obj,gesture)
			if inputGesture=="m":
				if direction=="next":
					browseMode.BrowseModeTreeInterceptor.script_nextFrame(obj,gesture)
				if direction=="previous":
					browseMode.BrowseModeTreeInterceptor.script_previousFrame(obj,gesture)
			if inputGesture=="g":
				if direction=="next":
					browseMode.BrowseModeTreeInterceptor.script_nextGraphic(obj,gesture)
				if direction=="previous":
					browseMode.BrowseModeTreeInterceptor.script_previousGraphic(obj,gesture)
			if inputGesture=="d":
				if direction=="next":
					browseMode.BrowseModeTreeInterceptor.script_nextLandmark(obj,gesture)
				if direction=="previous":
					browseMode.BrowseModeTreeInterceptor.script_previousLandmark(obj,gesture)
			if inputGesture=="o":
				if direction=="next":
					browseMode.BrowseModeTreeInterceptor.script_nextEmbeddedObject(obj,gesture)
				if direction=="previous":
					browseMode.BrowseModeTreeInterceptor.script_previousEmbeddedObject(obj,gesture)
			if inputGesture=="1":
				if direction=="next":
					browseMode.BrowseModeTreeInterceptor.script_nextHeading1(obj,gesture)
				if direction=="previous":
					browseMode.BrowseModeTreeInterceptor.script_previousHeading1(obj,gesture)
			if inputGesture=="2":
				if direction=="next":
					browseMode.BrowseModeTreeInterceptor.script_nextHeading2(obj,gesture)
				if direction=="previous":
					browseMode.BrowseModeTreeInterceptor.script_previousHeading2(obj,gesture)
			if inputGesture=="3":
				if direction=="next":
					browseMode.BrowseModeTreeInterceptor.script_nextHeading3(obj,gesture)
				if direction=="previous":
					browseMode.BrowseModeTreeInterceptor.script_previousHeading3(obj,gesture)
			if inputGesture=="4":
				if direction=="next":
					browseMode.BrowseModeTreeInterceptor.script_nextHeading4(obj,gesture)
				if direction=="previous":
					browseMode.BrowseModeTreeInterceptor.script_previousHeading4(obj,gesture)
			if inputGesture=="5":
				if direction=="next":
					browseMode.BrowseModeTreeInterceptor.script_nextHeading5(obj,gesture)
				if direction=="previous":
					browseMode.BrowseModeTreeInterceptor.script_previousHeading5(obj,gesture)
			if inputGesture=="6":
				if direction=="next":
					browseMode.BrowseModeTreeInterceptor.script_nextHeading6(obj,gesture)
				if direction=="previous":
					browseMode.BrowseModeTreeInterceptor.script_previousHeading6(obj,gesture)
			if previo==api.getNavigatorObject():
				return None #No se produjo la navegacion
			else:
				eventoI=self.handlerEvent(inputGesture, url)
				eventoI.previo(focoPrevio,navegadoPrevio)
				return eventoI
		except:
			ui.message("Error al despacher evento")
			
	
	def handlerEvent(self, inputKey, url):
		try: 
			obj=api.getNavigatorObject().treeInterceptor
			foco=api.getFocusObject()
			navegado=api.getNavigatorObject()
			xpathCalc=xpathInstance.XpathInstance("")
			if inputKey=="h":
				eventI=NavigationByKeyH("NavigationByKeyH", url, foco, navegado, xpathCalc)
			if inputKey=="l":
				eventI= NavigationByKeyL("NavigationByKeyL", url, foco, navegado,xpathCalc)
			if inputKey=="i":
				eventI= NavigationByKeyI("NavigationByKeyI", url, foco, navegado,xpathCalc)
			if inputKey=="t":
				eventI= NavigationByKeyT("NavigationByKeyt", url, foco, navegado,xpathCalc)
			if inputKey=="k":
				eventI= NavigationByKeyK("NavigationByKeyk", url, foco, navegado,xpathCalc)
			if inputKey=="n":
				eventI= NavigationByKeyN("NavigationByKeyN", url, foco, navegado,xpathCalc)
			if inputKey=="f":
				eventI= NavigationByKeyF("NavigationByKeyF", url, foco, navegado,xpathCalc)
			if inputKey=="u":
				eventI= NavigationByKeyU("NavigationByKeyU", url, foco, navegado,xpathCalc)
			if inputKey=="v":
				eventI= NavigationByKeyV("NavigationByKeyV", url, foco, navegado,xpathCalc)
			if inputKey=="e":
				eventI= NavigationByKeyE("NavigationByKeyE", url, foco, navegado,xpathCalc)
			if inputKey=="b":
				eventI= NavigationByKeyB("NavigationByKeyB", url, foco, navegado,xpathCalc)
			if inputKey=="x":
				eventI= NavigationByKeyX("NavigationByKeyX", url, foco, navegado,xpathCalc)
			if inputKey=="c":
				eventI= NavigationByKeyC("NavigationByKeyC", url, foco, navegado,xpathCalc)
			if inputKey=="r":
				eventI= NavigationByKeyR("NavigationByKeyC", url, foco, navegado,xpathCalc)
			if inputKey=="q":
				eventI= NavigationByKeyQ("NavigationByKeyQ", url, foco, navegado,xpathCalc)
			if inputKey=="s":
				eventI= NavigationByKeyS("NavigationByKeyS", url, foco, navegado,xpathCalc)
			if inputKey=="m":
				return None
			if inputKey=="g":
				return None
			if inputKey=="d":
				return None
			if inputKey=="o":
				return None
			if inputKey=="1":
				eventI=NavigationByKeyH("NavigationByKeyH", url, foco, navegado, xpathCalc)
			if inputKey=="2":
				eventI=NavigationByKeyH("NavigationByKeyH", url, foco, navegado, xpathCalc)
			if inputKey=="3":
				eventI=NavigationByKeyH("NavigationByKeyH", url, foco, navegado, xpathCalc)
			if inputKey=="4":
				eventI=NavigationByKeyH("NavigationByKeyH", url, foco, navegado, xpathCalc)
			if inputKey=="5":
				eventI=NavigationByKeyH("NavigationByKeyH", url, foco, navegado, xpathCalc)
			if inputKey=="6":
				eventI=NavigationByKeyH("NavigationByKeyH", url, foco, navegado, xpathCalc)
			return eventI
		except:
			ui.message("Error al crear el evento de interaccion")
