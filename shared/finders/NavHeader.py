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
    def __init__(self, name,logger,xpathInstance,url):
        self.minimunSteps=3
        self.threatName="NavigationBetweenHeader"
        self.logger=logger
        self.url=url
        super(Finder,self).__init__(name)

    def flush(self):
        if len(self.listEvent)>self.minimunSteps:
            xpaths="&"
            for lista in self.listEvent:
                xpaths=xpaths + str(lista.getXpath()) + "&"
            params={"threatName":self.threatName,"url":self.url,"xpaths":xpaths}
            eventoAccesibilidad=AccessibilityEventNVDA(self.threatName,[],params)
            self.logger.logEven(eventoAccesibilidad.name, eventoAccesibilidad.getReportLogger(), False)
            self.listEvent=[]
            return eventoAccesibilidad
        self.reset()
        return None
    
    def approbes(self, event):
        try:
            if isinstance(event,NavigationByKeyH):
                self.listEvent.append(event)
            else:
                return self.flush()          
        except:
            ui.message("Error en approbes")        

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