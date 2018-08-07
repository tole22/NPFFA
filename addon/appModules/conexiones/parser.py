'''
Created on 18 jun. 2018

@author: fernando
'''
from HTMLParser import HTMLParser
import urllib
from __builtin__ import len

class parser(HTMLParser):
    '''
    classdocs
    '''
    def __init__(self,url):
        HTMLParser.__init__(self)
        self.document=url

    def handle_starttag(self, tag, attrs):
        if tag=='meta':
            item=attrs[0]
            if item[0]=='name':
                if item[1]=="SelfRefactoringToken":
                    token=attrs[1]
                    self.token=token[1]
    
    def handle_data(self, data):
        if "LoggerAccesibility" in data:
            inicio=data.find("LoggerAccesibility")
            sub=data[inicio+len('LoggerAccesibility')+1+len('http://')+1:]
            fin=sub.find(',true')-1
            self.server=sub[:fin]
    
    def getServer(self):
        f=urllib.urlopen(self.document)
        l=f.read()
        self.feed(l)
        return self.server
    
    def getToken(self):
        f=urllib.urlopen(self.document)
        l=f.read()
        self.feed(l)
        return self.token
        
if __name__=='__main__':
    x=parser('http://192.168.1.110/accesibilidad2/modonavegacion.php')
    print "El server es:",x.getServer()
    print "El token es: ",x.getToken()
