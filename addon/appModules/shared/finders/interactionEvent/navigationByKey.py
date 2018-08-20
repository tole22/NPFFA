# NVDA Keyboard Event Capture for Mozilla Firefox
#This file is covered by the GNU General Public License.
#See the file COPYING.txt for more details.
#Copyright (C) 2018 Fernando Durgam <fdurgam@gmail.com>
#Preferencias/Opciones de Cursor de Revision seguir foco del sistema=false
#Preferencia /modo navegagacion/todo focos =false
from eventoInteraccion import evento
import api
import ui
class NavigationByKey(evento):
    '''
    constructor
    '''
    def __init__(self, name, url):
        '''
        Constructor
        '''
        self.foco=api.getFocusObject()
        self.navegado=api.getNavigatorObject()
        super(NavigationByKey,self).__init__(name,url)
        ui.message("Evento de")
        ui.message(self.name)
    
    
    def __str__(self, *args, **kwargs):
        cadena="name: " + self.name
        return cadena
    
    def _get_objNavegado(self):
        return self.navegado
    
    def _get_objFocus(self):
        return self.foco
    
if __name__== '__main__':
    x= NavigationByKey("evento1","foco","navegado","www.google.com")
    print(x.__str__())