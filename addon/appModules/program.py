import httplib, urllib
import shared.finders
from shared.finders.accessibilityEvent.accessibilityEvent import AccessibilityEventNVDA
from shared.finders.interactionEvent.eventoInteraccion import evento
from shared.finders.interactionEvent.navigationByKeyH import NavigationByKeyH
from shared.finders.interactionEvent.navigationByKeyL import NavigationByKeyL
def server():
    server="192.168.1.110:8080"
    return server

def token():
    token="sfs"
    return token

class loggerServer(object):
    '''
    classdocs
    '''
    def __init__(self, serverHost, token ,verbose):
        '''
        Constructor
        '''
        self.server=serverHost
        self.clientToken=token
        self.host=str(serverHost) +"/Threats"
        self.refactoringsHost=str(serverHost) +"/RefactoringsServer/"
        self.verbose=verbose
        self.loggingEnabled=True
        #self.loadUsabilityEventsLoggers()
        
    def logEven(self, threatName, params, asynchronic):
        headers= {"Content-type":"application/x-www-form-urlencoded","Accept":"text/plain"}
        conn=httplib.HTTPConnection(self.server)
        request=conn.request("POST","/Threats",params,headers)
        response=conn.getresponse()
        
    def __str__(self, *args, **kwargs):
        cadena="Token:" + self.clientToken + ", host: " +self.host + ", refactoringsHost: "+self.refactoringsHost
        return cadena

if __name__== '__main__':
    logger=loggerServer(server(),token(),False)
    finderEvent=shared.finders.getFinders()
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
    #report="url=www.google.com&timeStamp=%5Bdatetime.datetime%282018%2C+9%2C+4%2C+15%2C+19%2C+33%2C+5000%29%2C+datetime.datetime%282018%2C+9%2C+4%2C+15%2C+19%2C+33%2C+5000%29%2C+datetime.datetime%282018%2C+9%2C+4%2C+15%2C+19%2C+33%2C+5000%29%2C+datetime.datetime%282018%2C+9%2C+4%2C+15%2C+19%2C+33%2C+5000%29%2C+datetime.datetime%282018%2C+9%2C+4%2C+15%2C+19%2C+33%2C+5000%29%2C+datetime.datetime%282018%2C+9%2C+4%2C+15%2C+19%2C+33%2C+5000%29%2C+datetime.datetime%282018%2C+9%2C+4%2C+15%2C+19%2C+33%2C+5000%29%2C+datetime.datetime%282018%2C+9%2C+4%2C+15%2C+19%2C+33%2C+5000%29%2C+datetime.datetime%282018%2C+9%2C+4%2C+15%2C+19%2C+33%2C+5000%29%5D&threat=FlashScroll"
    #eventoAccessibility=AccessibilityEventNVDA("nombre","list",report)
    #print eventoAccessibility.name
    for finder in finderEvent:
       if finder.approbes(eventsNavListtest):
           print ("El Buscador")
           print finder.name
           print (" encontro el evento")
           eventoAccesibilidad=finder.approbes(eventsNavListtest)
           print  eventoAccesibilidad
           logger.logEven(eventoAccesibilidad.name, eventoAccesibilidad.getReportLogger(), False)
       else:
           print ("El Buscador")
           print finder.name
           print (" No encontro evento")
       print("")

 