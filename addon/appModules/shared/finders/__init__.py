import NavHeader
import NavList
import FlashScrollKey
def getFinders():
    lista=[]
    lista.append(NavHeader.Finder("busca navegacon entre encabezados"))
    lista.append(NavList.Finder("busca Navegacon entre listas"))
    lista.append(FlashScrollKey.Finder("busca FlashScroll"))
    return lista