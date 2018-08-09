# NVDA Keyboard Event Capture for Mozilla Firefox
#This file is covered by the GNU General Public License.
#See the file COPYING.txt for more details.
#Copyright (C) 2018 Fernando Durgam <fdurgam@gmail.com>
#Preferencias/Opciones de Cursor de Revision seguir foco del sistema=false
#Preferencia /modo navegagacion/todo focos =false
from eventoAccesibility import NavigationByKeyH
from eventoAccesibility import NavigationByKeyL
import finder
class Finder(finder.Finder):
    def __init__(self, name):
        super(Finder,self).__init__(name)

    def approbes(self, listEvent, logger):
        try:
            for event in reversed(listEvent):
                print("Procesando evento")
                if isinstance(event,NavigationByKeyH):
                    print("Es instancia")
                    (leftf,topf,widthf,heightf)=event.foco.location
                    #speech.speakObject(event.foco)
                    #ui.message("Objeto navegado")
                    (left,top,width,height)=event.navegado.location
                    #ui.message("Absolutas")
                    (deskLeft,deskTop,deskWidth,deskHeight)=api.getDesktopObject().location
                    #speech.speakObject(event.navegado)
                    #finaltop=float(top-deskTop)
                    params=urllib.urlencode({"threat":"FlashScrolingKeyH","desktop":(deskLeft,deskTop,deskWidth,deskHeight),"foco Location":(leftf,topf,widthf,heightf),"finalTop":"finaltop" ,"locationNavegador":(left,top,width,height),"timeStamp":event.timeStamp,"navegado":event.navegado,"url":event.url})
                    logger.logEven('NavigationByKeyH',params,False)
                    #ui.message("enviando")
                else:
                    print("No instnacia")
        except:
            print("Error")

            
    def funciona(self):
        ui.message("funciona")

if __name__== '__main__':
    x=Finder("Buscador de H")
    eventos=[]
    eventos.append(NavigationByKeyH(x,"nombre","foco","obj","www.google.com"))
    eventos.append(NavigationByKeyL(x,"nombre","foco","obj","www.google.com"))
    x.approbes(eventos, "")
    