# NVDA Keyboard Event Capture for Mozilla Firefox
#This file is covered by the GNU General Public License.
#See the file COPYING.txt for more details.
#Copyright (C) 2018 Fernando Durgam <fdurgam@gmail.com>
#Preferencias/Opciones de Cursor de Revision seguir foco del sistema=false
#Preferencia /modo navegagacion/todo focos =false
from NavigationByKey import NavigationByKey
class NavigationByKeyH1(NavigationByKey):
    def __init__(self, name, foco, navegado, url):
        '''
        Constructor
        '''
        super(NavigationByKeyH,self).__init__(name, foco, navegado, url)
        
    def __str__(self, *args, **kwargs):
        cadena="name: " + self.name
        return cadena

class otra():
    pass
       
if __name__== '__main__':
    x= NavigationByKeyH("evento h","foco","navegado","www.google.com")
    print(x.__str__())