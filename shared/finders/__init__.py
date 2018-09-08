import NavHeader
import NavList
import FlashScrollKey
def getFinders(logger,xpathInstance):
    lista=[]
    #lista.append(NavHeader.Finder("busca navegacon entre encabezados"))
    lista.append(NavList.Finder("busca Navegacon entre listas",logger,xpathInstance))
    #lista.append(FlashScrollKey.Finder("busca FlashScroll",logger))
    return lista