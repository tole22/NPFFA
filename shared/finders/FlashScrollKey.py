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
from threading import Timer
from interactionEvent.navigationByKeyH import NavigationByKeyH
from accessibilityEvent.accessibilityEvent import AccessibilityEventNVDA
from datetime import date
class Finder(finder.Finder):
    def __init__(self, name,logger):
        super(Finder,self).__init__(name)
        self.logger=logger
        self.minimunSteps=2
        self.maximunScrollingTime=12
        self.dwellingTime=10.0
        self.scrollingStartingTime=1500
        #self.timer
        self.threatName="FlashScrollingAccessibilityNVDA"
        self.startingTop=0
        self.scrollingInitialited=False
        self.steps=0
        
    def flush(self, listEvent):
        if listEvent[0].navegado:
            (left,top,width,height)=listEvent[0].navegado.location
        else:
            top=0
        self.startingTop=top
        self.steps=len(listEvent)
        #time.sleep(12)
        #print("Evento ejecutado")
        if listEvent[-1].navegado:
            (left,top,width,height)=listEvent[self.steps].navegado.location
        else:
            top=100
        currentTop=top
        scrolledLenth=abs(self.startingTop-currentTop)
        #scrollingEndingTime=datetime.datetime.now()-self.dwellingTime
        scrollingEndingTime=listEvent[-1].timeStamp
        scrollingTime=listEvent[-1].timeStamp-listEvent[0].timeStamp
        if self.steps>self.minimunSteps:
            #params=urllib.urlencode({"threatName":self.threatName,"time":scrollingTime,"initialTop":self.startingTop,"finalTop":currentTop})
            params={"threatName":self.threatName,"time":scrollingTime,"initialTop":self.startingTop,"finalTop":currentTop}
            eventoAccesibilidad=AccessibilityEventNVDA(self.threatName,[],params)
            self.logger.logEven(eventoAccesibilidad.name, eventoAccesibilidad.getReportLogger(), False)
            self.listEvent=[]
            return eventoAccesibilidad
        return None
        #if self.steps>self.minimunSteps:
        #    params=urllib.urlencode({"threat":"FlashScroll","timeStamp":"times","url":"event.url","self.steps":self.steps})
            #ui.message("Enviando")
        #    self.logger.logEven('NavigationByKeyH',params,False)
            #ui.message("enviando")
        #self.scrollingInitialited=False
        #self.steps=0;
    
             
    def approbes(self, event):
        try:
            deltaTime=datetime.timedelta(0,3,20300)
            if len(self.listEvent)>0:
                #print(event.timeStamp-self.listEvent[-1].timeStamp)
                if (event.timeStamp-self.listEvent[-1].timeStamp)>deltaTime:
                    return self.flush(self.listEvent)
            self.listEvent.append(event)
            #print (len(self.listEvent))
            #print ("Tiempo: ")
            #print (datetime.datetime.now())
            #if not self.scrollingInitialited:     
            #    self.startingTop=self.listEvent[0]
            #    self.steps=len(self.listEvent)
            #self.timer.cancel()
  
            #self.timer=Timer(self.dwellingTime, self.flush,())
            #self.timer.start()

        except:
            x=1
           # ui.message("Error al  Procesar finder NavigationByKeyH")

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
    