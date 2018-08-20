'''
Created on 18 jun. 2018

@author: fernando
'''
#import requests
import httplib, urllib
#import NavigationByKey
#import xpathInstance
#import urllib.request
#import urllib2



def server():
    server=""
    return '192.168.1.110:8080'

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
        #parameters={"token":self.clientToken, "threat":threatName, "url":"document.URL","timestamp":"datetime"}
        #xpathInstance.getElementByXpath("parameters.xpath")
        #parametros={'threat':threatName, 'clientToken': token()}
        #params=urllib.urlencode({'threat':threatName,"otro":'fernando'})
        #params=urllib.urlencode({"span":1})
        headers= {"Content-type":"application/x-www-form-urlencoded","Accept":"text/plain"}
        #conn=httplib.HTTPConnection("192.168.10.111:8080")
        conn=httplib.HTTPConnection(self.server)
        request=conn.request("POST","/Threats",params,headers)
        response=conn.getresponse()
        #print response.status , response.reason
        #print request
        #print response.status
        
    def __str__(self, *args, **kwargs):
        cadena="Token:" + self.clientToken + ", host: " +self.host + ", refactoringsHost: "+self.refactoringsHost
        return cadena
    
    def loadUsabilityEventsLoggers(self):
        '''
        cargar evetnos
        '''
        #self.navegator=navigationByKey("navigationByKey",self)
    
    def prueba(self):
            params=urllib.urlencode({"span":1})
            headers= {"Content-type":"application/x-www-form-urlencoded","Accept":"text/plain"}
            #conn=httplib.HTTPConnection("192.168.10.111:8080")
            conn=httplib.HTTPConnection(self.server)
            request=conn.request("POST","/Threats",params,headers)
            response=conn.getresponse()
            print response.status , response.reason
            print request
    
if __name__== '__main__':
        params=urllib.urlencode({'span':1})
        headers= {"Content-type":"application/x-www-form-urlencoded","Accept":"text/plain"}
        #conn=httplib.HTTPConnection("192.168.10.111:8080")
        conn=httplib.HTTPConnection(server())
        request=conn.request("POST","/Threats",params,headers)
        response=conn.getresponse()
        print response.status , response.reason