# NVDA Keyboard Event Capture for Mozilla Firefox
#This file is covered by the GNU General Public License.
#See the file COPYING.txt for more details.
#Copyright (C) 2018 Fernando Durgam <fdurgam@gmail.com>
#Preferencias/Opciones de Cursor de Revision seguir foco del sistema=false
#Preferencia /modo navegagacion/todo focos =false
if __name__== '__main__':
    print("hola mundo")
    import sys
    sys.path.insert(0, "..\interactionEvent")
    from eventoAccesibility import *
    y=NavigationByKeyH(sys,"nombre","foco","obj","www.google.com")
    print(y.navegado)
    print("hola mundo")