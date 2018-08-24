import NavHeader
import NavList
import FlashScrollKey
def getFinders(logger):
    lista=[]
    lista.append(NavHeader.Finder("busca h"))
    lista.append(NavList.Finder("busca l"))
    lista.append(FlashScrollKey.Finder("busca FlashScroll",logger))
    return lista