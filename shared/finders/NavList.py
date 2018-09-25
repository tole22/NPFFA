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
        
    def flush(self):
        ui.message("estoy en flush")
        if len(self.listEvent)>self.minimunSteps:
            #ui.message("mi rol es")
            #ui.message(str(self.listEvent[-1].navegado.parent.role))
            xpath=[]
            for lista in self.listEvent:
                xpath.append(self.xpathInstance.getElementXPath(lista.navegado))
            #xpath=self.xpathInstance.getElementXPath(self.listEvent[-1].navegado)
            #xpath=xpathInstance.whatSibling(self.listEvent[-1].navegado)
            #ui.message(str(xpath))
            list=[]
            #ui.message("Los Evento son")
            #for ele in self.listEvent:
            #    ui.message("evento")
            #    ui.message(str(ele.navegado.role))
            #for key in self.listEvent[-1].navegado.IA2Attributes.keys():
            #    ui.message(key)
            #    ui.message(self.listEvent[-1].navegado.IA2Attributes[key])
            #    list.append(key+":"+self.listEvent[1].navegado.IA2Attributes[key])
            #params={"threatName":self.threatName,"url":self.url,"currentTop":self.listEvent[-1].navegado,"enlace":self.listEvent[-1].navegado.firstChild.next.value,"list":list,"xpaths":xpath}
            xpaths="&"
            for xp in xpath:
                xpaths=xpaths + str(xp) + "&"
            params={"threatName":self.threatName,"url":self.url,"xpaths":xpaths}
            eventoAccesibilidad=AccessibilityEventNVDA(self.threatName,[],params)
            self.logger.logEven(eventoAccesibilidad.name, eventoAccesibilidad.getReportLogger(), False)
            self.listEvent=[]
            ui.message("reporta evento")
            return eventoAccesibilidad
            #if event.foco:
            #    (leftf,topf,widthf,heightf)=event.foco.location
            #else:
            #    (leftf,topf,widthf,heightf)=(0,0,0,0)
            #if event.navegado:
            #    (left,top,width,height)=event.navegado.location
            #else:
            #    (left,top,width,height)=(0,0,0,0)
            #if urllib.urlencode({"threat":"NavigationListMenu","finalTop":"finaltop" ,"locationNavegador":(left,top,width,height),"timeStamp":event.timeStamp,"navegado":event.navegado,"url":event.url}):
            #    params=urllib.urlencode({"threat":"NavigationListMenu","finalTop":"finaltop" ,"locationNavegador":(left,top,width,height),"timeStamp":event.timeStamp,"navegado":event.navegado,"url":event.url})
            #    eventoAccesibilidad=AccessibilityEventNVDA("ContentOverlooked",eventsNavList,params)
            #    return eventoAccesibilidad
            #     #logger.logEven('',params,False)
        return None
    
    def listaEnlace(self,event):
        ui.message("buscando")
        cant=0
        todoEnlace=True
        if event.navegado.firstChild:
            ui.message("iterando")
            obj = event.navegado
            while obj:
                ui.message("rol")
                rol=obj.firstChild.next.role
                url=obj.firstChild.next.value
                element=obj.firstChild.next
                if isinstance(element,NVDAObject) and element.role==controlTypes.ROLE_LINK:
                    ui.message("Es Enlace")
                else:
                    ui.message("no es")
                    todoEnlace=False
                ui.message(str(obj.firstChild.next.role))
                cant=cant+1
                obj=obj.next
        return todoEnlace
        
    
    def calculateXpath(self,element):
        try:
            return self.xpathInstance.getElementXPath(element)
        except:
            ui.message("Error al calcular el xpath")

    
    def approbes(self, event):
        try:
            ui.message("estoy en finder")
            #ui.message("xpaht")
            #ui.message(str(self.calculateXpath(event.navegado)))
            if isinstance(event,NavigationByKeyL):
                #print(event)
                #print(len(self.listEvent))
                ui.message("Buscando enlaces")
                if self.listaEnlace(event):
                    ui.message("es intancia")
                    self.listEvent.append(event)
                    ui.message("instancia agregada")
                    ui.message(len(self.listEvent))
                else:
                    ui.message("no son todos enlaces")
                    return self.flush()
            else:
                ui.message("procesando")
                return self.flush()          
        except:
            x=2

if __name__== '__main__':
    x=Finder("Buscar Navegacion entre listas")
    eventsNavListtest=[]
    eventsNavListtest.append(NavigationByKeyL("nombre","www.google.com","",""))
    if x.approbes(eventsNavListtest):
        print("Evento")
        print x.approbes(eventsNavListtest).name
        print x.approbes(eventsNavListtest).getReportLogger()
        print("no evento")