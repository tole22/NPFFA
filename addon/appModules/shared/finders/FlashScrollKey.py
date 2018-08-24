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
from threading import Timer
#from interactionEvent.eventoAccesibility import *
#from interactionEvent.navigationByKeyH import NavigationByKeyH
from interactionEvent.navigationByKeyH import NavigationByKeyH
class Finder(finder.Finder):
    def __init__(self, name, logger):
        super(Finder,self).__init__(name)
        self.minimunSteps=3
        self.maximunScrollingTime=2000
        self.scrollingStarTingTime=1500
        self.steps=0
        self.logger=logger
        #r=Timer(20.0,self.flush())
    
    def flush(self):
        #Timer(3.0, ui.message("con retardo"))
        params=urllib.urlencode({"threat":"FlashScroll","timeStamp":"times","url":"event.url"})
        ui.message("Enviando")
        self.logger.logEven('NavigationByKeyH',params,False)
        ui.message("enviando")
       

    def approbes(self, listEvent, logger):
        try:
            if not len(listEvent)>self.minimunSteps:
                return None
            times=[]
            for event in reversed(listEvent):
                times.append(event.timeStamp)
            params=urllib.urlencode({"threat":"FlashScroll","timeStamp":times,"url":event.url})
            ui.message("Enviando")
            logger.logEven('NavigationByKeyH',params,False)
            ui.message("enviando")
        except:
            x=1
            ui.message("Error al  Procesar finder NavigationByKeyH")
            
    def funciona(self):
        ui.message("funciona")

if __name__== '__main__':
    eventos=[]
    eventos.append(NavigationByKeyH(x,"nombre","foco","obj","www.google.com"))
    eventos.append(NavigationByKeyL(x,"nombre","foco","obj","www.google.com"))