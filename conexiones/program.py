'''
Created on 18 jun. 2018

@author: fernando
'''
from NVDAObjects.IAccessible.mozilla import Dialog, IAccessible
import ui
import speech
import controlTypes
from NVDAObjects import NVDAObject


class XpathInstance(object):
    '''
    classdocs
    '''
    
    def __init__(self, params):
        '''
        Constructor
        '''
    
    def getElementByXpath(self,path,url):
        ui.message("si ejecuta")
        from lxml import html
        import requests
        url='http://192.168.1.110/accesibilidad2/Modo%20Navegacion%20NVDA/ModoNavegacion.php'
        path='/html/body/h1[4]'
        #page=requests.get(url)
        #tree=html.fromstring(page.content)
        #element=tree.xpath(path)
        #ui.message(element)
            
    
    def getElementTreeXPath(self,element):
        try:
            x=0
            paths=[]
            while element and not element.role==controlTypes.ROLE_DOCUMENT:
                x=x+1
                ui.message("iterando x")
                index=0
                sibling=element.previous
                ui.message("sibling")
                speech.speakObject(sibling)
                ui.message("role del sibling")
                ui.message(str(sibling.role))
                ui.message("el parent es")
                speech.speakObject(element.parent)
                ui.message("rol del parent")
                ui.message(str(element.parent.role))
                ui.message("Conetnedor")
                speech.speakObject(element.container)
                ui.message("texto")
                ui.message(element.basicText)
                ui.message("nombre")
                ui.message(element.name)
                y=0
                while sibling:
                    y=y+1
                    ui.message("iterando y")
                    if sibling.role==controlTypes.ROLE_DOCUMENT:#bueb
                        ui.message("llego al final")
                        continue
                    if sibling.role==element.role:
                        index+=1
                    ui.message("siguiente siblig")   
                    sibling=sibling.previous
                    ui.message("siguiente siblig")
                tagName=element.name
                if index>0:
                    index+=1
                    pathIndex="["+str(index)+"]"
                else:
                    pathIndex=""
                paths.append(tagName+pathIndex)
                element=element.parent
            ui.message("funciona")
            #ui.message(str(paths))
            return("funciona")
        except:
            ui.message("Error en xpath")
            #for(;elemnet)
            return ("aun no tiene xpaht")
    
    def getElementXPath(self,element):
        key="id"
        if key in element.IA2Attributes.keys():
            ui.message("el id es")
            id=str('//*[@id="'+element.IA2Attributes[key])
            id=id+'"]'
            return id
        else:
            return self.getElementTreeXPath(element)
    
if __name__== '__main__':
    x=XpathInstance()