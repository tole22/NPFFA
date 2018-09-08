'''
Created on 18 jun. 2018

@author: fernando
'''
from navigationByKeyH import NavigationByKeyH
from navigationByKeyB import NavigationByKeyB
if __name__== '__main__':
    x= NavigationByKeyH("evento h","www.google.com.ar","foco","navegado")
    y= NavigationByKeyB("evento b","www.google.com.ar","foco","navegado")
    print(x.__str__())
    print(y.__str__())
        