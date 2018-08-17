# NVDA Keyboard Event Capture for Mozilla Firefox
#This file is covered by the GNU General Public License.
#See the file COPYING.txt for more details.
#Copyright (C) 2018 Fernando Durgam <fdurgam@gmail.com>
#Preferencias/Opciones de Cursor de Revision seguir foco del sistema=false
#Preferencia /modo navegagacion/todo focos =false
import urllib
import ui
import api
import speech
import finder
from interactionEvent.eventoAccesibility import *
class Finder(finder.Finder):
    def __init__(self, name):
        super(Finder,self).__init__(name)
    
    def approbes(self, listEvent, logger):
        try:
            eventsNavList=[]
            for event in reversed(listEvent):
                 if isinstance(event,NavigationByKeyL):
                    ui.message("Cantidad de Hijos")
                    #speech.speakObject(event.navegado)
                    #ui.message(str(len(event.navegado.children)))
                    eventsNavList.append(event)
                    #ui.message("Objeto Foco")
                    (leftf,topf,widthf,heightf)=event.foco.location
                    #ui.message("Objeto navegado")
                    (left,top,width,height)=event.navegado.location
                    #ui.message("Absolutas")
                    params=urllib.urlencode({"threat":"NavigationListMenu","finalTop":"finaltopp" ,"locationNavegador":(left,top,width,height),"timeStamp":event.timeStamp,"navegado":event.navegado,"url":event.url})
                    logger.logEven('NavigationByKeyH',params,False)
            #ui.message("Cantidad de Navegacion de listas NavigationBetweenList")
            #ui.message(str(len(eventsNavList)))
        except:
            x=2
            #ui.message("Error al  Procesar finder de list")

if __name__== '__main__':
	x=Finder("Buscar Navegacion entre listas")