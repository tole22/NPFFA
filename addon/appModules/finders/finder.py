# NVDA Keyboard Event Capture for Mozilla Firefox
#This file is covered by the GNU General Public License.
#See the file COPYING.txt for more details.
#Copyright (C) 2018 Fernando Durgam <fdurgam@gmail.com>
#Preferencias/Opciones de Cursor de Revision seguir foco del sistema=false
#Preferencia /modo navegagacion/todo focos =false

class Finder(object):
    '''
    classdocs
    '''
    def __init__(self,name):
        '''
        Constructor
        '''
        self.name=name
    
    def getElementByXpath(self,path):
        pass 

if __name__== '__main__':
	x=Finder("Buscador")