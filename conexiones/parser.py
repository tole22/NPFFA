'''
Created on 18 jun. 2018

@author: fernando
'''
from HTMLParser import HTMLParser
import urllib
from __builtin__ import len
import ui

class parser(HTMLParser):
    '''
    classdocs
    '''
    def __init__(self,url):
        HTMLParser.__init__(self)
        self.document=url

    def handle_starttag(self, tag, attrs):
        try:
            if tag=='meta':
                item=attrs[0]
                if item[0]=='name':
                    if item[1]=="SelfRefactoringToken":
                        token=attrs[1]
                        self.token=token[1]
        except:
            ui.message("Error en startTag")
    
    def getURL(self):
        return self.document
    
    def handle_data(self, data):
        try:
            if "LoggerAccesibility" in data:
                inicio=data.find("LoggerAccesibility")
                sub=data[inicio+len('LoggerAccesibility')+1+len('http://')+1:]
                fin=sub.find(',true')-1
                self.server=sub[:fin]
        except:
            ui.message("Error en handle data")
    
    def getServer(self):
        try:
            f=urllib.urlopen(self.document)
            l=f.read()
            self.feed(l)
            return self.server
        except:
            ui.message("Error en getServer")
    
    def getToken(self):
        try:
            f=urllib.urlopen(self.document)
            l=f.read()
            self.feed(l)
            return self.token
        except:
            ui.message("Error en getToken")
