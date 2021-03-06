# NVDA Keyboard Event Capture for Mozilla Firefox
#This file is covered by the GNU General Public License.
#See the file COPYING.txt for more details.
#Copyright (C) 2018 Fernando Durgam <fdurgam@gmail.com>
#Preferencias/Opciones de Cursor de Revision seguir foco del sistema=false
#Preferencia /modo navegagacion/todo focos =false
from navigationByKey import NavigationByKey
class NavigationByKeyH(NavigationByKey):
        
    def __init__(self, name, url,foco, navegado,xpathCalc):
        '''
        Constructor
        '''
        self.setXpath(xpathCalc.getElementXPath(navegado))
        super(NavigationByKeyH,self).__init__(name, url, foco, navegado,xpathCalc)
        
    def __str__(self, *args, **kwargs):
        cadena="evento: " + self.name
        return cadena
       
if __name__== '__main__':
    x= NavigationByKeyH("evento h","foco","navegado","www.google.com")
    print(x.__str__())