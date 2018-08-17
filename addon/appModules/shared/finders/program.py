# NVDA Keyboard Event Capture for Mozilla Firefox
#This file is covered by the GNU General Public License.
#See the file COPYING.txt for more details.
#Copyright (C) 2018 Fernando Durgam <fdurgam@gmail.com>
#Preferencias/Opciones de Cursor de Revision seguir foco del sistema=false
#Preferencia /modo navegagacion/todo focos =false



if __name__== '__main__':
    import sys
    import importlib
    import os
    dirname, basename = os.path.split(os.path.abspath(os.path.dirname(__file__)))
    sys.path.append(dirname)
    from shared.eventoAccesibility import *
    x=NavigationByKeyH("nombre","foco","obj","","www.google.com")
    print(str(type(x)))
    print("no")
    