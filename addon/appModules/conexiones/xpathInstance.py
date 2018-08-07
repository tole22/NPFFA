'''
Created on 18 jun. 2018

@author: fernando
'''

class xpathInstance(object):
    '''
    classdocs
    '''

    def __init__(self, params):
        '''
        Constructor
        '''
    
    def getElementByXpath(self,path):
        pass
    
    def getElementTreeXPath(self,element):
        pass
    
    def getElementXPath(self,element):
        if element:
            if element.IA2Attributes["id"]:
                return '//*[@id="'+element.IA2Attributes["id"]+'"]'
        return self.getElementTreeXPath(element)