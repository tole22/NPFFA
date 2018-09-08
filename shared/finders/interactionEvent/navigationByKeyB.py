# NVDA Keyboard Event Capture for Mozilla Firefox
#This file is covered by the GNU General Public License.
#See the file COPYING.txt for more details.
#Copyright (C) 2018 Fernando Durgam <fdurgam@gmail.com>
#Preferencias/Opciones de Cursor de Revision seguir foco del sistema=false
#Preferencia /modo navegagacion/todo focos =false
from navigationByKey import NavigationByKey
class NavigationByKeyB(NavigationByKey):
    def __init__(self, name, url, foco ,navegado):
        '''
        Constructor
        '''
        super(NavigationByKeyB,self).__init__(name, url, foco ,navegado)
        
    def __str__(self, *args, **kwargs):
        cadena="name: " + self.name
        return cadena

class otra():
    pass
       
if __name__== '__main__':
    x= NavigationByKeyB("evento h","foco","navegado","www.google.com")
    print(x.__str__())