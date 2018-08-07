'''
Created on 26 jun. 2018
@author: fernando
'''
import sys
from Tkinter import *
import configuracion
import Tkinter

def ejecutar():
    App.ejecutar(self)

class App():
    def __init__(self, master):      
        frame = Frame(master)
        self.frame=frame
        frame.pack()
        token= Tkinter.StringVar()
        token.set(configuracion.getToken())
        server=Tkinter.StringVar()
        server.set(configuracion.getServer())
        lblToken=Label(frame,text="Token").pack()
        self.entToken=Entry(frame,textvariable=token)
        self.entToken.pack()
        lblServer=Label(frame,text="Server").pack()
        self.entServer=Entry(frame,textvariable=server)
        self.entServer.pack()
        btnAceptar=Button(frame,text="Aceptar", command=self.guardar).pack()
        btnCancelar=Button(frame,text="Cancelar", command=frame.quit).pack()
    
    def guardar(self):
        print "El Server es: ",self.entServer.get()
        print "El Token es: ",self.entToken.get()
        configuracion.setServer(self.entServer.get())
        configuracion.setToken(self.entToken.get())
        self.frame.quit()
   
    def ejecutar(self):
        root=Tk()
        ap=App(root)
        root.mainloop()

if __name__ == '__main__':
    root=Tkinter.Tk()
    ap=App(root)
    root.mainloop()