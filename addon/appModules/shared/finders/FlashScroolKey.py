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
#from interactionEvent.eventoAccesibility import *
from interactionEvent.navigationByKeyH import NavigationByKeyH
class Finder(finder.Finder):
    def __init__(self, name):
        super(Finder,self).__init__(name)

    def approbes(self, listEvent, logger):
        try:
            try:
                #import sys
                #sys.path.append("C:\Users\fernando\AppData\Roaming\nvda\addons\NVDA-Accessibility\appModules\shared")
                ui.message("Si import")
                #import importlib
                #import os
                #ui.message("importlib importada")
                #dirname, basename = os.path.split(os.path.abspath(os.path.dirname(__file__)))
                #sys.path.append(dirname)
                #from shared.eventoAccesibility import *
                #ui.message(dirname)
                #from eventoAccesibility import *
                #ui.message("el error")
                #y=NavigationByKeyH(sys,"nombre","foco","obj","www.google.com")
                #ui.message(y.url)
            except ImportError:
                ui.message("No import")
            for event in reversed(listEvent):
                ui.message("finde h")
                #x=NavigationByKeyH("nombre","foco","obj","","www.google.com")
                #ui.message("tipo de evento")
                #ui.message(str(type(event)))
                #ui.message("tipo de x")
                #ui.message(str(type(x)))
                if isinstance(event,NavigationByKeyH):
                    ui.message("Objeto Foco")
                    (leftf,topf,widthf,heightf)=event.foco.location
                    speech.speakObject(event.foco)
                    ui.message("Objeto navegado")
                    (left,top,width,height)=event.navegado.location
                    ui.message("Absolutas")
                    (deskLeft,deskTop,deskWidth,deskHeight)=api.getDesktopObject().location
                    #speech.speakObject(event.navegado)
                    #finaltop=float(top-deskTop)
                    params=urllib.urlencode({"threat":"FlashScrolingKeyH","desktop":(deskLeft,deskTop,deskWidth,deskHeight),"foco Location":(leftf,topf,widthf,heightf),"finalTop":"finaltop" ,"locationNavegador":(left,top,width,height),"timeStamp":event.timeStamp,"navegado":event.navegado,"url":event.url})
                    ui.message("Enviando")
                    logger.logEven('NavigationByKeyH',params,False)
                    ui.message("enviando")
                else:
                    ui.message("No es instnacia de NavigationByKeyH ")
        except:
            x=1
            ui.message("Error al  Procesar finder NavigationByKeyH")
            
    def funciona(self):
        ui.message("funciona")

if __name__== '__main__':
    eventos=[]
    eventos.append(NavigationByKeyH(x,"nombre","foco","obj","www.google.com"))
    eventos.append(NavigationByKeyL(x,"nombre","foco","obj","www.google.com"))