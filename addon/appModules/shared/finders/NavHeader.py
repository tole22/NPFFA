# NVDA Keyboard Event Capture for Mozilla Firefox
#This file is covered by the GNU General Public License.
#See the file COPYING.txt for more details.
#Copyright (C) 2018 Fernando Durgam <fdurgam@gmail.com>
#Preferencias/Opciones de Cursor de Revision seguir foco del sistema=false
#Preferencia /modo navegagacion/todo focos =false
import urllib
#import ui
#import api
#import speech
import finder
#from interactionEvent.eventoAccesibility import *
from interactionEvent.navigationByKeyH import NavigationByKeyH
from accessibilityEvent.accessibilityEvent import AccessibilityEventNVDA
class Finder(finder.Finder):
    def __init__(self, name):
        super(Finder,self).__init__(name)

    def approbes(self, listEvent):
        try:
            for event in reversed(listEvent):
                #ui.message("finde h")
                if isinstance(event,NavigationByKeyH):
                    #ui.message("Objeto Foco")
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
                    #(deskLeft,deskTop,deskWidth,deskHeight)=api.getDesktopObject().location
                    #speech.speakObject(event.navegado)
                    #finaltop=float(top-deskTop)
                    if urllib.urlencode({"threat":"FlashScrolingKeyH","timeStamp":event.timeStamp,"navegado":event.navegado,"url":event.url,"locationNavegador":(left,top,width,height)}):
                        params=urllib.urlencode({"threat":"FlashScrolingKeyH","timeStamp":event.timeStamp,"navegado":event.navegado,"url":event.url,"locationNavegador":(left,top,width,height)})
                        eventoAccesibilidad=AccessibilityEventNVDA("ContentOverlooked",listEvent,params)
                        return eventoAccesibilidad
                    return None

                    #logger.logEven('NavigationByKeyH',params,False)
                    #ui.message("enviando")
            return None
                    #ui.message("No es instnacia de NavigationByKeyH ")
        except:
            pass
            #ui.message("Error al  Procesar finder NavigationByKeyH")
            

if __name__== '__main__':
    x=Finder("Busacdoer")
    eventsNavListtest=[]
    e=NavigationByKeyH("nombre","www.google.com","foco","navegado")
    eventsNavListtest.append(NavigationByKeyH("nombre","www.google.com","",""))
    if x.approbes(eventsNavListtest):
        print("Evento")
        print x.approbes(eventsNavListtest).name
        print x.approbes(eventsNavListtest).getReportLogger()
    else:
        print ("No evento")
    #eventos.append(NavigationByKeyH("nombre","foco","obj","www.google.com"))
    #eventos.append(NavigationByKeyL(x,"nombre","foco","obj","www.google.com"))