# NVDA Keyboard Event Capture for Mozilla Firefox
#This file is covered by the GNU General Public License.
#See the file COPYING.txt for more details.
#Copyright (C) 2018 Fernando Durgam <fdurgam@gmail.com>
#Preferencias/Opciones de Cursor de Revision seguir foco del sistema=false
#Preferencia /modo navegagacion/todo focos =false
import urllib
import finder
import datetime
import time
import ui
from threading import Timer
from interactionEvent.navigationByKeyH import NavigationByKeyH
from accessibilityEvent.accessibilityEvent import AccessibilityEventNVDA
from datetime import date
class Finder(finder.Finder):
    def __init__(self, name,logger,xpathInstance,url):
        super(Finder,self).__init__(name)
        self.logger=logger
        self.minimunSteps=2
        #self.maximunScrollingTime=12
        #self.dwellingTime=10.0
        #self.scrollingStartingTime=1500
        self.threatName="FlashScrollingAccessibilityNVDA"
        #self.startingTop=0
        #self.scrollingInitialited=False
        self.steps=0
        self.url=url
        #self.xpathInstance=xpathInstance
        
    def flush(self):
        listEvent=self.listEvent
        self.steps=len(self.listEvent)
        scrollingTime=self.listEvent[-1].timeStamp-self.listEvent[0].timeStamp
        if self.steps>self.minimunSteps:
            xpaths="&"
            for lista in self.listEvent:
                xpaths=xpaths + str(lista.getXpath()) + "&"
            params={"threatName":self.threatName,"url":self.url,"xpaths":xpaths,"time":scrollingTime,"initialTop":self.listEvent[0].getXpath(),"finalTop":self.listEvent[-1].getXpath()}
            eventoAccesibilidad=AccessibilityEventNVDA(self.threatName,[],params)
            self.logger.logEven(eventoAccesibilidad.name, eventoAccesibilidad.getReportLogger(), False)
            self.reset()
            ui.message("flos enviado")
            return eventoAccesibilidad
        self.reset()
        return None
    
             
    def approbes(self, event):
        try:
            deltaTime=datetime.timedelta(0,3,20300)
            if len(self.listEvent)>0:
                if (event.timeStamp-self.listEvent[-1].timeStamp)>deltaTime:
                    return self.flush()
            self.listEvent.append(event)
        except:
            ui.message("Error en approbes FlahScrollkey")  
           
   
if __name__== '__main__':
    #r=Timer(2.0, imprimir,())
    #r.start()
    x=Finder("flah scroll")
    eventsNavListtest=[]
    eventsNavListtest.append(NavigationByKeyH("nombre","www.google.com","",""))
    eventsNavListtest.append(NavigationByKeyH("nombre","www.google.com","",""))
    eventsNavListtest.append(NavigationByKeyH("nombre","www.google.com","",""))
    eventsNavListtest.append(NavigationByKeyH("nombre","www.google.com","",""))
    if x.approbes(eventsNavListtest):
        print("Evento")
        #print x.approbes(eventsNavListtest).getReportLogger()
    else:
        print("no evento")
    