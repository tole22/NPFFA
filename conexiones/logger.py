'''
Created on 18 jun. 2018

@author: fernando
'''
#import requests
import httplib, urllib
import datetime
#import NavigationByKey
#import xpathInstance
#import urllib.request
#import urllib2
import ui
import time



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
        ui.message("prcesando longger")
        #ui.message("URL")
        ui.message(params["url"])
        parameters={"token":self.clientToken, "threat":threatName}
        params["token"]=self.clientToken
        params["threat"]=threatName
        params["timestamp"]=int(time.time()*1000)
        #params["timestamp"]=datetime.datetime.now()
        #params=params.update(parameters)
        ui.message("por buscar xpath")
        #if params["xpath"]:
        #    ui.message("xpath encontrado")
        #    element="algo"
        #    (left,top,width,height)=element.location
        #    params["elementLeft"]=left
        #    params["elementTop"]=top
        #    params["elementWidth"]=width
        #    params["elementHeigh"]=height
        #    params["elementContent"]="self.sanitizeContent(element)"
        #    params["parentsList"]="self.builParentsList(element)"
        ui.message("por enviar en este momento")
        params=urllib.urlencode(params)
        headers= {"Content-type":"application/x-www-form-urlencoded","Accept":"text/plain"}
        conn=httplib.HTTPConnection(self.server)
        request=conn.request("POST","/Threats",params,headers)
        response=conn.getresponse()
        
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