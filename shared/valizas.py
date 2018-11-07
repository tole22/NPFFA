'''
Created on 18 jun. 2018

@author: fernando
'''
import datetime
class eventoValiza(object):
    
    def __init__(self, name,url):
        '''
        Constructor
        '''
        self.name=name
        self.url=url
        self.timeStamp= datetime.datetime.now()
        