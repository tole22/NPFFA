'''
Created on 15 jun. 2018

@author: fernando
'''
from conexion import Logger
import eventosNvdaAccesibility.eventosAccesibilidad
import sys
import Tkinter
#import http.client
#https://www.journaldev.com/19213/python-http-client-request-get-post

def conf_read(self):
    f = open('conf.ini', 'r')
    for linea in f:
        print linea,

if __name__ == '__main__':
    raiz=Tkinter.Tk()
    raiz.mainloop()
print "hola mundo"
conf_read()
eventhead = eventosNvdaAccesibility.eventosAccesibilidad.navigateToHead("Acceso a Header")
print eventhead.returnName()
logger=Logger("token","host","refactoringsHost", "verbose", "loggingEnabled")
print logger
logger.conectar()

#import httplib
#conn = httplib.HTTPConnection("www.google.com")
#conn.request("HEAD", "/index.html")

#res = conn.getresponse()
#print res.status, res.reason
#print res.getheaders()
#connection = http.client.HTTPConnection('www.python.org', 80, timeout=10)
#print(connection)