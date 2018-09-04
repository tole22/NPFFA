# NVDA Keyboard Event Capture for Mozilla Firefox
#This file is covered by the GNU General Public License.
#See the file COPYING.txt for more details.
#Copyright (C) 2018 Fernando Durgam <fdurgam@gmail.com>
#Preferencias/Opciones de Cursor de Revision seguir foco del sistema=false
#Preferencia /modo navegagacion/todo focos =false
import urllib
import finder
import datetime
from threading import Timer
from interactionEvent.navigationByKeyH import NavigationByKeyH
from accessibilityEvent.accessibilityEvent import AccessibilityEventNVDA
from datetime import date
class Finder(finder.Finder):
    def __init__(self, name):
        super(Finder,self).__init__(name)
        self.minimunSteps=3
        self.maximunScrollingTime=2000
        self.dwellingTime=2.0
        self.scrollingStarTingTime=1500
        self.steps=0
        #self.logger=logger
        self.scrollingInitialited=False
        
        
    
    def flush(self):
        #Timer(3.0, ui.message("con retardo"))
        if self.steps>self.minimunSteps:
            params=urllib.urlencode({"threat":"FlashScroll","timeStamp":"times","url":"event.url","self.steps":self.steps})
            #ui.message("Enviando")
            self.logger.logEven('NavigationByKeyH',params,False)
            #ui.message("enviando")
        #self.scrollingInitialited=False
        #self.steps=0;
        
    def go(self):
        if not self.scrollingInitialited:
            self.scrollingInitialited=True
            self.scrollingStarTingTime=datetime.datetime.now()
            self.startingTop="inicial"
        else:
            self.steps=self.steps+1
            self.timer=Timer(self.dwellingTime,self.flush())
        
        
    def approbes(self, listEvent):
        try:
            self.go()
            if not len(listEvent)>self.minimunSteps:
                return None
            times=[]
            for event in reversed(listEvent):
                times.append(event.timeStamp)
            params=urllib.urlencode({"threat":"FlashScroll","timeStamp":times,"url":event.url})
            #ui.message("Enviando")
            eventoAccesibilidad=AccessibilityEventNVDA("ContentOverlooked",listEvent,params)
            return eventoAccesibilidad
            #logger.logEven('NavigationByKeyH',params,False)
            #ui.message("enviando")
        except:
            x=1
           # ui.message("Error al  Procesar finder NavigationByKeyH")
            
    def funciona(self):
        ui.message("funciona")

if __name__== '__main__':
    x=Finder("flah scroll")
    evet=NavigationByKeyH("nombre","www.google.com","foco","navegado")
    print(evet.url)
    print(evet.foco)
    eventsNavListtest=[]
    eventsNavListtest.append(NavigationByKeyH("nombre","www.google.com","",""))
    eventsNavListtest.append(NavigationByKeyH("nombre","www.google.com","",""))
    eventsNavListtest.append(NavigationByKeyH("nombre","www.google.com","",""))
    eventsNavListtest.append(NavigationByKeyH("nombre","www.google.com","",""))
    print x.approbes(eventsNavListtest)
    if x.approbes(eventsNavListtest):
        print("Evento")
        print x.approbes(eventsNavListtest).getReportLogger()
    else:
        print("no evento")