import NavHeader
import NavList
import FlashScrollKey
def getFinders(logger,xpathInstance,url):
    lista=[]
    #lista.append(NavHeader.Finder("busca navegacon entre encabezados"))
    lista.append(NavList.Finder("busca Navegacon entre listas",logger,xpathInstance,url))
    #lista.append(FlashScrollKey.Finder("busca FlashScroll",logger))
    return lista