# NVDA Keyboard Event Capture for Mozilla Firefox
#This file is covered by the GNU General Public License.
#See the file COPYING.txt for more details.
#Copyright (C) 2018 Fernando Durgam <fdurgam@gmail.com>

from datetime import datetime, timedelta
from threading import Timer
import speech
import controlTypes
import api
import addonHandler

addonHandler.initTranslation()

def getUrl():
	return "http://192.168.1.110/accesibilidad2/Modo%20Navegacion%20NVDA/ModoNavegacion.php"