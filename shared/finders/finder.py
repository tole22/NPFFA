# NVDA Keyboard Event Capture for Mozilla Firefox
#This file is covered by the GNU General Public License.
#See the file COPYING.txt for more details.
#Copyright (C) 2018 Fernando Durgam <fdurgam@gmail.com>
#Preferencias/Opciones de Cursor de Revision seguir foco del sistema=false
#Preferencia /modo navegagacion/todo focos =false
import ui
	
class Finder(object):
    '''
    classdocs
    '''
    def __init__(self,name):
        '''
        Constructor
        '''
        self.name=name
        self.listEvent=[]
        
    def valiza(self,valiza):
        try:
            self.flush()
            self.reset()
        except:
            ui.message("error en valiza") 
        
    def __str__(self, *args, **kwargs):
        cadena="name: " + self.name
        return cadena
  
    
    def approbes(self, event):
    	pass
    
    def flush(self):
    	pass
    
    def reset(self):
        self.listEvent=[]

if __name__== '__main__':
	x=getFinders()
	print(x)