'''
Created on 18 jun. 2018

@author: fernando
'''
import finders
from finders.interactionEvent.eventoInteraccion import evento
from finders.interactionEvent.navigationByKeyH import NavigationByKeyH
from finders.interactionEvent.navigationByKeyL import NavigationByKeyL
if __name__== '__main__':
   # miLogger=logger.logger("",",","","")
   finderEvent=finders.getFinders()
   eventsNavListtest=[]
   eventsNavListtest.append(NavigationByKeyH("nombre","www.google.com","",""))
   eventsNavListtest.append(NavigationByKeyH("nombre","www.google.com","",""))
   eventsNavListtest.append(NavigationByKeyH("nombre","www.google.com","",""))
   eventsNavListtest.append(NavigationByKeyH("nombre","www.google.com","",""))
   eventsNavListtest.append(NavigationByKeyL("nombre","www.google.com","",""))
   eventsNavListtest.append(NavigationByKeyL("nombre","www.google.com","",""))
   eventsNavListtest.append(NavigationByKeyL("nombre","www.google.com","",""))
   eventsNavListtest.append(NavigationByKeyL("nombre","www.google.com","",""))
   eventsNavListtest.append(NavigationByKeyL("nombre","www.google.com","",""))
   for finder in finderEvent:
       if finder.approbes(eventsNavListtest):
           print ("El Buscador")
           print finder.name
           print (" encontro el evento")
           eventoAccesibilidad=finder.approbes(eventsNavListtest).getReportLogger()
           print  eventoAccesibilidad
       else:
           print ("El Buscador")
           print finder.name
           print (" No encontro evento")
       print("")
            
        
                 
   #print(x.navegado)
        