# NVDA Keyboard Event Capture for Mozilla Firefox
#This file is covered by the GNU General Public License.
#See the file COPYING.txt for more details.
#Copyright (C) 2018 Fernando Durgam <fdurgam@gmail.com>
#Preferencias/Opciones de Cursor de Revision seguir foco del sistema=false
#Preferencia /modo navegagacion/todo focos =false
import urllib
import finder
import ui
import api
import speech
import controlTypes
from NVDAObjects import NVDAObject
#from NVDAObjects.IAccessible.mozilla import IAccessible
from interactionEvent.navigationByKeyL import NavigationByKeyL
from interactionEvent.navigationByKeyK import NavigationByKeyK
from accessibilityEvent.accessibilityEvent import AccessibilityEventNVDA
class Finder(finder.Finder):
    def __init__(self, name,logger,xpathInstance,url):
        self.minimunSteps=1
        self.threatName="NavigationBetweenListsAndLink"
        self.logger=logger
        self.url=url
        self.xpathInstance=xpathInstance
        super(Finder,self).__init__(name)
        
    def flush(self):
        if len(self.listEvent)>self.minimunSteps:
            list=[]
            ui.message("enviando")
            xpaths="&"
            for lista in self.listEvent:
                xpaths=xpaths + str(lista.getXpath()) + "&"
                list.append(str(lista.getChildCount()))
            params={"threatName":self.threatName,"url":self.url,"xpaths":xpaths,"countElement":list}
            eventoAccesibilidad=AccessibilityEventNVDA(self.threatName,[],params)
            self.logger.logEven(eventoAccesibilidad.name, eventoAccesibilidad.getReportLogger(), False)
            self.listEvent=[]
            return eventoAccesibilidad
        self.reset()
        return None
        

    
    def approbes(self, event):
        try:
            if isinstance(event,NavigationByKeyL) or isinstance(event,NavigationByKeyK):
                self.listEvent.append(event)
            else:
                return self.flush()         
        except:
            ui.message("Error en approbes de NavListAndLink")
            


if __name__== '__main__':
    x=Finder("Buscar Navegacion entre listas")
    eventsNavListtest=[]
    eventsNavListtest.append(NavigationByKeyL("nombre","www.google.com","",""))
    if x.approbes(eventsNavListtest):
        print("Evento")
        print x.approbes(eventsNavListtest).name
        print x.approbes(eventsNavListtest).getReportLogger()
        print("no evento")