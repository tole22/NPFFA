'''
Created on 18 jun. 2018

@author: fernando
'''
import datetime

class eventoInteraccion(object):
    
    def __init__(self, name,url):
        '''
        Constructor
        '''
        self.name=name
        self.url=url
        self.timeStamp= datetime.datetime.now()    

class NavigationByKey(eventoInteraccion):
    '''
    constructor
    '''
    def __init__(self, name, foco, navegado, url):
        '''
        Constructor
        '''
        self.foco=foco
        self.navegado=navegado
        super(NavigationByKey,self).__init__(name,url)
        
    def __str__(self, *args, **kwargs):
        cadena="name: " + self.name
        return cadena
    
    def event_caret(self,obj):
        '''
        este es el evnto que deberia llamar al loger
        type parametros: valores que describen el evetno
        
        '''
        self.logger.logEven(self.name, "parameters","asynchronic")
    
    def _get_objNavegado(self):
        return self.navegado
    
    def _get_objFocus(self):
        return self.navegado
    
    def getLogger(self):
        return self.logger
        
class NavigationByKeyH(NavigationByKey):
    def __init__(self, name, foco, navegado, listEvent,url):
        '''
        Constructor
        '''
        super(NavigationByKeyH,self).__init__(name, foco, navegado, url)
        
    def __str__(self, *args, **kwargs):
        cadena="name: " + self.name
        return cadena
    
class NavigationByKeyL(NavigationByKey):
    def __init__(self, name, foco, navegado, listEvent, url):
        '''
        Constructor
        '''
        super(NavigationByKeyL,self).__init__(name, foco, navegado,url)
    

if __name__== '__main__':
   # miLogger=logger.logger("",",","","")
    nw=NavigationByKey("NavigatorByKEyH","initialTop","navegado")
    nh=NavigationByKeyH("PressH","foco","navegado","")
    print nw.__str__()
    print nh.__str__()
    print str(nh._get_objNavegado())
        