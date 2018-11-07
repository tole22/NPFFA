import NavHeader
import NavList
import FlashScrollKey
import NavListAndLink
import roles
def getFinders(logger,xpathInstance,url):
    lista=[]
    lista.append(NavHeader.Finder("busca navegacon entre encabezados",logger,xpathInstance,url))
    lista.append(NavList.Finder("busca Navegacon entre listas",logger,xpathInstance,url))
    #lista.append(roles.Finder("Descubrir roles",logger,xpathInstance,url))
    lista.append(NavListAndLink.Finder("Busca Navegacion entre listas y enlaces",logger,xpathInstance,url))
    lista.append(FlashScrollKey.Finder("busca FlashScroll",logger,xpathInstance,url))
    return lista