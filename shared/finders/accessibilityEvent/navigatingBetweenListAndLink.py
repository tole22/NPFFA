# NVDA Keyboard Event Capture for Mozilla Firefox
#This file is covered by the GNU General Public License.
#See the file COPYING.txt for more details.
#Copyright (C) 2018 Fernando Durgam <fdurgam@gmail.com>
#Preferencias/Opciones de Cursor de Revision seguir foco del sistema=false
#Preferencia /modo navegagacion/todo focos =false


#import ui
#import api
#import speech
#from interactionEvent.eventoAccesibility import *
from accessibilityEvent import event
class ContentOverlooked(event):
    def __init__(self, name, listEventInteraction, reportLogger):
        super(ContentOverlooked,self).__init__(name,listEventInteraction,reportLogger)
      

if __name__== '__main__':
    x=ContentOverlooked("ContentOverlooked","fd","parametros")
    #print (x.getReportLogger())