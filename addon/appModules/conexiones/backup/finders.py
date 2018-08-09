'''
Created on 18 jun. 2018

@author: fernando
'''
import urllib
import ui
import logger
import speech
import api
from eventoAccesibility import *
class finder(object):
    '''
    classdocs
    '''
    def __init__(self,name):
        '''
        Constructor
        '''
        self.name=name
    
    def getElementByXpath(self,path):
        pass 
    
class finder_NavigationBetweenHeader(finder):
    def __init__(self, name):
        super(finder_NavigationBetweenHeader,self).__init__(name)
    
    def approbes(self, listEvent,logger):
        try:
            for event in reversed(listEvent):
                if isinstance(event,NavigationByKeyH):
                    ui.message("Objeto Foco")
                    (leftf,topf,widthf,heightf)=event.foco.location
                    speech.speakObject(event.foco)
                    ui.message("Objeto navegado")
                    (left,top,width,height)=event.navegado.location
                    ui.message("Absolutas")
                    (deskLeft,deskTop,deskWidth,deskHeight)=api.getDesktopObject().location
                    speech.speakObject(event.navegado)
                    #finaltop=float(top-deskTop)
                    params=urllib.urlencode({"threat":"FlashScrolingKeyH","desktop":(deskLeft,deskTop,deskWidth,deskHeight),"foco Location":(leftf,topf,widthf,heightf),"finalTop":"finaltop" ,"locationNavegador":(left,top,width,height),"timeStamp":event.timeStamp,"navegado":event.navegado,"url":event.url})
                    logger.logEven('NavigationByKeyH',params,False)
                    ui.message("enviando")
        except:
            ui.message("Error al  Procesar finder NavigationByKeyH")

    
class finder_NavigationBetweenList(finder):
    def __init__(self, name):
        super(finder_NavigationBetweenList,self).__init__(name)
    
    def approbes(self, listEvent, logger):
        try:
            eventsNavList=[]
            for event in reversed(listEvent):
                 if isinstance(event,NavigationByKeyL):
                    ui.message("Cantidad de Hijos")
                    speech.speakObject(event.navegado)
                    ui.message(str(len(event.navegado.children)))
                    eventsNavList.append(event)
                    ui.message("Objeto Foco")
                    (leftf,topf,widthf,heightf)=event.foco.location
                    ui.message("Objeto navegado")
                    (left,top,width,height)=event.navegado.location
                    ui.message("Absolutas")
                    params=urllib.urlencode({"threat":"NavigationListMenu","finalTop":"finaltopp" ,"locationNavegador":(left,top,width,height),"timeStamp":event.timeStamp,"navegado":event.navegado,"url":event.url})
                    logger.logEven('NavigationByKeyH',params,False)
            ui.message("Cantidad de Navegacion de listas NavigationBetweenList")
            ui.message(str(len(eventsNavList)))
        except:
            ui.message("Error al  Procesar finder de list")

if __name__== '__main__':
    x=finder_NavigationBetweenHeader("buscador 2")
    print x.approbes("")