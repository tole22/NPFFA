# NVDA Keyboard Event Capture for Mozilla Firefox
#This file is covered by the GNU General Public License.
#See the file COPYING.txt for more details.
#Copyright (C) 2018 Fernando Durgam <fdurgam@gmail.com>
#Preferencias/Opciones de Cursor de Revision seguir foco del sistema=false
#Preferencia /modo navegagacion/todo focos =false
import urllib
import finder
from interactionEvent.navigationByKeyL import NavigationByKeyL
from accessibilityEvent.accessibilityEvent import AccessibilityEventNVDA
class Finder(finder.Finder):
    def __init__(self, name):
        super(Finder,self).__init__(name)
    
    def approbes(self, listEvent):
        try:
            eventsNavList=[]
            for event in reversed(listEvent):
                 if isinstance(event,NavigationByKeyL):
                    #ui.message("Cantidad de Hijos")
                    #speech.speakObject(event.navegado)
                    #ui.message(str(len(event.navegado.children)))
                    eventsNavList.append(event)
                    #ui.message("Objeto Foco")
                    #return event.foco.location
                    if event.foco:
                        (leftf,topf,widthf,heightf)=event.foco.location
                    else:
                        (leftf,topf,widthf,heightf)=(0,0,0,0)
                    #ui.message("Objeto navegado")
                    if event.navegado:
                        (left,top,width,height)=event.navegado.location
                    else:
                        (left,top,width,height)=(0,0,0,0)
                    #ui.message("Absolutas")
                    if urllib.urlencode({"threat":"NavigationListMenu","finalTop":"finaltop" ,"locationNavegador":(left,top,width,height),"timeStamp":event.timeStamp,"navegado":event.navegado,"url":event.url}):
                        params=urllib.urlencode({"threat":"NavigationListMenu","finalTop":"finaltop" ,"locationNavegador":(left,top,width,height),"timeStamp":event.timeStamp,"navegado":event.navegado,"url":event.url})
                        eventoAccesibilidad=AccessibilityEventNVDA("ContentOverlooked",eventsNavList,params)
                        return eventoAccesibilidad
                    #logger.logEven('',params,False)
                    return None
            return None
            #ui.message("Cantidad de Navegacion de listas NavigationBetweenList")
            #ui.message(str(len(eventsNavList)))
        except:
            x=2
            #ui.message("Error al  Procesar finder de list")

if __name__== '__main__':
    x=Finder("Buscar Navegacion entre listas")
    eventsNavListtest=[]
    eventsNavListtest.append(NavigationByKeyL("nombre","www.google.com","",""))
    if x.approbes(eventsNavListtest):
        print("Evento")
        print x.approbes(eventsNavListtest).name
        print x.approbes(eventsNavListtest).getReportLogger()
        print("no evento")