# NVDA Keyboard Event Capture for Mozilla Firefox
#This file is covered by the GNU General Public License.
#See the file COPYING.txt for more details.
#Copyright (C) 2018 Fernando Durgam <fdurgam@gmail.com>
#Preferencias/Opciones de Cursor de Revision seguir foco del sistema=false
#Preferencia /modo navegagacion/todo focos =false
from navigationByKey import NavigationByKey
import api
import ui
class NavigationByKeyT(NavigationByKey):
    def __init__(self, name, url,foco, navegado,xpathCalc):
        '''
        Constructor
        '''
        super(NavigationByKeyT,self).__init__(name, url, foco, navegado,xpathCalc)
        
    def __str__(self, *args, **kwargs):
        cadena="name: " + self.name
        return cadena

       
if __name__== '__main__':
    x= NavigationByKeyTable("evento h","www.google.com")
    print(x.__str__())