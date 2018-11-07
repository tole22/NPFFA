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
from accessibilityEvent.accessibilityEvent import AccessibilityEventNVDA
class Finder(finder.Finder):
    def __init__(self, name,logger,xpathInstance,url):
        self.minimunSteps=1
        self.threatName="NavigationBetweenLists"
        self.logger=logger
        self.url=url
        self.xpathInstance=xpathInstance
        super(Finder,self).__init__(name)
        
    def flush(self,event):
        try:    
            
            #xpaths= self.xpathInstance.getElementXPath(event.navegado)
            xpaths=event.getXpath()
            params={"threatName":self.threatName,"url":self.url,"xpaths":xpaths}
            eventoAccesibilidad=AccessibilityEventNVDA(self.threatName,[],params)
            self.logger.logEven(eventoAccesibilidad.name, eventoAccesibilidad.getReportLogger(), False)
            self.listEvent=[]
            return eventoAccesibilidad
        except:
            ui.message("Error flus")
            
            
     

    def approbes(self, event):
        try:
            self.listEvent.append(event)
            return self.flush(event)          
        except:
            x=2
            
    def reset(self):
        self.listEvent=[]
