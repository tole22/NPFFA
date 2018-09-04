# NVDA Keyboard Event Capture for Mozilla Firefox
#This file is covered by the GNU General Public License.
#See the file COPYING.txt for more details.
#Copyright (C) 2018 Fernando Durgam <fdurgam@gmail.com>
#Preferencias/Opciones de Cursor de Revision seguir foco del sistema=false
#Preferencia /modo navegagacion/todo focos =false

def getFinders():
	finders=[]
	finders.append(Finder(""))
	finders.append(Finder(""))
	return finders
	
class Finder(object):
    '''
    classdocs
    '''
    def __init__(self,name):
        '''
        Constructor
        '''
        self.name=name
        
       
    def __str__(self, *args, **kwargs):
        cadena="name: " + self.name
        return cadena
    
    def getElementByXpath(self,path):
        pass 
    
    def go(self):
    	pass

if __name__== '__main__':
	x=getFinders()
	print(x)