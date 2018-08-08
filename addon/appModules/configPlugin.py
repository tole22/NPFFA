# NVDA Keyboard Event Capture for Mozilla Firefox
#This file is covered by the GNU General Public License.
#See the file COPYING.txt for more details.
#Copyright (C) 2018 Fernando Durgam <fdurgam@gmail.com>
from conexiones import logger
import subprocess
import os
#import ConfigParser
#import requests
def getToken():
	x=conf()
	return x.getToken()

def getServer():
	return conf().getServer()

def getDirPython():
	return conf().getDirPython()

def directorio():
	#return abspath(getsourcefile(lambda:0))
	return os.path.dirname(os.path.abspath(__file__))

class conf():
	def __init__(self):
		self.file=directorio()+"\conf.ini"
		file=open(self.file)
		self.lines=file.readlines()
		file.close()
		
	def getServer(self):
		for line in self.lines:
			valor=line.split()
			if valor[0]=="server":
				return valor[2]
				break
	
	def getToken(self):
		for line in self.lines:
			valor=line.split()
			if valor[0]=="token":
				return valor[2]
				break
			
	def getDirPython(self):
		for line in self.lines:
			valor=line.split()
			if valor[0]=="python":
				return valor[2]
				break	
	
		
if __name__ == '__main__':
	#print os.path.dirname(os.path.abspath(__file__))
	print "Server: ",getServer()," - Token: ",getToken()," - Dir Python:",getDirPython()
	print conf().file
	folder=os.path.dirname(os.path.abspath(__file__))+"\conf\\readDatos.py"
	print folder
	retcode=subprocess.call('python '+ str(folder))
	logger.logger(getServer(),getToken(),False).prueba()
	