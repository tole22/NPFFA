# NVDA Keyboard Event Capture for Mozilla Firefox
#This file is covered by the GNU General Public License.
#See the file COPYING.txt for more details.
#Copyright (C) 2018 Fernando Durgam <fdurgam@gmail.com>
#Preferencias/Opciones de Cursor de Revision seguir foco del sistema=false
#Preferencia /modo navegagacion/todo focos =false
#

from conexiones.logger import logger
class program():
    lista=[]
    def __init__(self):
        self.logger=logger("192.168.10.110", "self.token", False)

    def getLista(self):
        return "si"
    

if __name__== '__main__':
    x=program()
    print(x.getLista())