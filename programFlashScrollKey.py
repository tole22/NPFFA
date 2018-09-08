import httplib, urllib
import shared.finders
import time
import datetime
from shared.finders.accessibilityEvent.accessibilityEvent import AccessibilityEventNVDA
from shared.finders.interactionEvent.eventoInteraccion import evento
from shared.finders.interactionEvent.navigationByKeyH import NavigationByKeyH
from shared.finders.interactionEvent.navigationByKeyL import NavigationByKeyL
import logger
def server():
    server="192.168.1.110:8080"
    return server

def token():
    token="sfs"
    return token

def enviarEvento(finders,newList):
    for finder in finders:
            eventoAccesibilidad=finder.approbes(newList)
            if eventoAccesibilidad:
                print eventoAccesibilidad
                #logger.logEven(eventoAccesibilidad.name, eventoAccesibilidad.getReportLogger(), False)
            else:
                print ("El Buscador")
                print finder.name
                print (" No encontro evento")
                print("")
                
   
if __name__== '__main__':
    import random
    from threading import Timer
    logger=logger.logger(server(),token(),False)
    print(logger)
    finderEvent=shared.finders.getFinders(logger)
    eventsNavListtest=[]
    eventsNavListtest.append(NavigationByKeyH("nombre","www.google.com","",""))
    time.sleep(2)
    eventsNavListtest.append(NavigationByKeyH("nombre","www.google.com","",""))
    time.sleep(2)
    eventsNavListtest.append(NavigationByKeyH("nombre","www.google.com","",""))
    time.sleep(2)
    eventsNavListtest.append(NavigationByKeyH("nombre","www.google.com","",""))
    time.sleep(2)
    eventsNavListtest.append(NavigationByKeyL("nombre","www.google.com","",""))
    time.sleep(2)
    eventsNavListtest.append(NavigationByKeyL("nombre","www.google.com","",""))
    time.sleep(5)
    eventsNavListtest.append(NavigationByKeyL("nombre","www.google.com","",""))
    time.sleep(2)
    eventsNavListtest.append(NavigationByKeyH("nombre","www.google.com","",""))
    time.sleep(2)
    eventsNavListtest.append(NavigationByKeyH("nombre","www.google.com","",""))
    time.sleep(2)
    eventsNavListtest.append(NavigationByKeyH("nombre","www.google.com","",""))
    time.sleep(2)
    eventsNavListtest.append(NavigationByKeyH("nombre","www.google.com","",""))
    time.sleep(2)
    eventsNavListtest.append(NavigationByKeyH("nombre","www.google.com","",""))
    time.sleep(2)
    eventsNavListtest.append(NavigationByKeyH("nombre","www.google.com","",""))
    time.sleep(4)
    #eventsNavListtest.append(NavigationByKeyL("nombre","www.google.com","",""))
    #eventsNavListtest.append(NavigationByKeyL("nombre","www.google.com","",""))
    #eventsNavListtest.append(NavigationByKeyL("nombre","www.google.com","",""))
    #report="url=www.google.com&timeStamp=%5Bdatetime.datetime%282018%2C+9%2C+4%2C+15%2C+19%2C+33%2C+5000%29%2C+datetime.datetime%282018%2C+9%2C+4%2C+15%2C+19%2C+33%2C+5000%29%2C+datetime.datetime%282018%2C+9%2C+4%2C+15%2C+19%2C+33%2C+5000%29%2C+datetime.datetime%282018%2C+9%2C+4%2C+15%2C+19%2C+33%2C+5000%29%2C+datetime.datetime%282018%2C+9%2C+4%2C+15%2C+19%2C+33%2C+5000%29%2C+datetime.datetime%282018%2C+9%2C+4%2C+15%2C+19%2C+33%2C+5000%29%2C+datetime.datetime%282018%2C+9%2C+4%2C+15%2C+19%2C+33%2C+5000%29%2C+datetime.datetime%282018%2C+9%2C+4%2C+15%2C+19%2C+33%2C+5000%29%2C+datetime.datetime%282018%2C+9%2C+4%2C+15%2C+19%2C+33%2C+5000%29%5D&threat=FlashScroll"
    #eventoAccessibility=AccessibilityEventNVDA("nombre","list",report)
    #print eventoAccessibility.name
    newList=[]
    for event in eventsNavListtest:
        print ("Evento")
        newList.append(event)
        #tiempo=random.randrange(1,10,1)
        #print (tiempo)
        #enviarEvento(finderEvent,newList)
        #exe=Timer(1.0,enviarEvento,(finderEvent,newList))
        #exe.start()
        for finder in finderEvent:
            eventoAccesibilidad=finder.approbes(event)
            if eventoAccesibilidad:
                print ("El Buscador")
                print finder.name
                print eventoAccesibilidad
                #logger.logEven(eventoAccesibilidad.name, eventoAccesibilidad.getReportLogger(), False)
                print("")
        
        

 