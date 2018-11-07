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
        self.minimunSteps=3
        self.minimunChildren=3
        self.threatName="NavigationBetweenLists"
        self.logger=logger
        self.url=url
        super(Finder,self).__init__(name)
        
    def flush(self):
        if (len(self.listEvent)>self.minimunSteps) and (self.countChildren(self.listEvent)):
            list=[]
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
    
    def countChildren(self,lista):
        try:
            allLink=True
            for event in lista:
                #ui.message("cantidad de hijos")
                #ui.message(str(event.navegado.parent.childCount))
                l=0
                for li in event.navegado.parent.children:# element ==li
                    l=l+1
                    #ui.message("roles")
                    #ui.message(str(li.role))
                    if self.isLink(li):
                       # ui.message("elemto")
                        #ui.message(str(l))
                        ui.message("tiene linck ")
                    else:
                        allLink=False
                        ui.message("no tiene linck")
            return allLink     
        except:
            ui.message("Error countChildren")
            
    def isLink(self,li):
        try:
            for item in li.children:
                if item.role==controlTypes.ROLE_LINK:
                    #ui.message("es enlace")
                    return True
                else:
                    #ui.message("No es enlace el rol es")
                    #ui.message(str(item.role))
                    if item.firstChild:
                      #  ui.message("canidad de hijos")
                       # ui.message("recursion")
                        #ui.message(str(item.childCount))
                        return self.isLink(item)
                    
                    
                     
        except:
            ui.message("Error en islink")
                 
        
    def approbes(self, event):
        try:
            if isinstance(event,NavigationByKeyL):
                self.listEvent.append(event)
                #if self.countChildren(self.listEvent):
                #    ui.message("son lintas de enlaces")
                #else:
                #    ui.message("no son todos enlaces")
                
            else:
                return self.flush()          
        except:
            ui.message("Error en approbes")
            


if __name__== '__main__':
    x=Finder("Buscar Navegacion entre listas")
    eventsNavListtest=[]
    eventsNavListtest.append(NavigationByKeyL("nombre","www.google.com","",""))
    if x.approbes(eventsNavListtest):
        print("Evento")
        print x.approbes(eventsNavListtest).name
        print x.approbes(eventsNavListtest).getReportLogger()
        print("no evento")