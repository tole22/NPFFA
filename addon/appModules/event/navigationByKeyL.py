# NVDA Keyboard Event Capture for Mozilla Firefox
#This file is covered by the GNU General Public License.
#See the file COPYING.txt for more details.
#Copyright (C) 2018 Fernando Durgam <fdurgam@gmail.com>
#Preferencias/Opciones de Cursor de Revision seguir foco del sistema=false
#Preferencia /modo navegagacion/todo focos =false
import NavigationByKey
class NavigationByKeyL(NavigationByKey.NavigationByKey):
    def __init__(self, name, foco, navegado, url):
        '''
        Constructor
        '''
        super(NavigationByKeyL,self).__init__(name, foco, navegado,url)
if __name__== '__main__':
    x= NavigationByKeyL("evento L","foco","navegado","www.google.com")
    print(x.__str__())