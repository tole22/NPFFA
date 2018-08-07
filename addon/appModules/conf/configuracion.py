'''
Created on 28 jun. 2018

@author: fernando
'''
import ConfigParser
def getArchivo():
    return "../conf.ini"

def guardar(server,token):
    #f = open('conf.ini', 'w')
    config = ConfigParser.ConfigParser()
    config.read(getArchivo())
    config.set("CONEXION", "server", server)
    config.set("CONEXION", "token", token)
    config.write(open('conf.ini','w'))

def default():
    config = ConfigParser.ConfigParser()
    config.read(getArchivo())
    config.set("CONEXION", "server", "localhost")
    config.set("CONEXION", "token", "111111111")
    config.write(open('conf.ini','w'))

def leer():
    config = ConfigParser.ConfigParser()
    config.read(getArchivo())
    token = config.get('CONEXION', 'token')
    print "Token:",token
    server = config.get('CONEXION', 'server')
    print "Server:",server

def getToken():
    cnn=conexiones()
    return cnn.token()

def getServer():
    cnn=conexiones()
    return cnn.server()

def setServer(server):
    cnn=conexiones()
    cnn.newServer(server)
    
def setToken(token):
    cnn=conexiones()
    cnn.newToken(token)
    
class conexiones():
    
    def token(self):
        config = ConfigParser.ConfigParser()
        config.read(getArchivo())
        token = config.get('CONEXION', 'token')
        return token
    
    
    def server(self):
        config = ConfigParser.ConfigParser()
        config.read(getArchivo())
        server = config.get('CONEXION', 'server')
        return server
    
    def newServer(self,server):
        config = ConfigParser.ConfigParser()
        config.read(getArchivo())
        config.set("CONEXION", "server", server)
        config.write(open(getArchivo(),'w'))
        
    def newToken(self,token):
        config = ConfigParser.ConfigParser()
        config.read(getArchivo())
        config.set("CONEXION", "token", token)
        config.write(open(getArchivo(),'w'))
        
if __name__ == '__main__':
    x=conexiones()
    #guardar("www.oran.uns.eduar", "888888")
    print "Token:",x.token(),"Server:", x.server()    