'''
Created on 18 jun. 2018

@author: fernando
'''
from copy_reg import constructor

class eventoAccesibility(object):
    '''
    classdocs
    '''
    
    def __init__(self, name):
        '''
        Constructor
        '''
        self.name=name

class navigationByKey(eventoAccesibility):
    '''
    constructor
    '''
    def __init__(self, name, logger):
        '''
        Constructor
        '''
        name="navigationByKey"
        self.logger=logger
        super(navigationByKey,self).__init__(name)
        
    def __str__(self, *args, **kwargs):
        cadena="name" + self.name
        return cadena
    
    def event_caret(self,obj):
        '''
        este es el evnto que deberia llamar al loger
        type parametros: valores que describen el evetno
        
        '''
        self.logger.logEven(self.name, "parameters","asynchronic")
        