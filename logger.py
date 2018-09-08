import httplib, urllib
import shared.finders
import time
import datetime
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

class logger(object):
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
        parameters={"token":self.clientToken, "threat":threatName,"timestamp":datetime.datetime.now()}
        params["token"]=self.clientToken
        params["threat"]=threatName
        params["timestamp"]=datetime.datetime.now()
        #params=params.update(parameters)
        params=urllib.urlencode(params)
        headers= {"Content-type":"application/x-www-form-urlencoded","Accept":"text/plain"}
        conn=httplib.HTTPConnection(self.server)
        request=conn.request("POST","/Threats",params,headers)
        response=conn.getresponse()
        
    def __str__(self, *args, **kwargs):
        cadena="Token:" + self.clientToken + ", host: " +self.host + ", refactoringsHost: "+self.refactoringsHost
        return cadena