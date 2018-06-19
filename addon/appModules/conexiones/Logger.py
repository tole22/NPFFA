'''
Created on 18 jun. 2018

@author: fernando
'''
import requests
from eventoAccesibility import navigationByKey
from xpathInstance import xpathInstance
class Logger(object):
    '''
    classdocs
    '''
    def __init__(self, serverHost, verbose):
        '''
        Constructor
        '''
        self.server=serverHost
        self.clientToken="7d042a5f-1a28-0d00-bfa1-641b04ade8d6"
        self.host=serverHost +"/Threats"
        self.refactoringsHost=serverHost +"/RefactoringsServer/"
        self.verbose=verbose
        self.loggingEnabled=True
        self.loadUsabilityEventsLoggers()
        
    def logEven(self, threatName, parameters, asynchronic):
        parameters={"token":self.clientToken, "threat":threatName, "url":"document.URL","timestamp":"datetime"}
        #xpathInstance.getElementByXpath("parameters.xpath")
        parametros={'threat':threatName, 'clientToken': '7d042a5f-1a28-0d00-bfa1-641b04ade8d6'}
        r=requests.post('http://'+ self.server+':8080/Threats', data=parameters)
        print "Codigo: "
        print r.status_code
        print "Evento:"  + self.__str__()
        
    def __str__(self, *args, **kwargs):
        cadena="ClienteToken:" + self.clientToken + ", host: " +self.host + ", refactoringsHost: "+self.refactoringsHost
        return cadena
    
    def loadUsabilityEventsLoggers(self):
        '''
        cargar evetnos
        '''
        self.navegator=navigationByKey("navigationByKey",self)