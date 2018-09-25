'''
Created on 18 jun. 2018
aa
@author: fernando
'''
from NVDAObjects.IAccessible.mozilla import Dialog, IAccessible
import ui
import speech
import controlTypes
from NVDAObjects import NVDAObject


class XpathInstance(object):
    '''
    classdocs
    '''
    
    def __init__(self, params):
        '''
        Constructor
        '''
        self.params=params
    
    def funciona(self):
        ui.message("funciona")
    
    def getElementByXpath(self,path,url):
        ui.message("si ejecuta")
        from lxml import html
        import requests
        url='http://192.168.1.110/accesibilidad2/Modo%20Navegacion%20NVDA/ModoNavegacion.php'
        path='/html/body/h1[4]'
        ui.message(path)
        #page=requests.get(url)
        #tree=html.fromstring(page.content)
        #element=tree.xpath(path)
        #ui.message(element)
    def whatSibling(self,element):
        try:
            #return (element.role)
            ui.message("Ejucuta whatSibling ")
            index=1
            #return str(len(element.parent.parent.children))
            child=element.parent.firstChild
            while child and not child==element:
                if child.role==element.role:
                    index+=1
                ui.message(str(child.role))
                child=child.next
            if index>1:
                return("["+str(index)+"]")
            else:
                return ""
            
        except:
            ui.message("Error what sibling")
            if index>1:
                return("["+str(index)+"]")
            else:
                return ""
            
    def tagHtml(self,role):
        try:
            tag={}
            tag["0"]="0" #ROLE_UNKNOWN=0
            tag["1"]="1" #ROLE_WINDOW=1
            tag["2"]="2" #ROLE_TITLEBAR=2
            tag["3"]="3" #ROLE_PANE=3
            tag["4"]="4" #ROLE_DIALOG=4
            tag["5"]="5" #ROLE_CHECKBOX=5
            tag["6"]="6" #ROLE_RADIOBUTTON=6
            tag["7"]="7" #ROLE_STATICTEXT=7
            tag["8"]="8" #ROLE_EDITABLETEXT=8
            tag["9"]="9" #ROLE_BUTTON=9
            tag["10"]="10" #ROLE_MENUBAR=10
            tag["11"]="11" #ROLE_MENUITEM=11
            tag["12"]="12" #ROLE_POPUPMENU=12
            tag["13"]="13" #ROLE_COMBOBOX=13
            tag["14"]="ul" #ROLE_LIST=14
            tag["15"]="15" #ROLE_LISTITEM=15
            tag["16"]="16" #ROLE_GRAPHIC=16
            tag["17"]="17" #ROLE_HELPBALLOON=17
            tag["18"]="18" #ROLE_TOOLTIP=18
            tag["19"]="19" #ROLE_LINK=19
            tag["20"]="20" #ROLE_TREEVIEW=20
            tag["21"]="21" #ROLE_TREEVIEWITEM=21
            tag["22"]="22" #ROLE_TAB=22
            tag["23"]="23" #ROLE_TABCONTROL=23
            tag["24"]="24" #ROLE_SLIDER=24
            tag["25"]="25" #ROLE_PROGRESSBAR=25
            tag["26"]="26" #ROLE_SCROLLBAR=26
            tag["27"]="27" #ROLE_STATUSBAR=27
            tag["28"]="table" #ROLE_TABLE=28
            tag["29"]="td" #ROLE_TABLECELL=29
            tag["30"]="30" #ROLE_TABLECOLUMN=30
            tag["31"]="tr" #ROLE_TABLEROW=31
            tag["32"]="32" #ROLE_TABLECOLUMNHEADER=32
            tag["33"]="33" #ROLE_TABLEROWHEADER=33
            tag["34"]="34" #ROLE_FRAME=34
            tag["35"]="35" #ROLE_TOOLBAR=35
            tag["36"]="36" #ROLE_DROPDOWNBUTTON=36
            tag["37"]="37" #ROLE_CLOCK=37
            tag["38"]="38" #ROLE_SEPARATOR=38
            tag["39"]="39" #ROLE_FORM=39
            tag["40"]="40" #ROLE_HEADING=40
            tag["41"]="41" #ROLE_HEADING1=41
            tag["42"]="42" #ROLE_HEADING2=42
            tag["43"]="43" #ROLE_HEADING3=43
            tag["44"]="44" #ROLE_HEADING4=44
            tag["45"]="45" #ROLE_HEADING5=45
            tag["46"]="46" #ROLE_HEADING6=46
            tag["47"]="47" #ROLE_PARAGRAPH=47
            tag["48"]="48" #ROLE_BLOCKQUOTE=48
            tag["49"]="49" #ROLE_TABLEHEADER=49
            tag["50"]="50" #ROLE_TABLEBODY=50
            tag["51"]="51" #ROLE_TABLEFOOTER=51
            tag["52"]="52" #ROLE_DOCUMENT=52
            tag["53"]="53" #ROLE_ANIMATION=53
            tag["54"]="54" #ROLE_APPLICATION=54
            tag["55"]="55" #ROLE_BOX=55
            tag["56"]="56" #ROLE_GROUPING=56
            tag["57"]="57" #ROLE_PROPERTYPAGE=57
            tag["58"]="58" #ROLE_CANVAS=58
            tag["59"]="59" #ROLE_CAPTION=59
            tag["60"]="60" #ROLE_CHECKMENUITEM=60
            tag["61"]="61" #ROLE_DATEEDITOR=61
            tag["62"]="62" #ROLE_ICON=62
            tag["63"]="63" #ROLE_DIRECTORYPANE=63
            tag["64"]="64" #ROLE_EMBEDDEDOBJECT=64
            tag["65"]="65" #ROLE_ENDNOTE=65
            tag["66"]="66" #ROLE_FOOTER=66
            tag["67"]="67" #ROLE_FOOTNOTE=67
            tag["69"]="69" #ROLE_GLASSPANE=69
            tag["70"]="70" #ROLE_HEADER=70
            tag["71"]="71" #ROLE_IMAGEMAP=71
            tag["72"]="72" #ROLE_INPUTWINDOW=72
            tag["73"]="73" #ROLE_LABEL=73
            tag["74"]="74" #ROLE_NOTE=74
            tag["75"]="75" #ROLE_PAGE=75
            tag["76"]="75" #ROLE_RADIOMENUITEM=76
            tag["77"]="77" #ROLE_LAYEREDPANE=77
            tag["78"]="78" #ROLE_REDUNDANTOBJECT=78
            tag["79"]="79" #ROLE_ROOTPANE=79
            tag["80"]="80" #ROLE_EDITBAR=80
            tag["82"]="82" #ROLE_TERMINAL=82
            tag["83"]="83" #ROLE_RICHEDIT=83
            tag["84"]="84" #ROLE_RULER=84
            tag["85"]="85" #ROLE_SCROLLPANE=85
            tag["86"]="div" #ROLE_SECTION=86
            tag["87"]="87" #ROLE_SHAPE=87
            tag["88"]="88" #ROLE_SPLITPANE=88
            tag["89"]="89" #ROLE_VIEWPORT=89
            tag["90"]="90" #ROLE_TEAROFFMENU=90
            tag["91"]="91" #ROLE_TEXTFRAME=91
            tag["92"]="92" #ROLE_TOGGLEBUTTON=92
            tag["93"]="93" #ROLE_BORDER=93
            tag["94"]="94" #ROLE_CARET=94
            tag["95"]="95" #ROLE_CHARACTER=95
            tag["96"]="96" #ROLE_CHART=96
            tag["97"]="97" #ROLE_CURSOR=97
            tag["98"]="98" #ROLE_DIAGRAM=98
            tag["99"]="99" #ROLE_DIAL=99
            tag["100"]="100" #ROLE_DROPLIST=100
            tag["101"]="101" #ROLE_SPLITBUTTON=101
            tag["102"]="102" #ROLE_MENUBUTTON=102
            tag["103"]="103" #ROLE_DROPDOWNBUTTONGRID=103
            tag["104"]="104" #ROLE_MATH=104
            tag["none"]="none" #ROLE_EQUATION=ROLE_MATH # Deprecated; for backwards compatibility.
            tag["105"]="105" #ROLE_GRIP=105
            tag["106"]="106" #ROLE_HOTKEYFIELD=106
            tag["107"]="107" #ROLE_INDICATOR=107
            tag["108"]="108" #ROLE_SPINBUTTON=108
            tag["109"]="109" #ROLE_SOUND=109
            tag["110"]="110" #ROLE_WHITESPACE=110
            tag["111"]="111" #ROLE_TREEVIEWBUTTON=111
            tag["112"]="112" #ROLE_IPADDRESS=112
            tag["113"]="113" #ROLE_DESKTOPICON=113
            tag["114"]="114" #ROLE_ALERT=114
            tag["115"]="115" #ROLE_INTERNALFRAME=115
            tag["116"]="116" #ROLE_DESKTOPPANE=116
            tag["117"]="117" #ROLE_OPTIONPANE=117
            tag["118"]="118" #ROLE_COLORCHOOSER=118
            tag["119"]="119" #ROLE_FILECHOOSER=119
            tag["120"]="120" #ROLE_FILLER=120
            tag["121"]="121" #ROLE_MENU=121
            tag["122"]="122" #ROLE_PANEL=122
            tag["123"]="123" #ROLE_PASSWORDEDIT=123
            tag["124"]="124" #ROLE_FONTCHOOSER=124
            tag["125"]="125" #ROLE_LINE=125
            tag["126"]="126" #ROLE_FONTNAME=126
            tag["127"]="127" #ROLE_FONTSIZE=127
            tag["128"]="128" #ROLE_BOLD=128
            tag["129"]="129" #ROLE_ITALIC=129
            tag["130"]="130" #ROLE_UNDERLINE=130
            tag["131"]="131" #ROLE_FGCOLOR=131
            tag["132"]="132" #ROLE_BGCOLOR=132
            tag["133"]="133" #ROLE_SUPERSCRIPT=133
            tag["134"]="134" #ROLE_SUBSCRIPT=134
            tag["135"]="135" #ROLE_STYLE=135
            tag["136"]="136" #ROLE_INDENT=136
            tag["137"]="137" #ROLE_ALIGNMENT=137
            tag["138"]="138" #ROLE_ALERT=138
            tag["139"]="139" #ROLE_DATAGRID=139
            tag["140"]="140" #ROLE_DATAITEM=140
            tag["141"]="141" #ROLE_HEADERITEM=141
            tag["142"]="142" #ROLE_THUMB=142
            tag["143"]="143" #ROLE_CALENDAR=143
            tag["146"]="146" #ROLE_CHARTELEMENT=146
            tag["144"]="144" #ROLE_VIDEO=144
            tag["145"]="145" #ROLE_AUDIO=145
            return tag[str(role)]
        except:
            return "Error Tag"
    
    def whatParent(self,element):
        try:
            paths=[]
            #paths.append(element.role)
            padre=element.parent
            while padre and not padre.role==controlTypes.ROLE_DOCUMENT:
                cant=self.whatSibling(padre)
                tagHtml=self.tagHtml(padre.role)
                paths.append(str(tagHtml)+ str(cant))
                padre=padre.parent
            tag=[]
            cadena=""
            for element in reversed(paths):
                tag.append(element)
                cadena=cadena+"/"+str(element)
            return("/html/body"+str(cadena))
        except:
            cadena=""
            for element in reversed(paths):
                tag.append(element)
                cadena=cadena+"/"+str(element)
            return("/html/body"+str(cadena))
            
        
    
    def getElementTreeXPath(self,element):
        try:
            return self.whatParent(element)
            paths=[]
            while element and not element.role==controlTypes.ROLE_DOCUMENT:
                index=0
                sibling=element.previous
                #speech.speakObject(sibling)
                ui.message("calculando TreeXpath")
                #ui.message(str(sibling.role))
                #ui.message("el parent es")
                #speech.speakObject(element.parent)
                #ui.message("rol del parent")
                #ui.message(str(element.parent.role))
                #ui.message("Conetnedor")
                #speech.speakObject(element.container)
                #ui.message("texto")
                #ui.message(element.basicText)
                #ui.message("nombre")
                #ui.message(element.name)
                while sibling:
                    ui.message("El hermano rol")
                    ui.message(str(sibling.role))
                    if sibling.role==controlTypes.ROLE_DOCUMENT:#bueb
                        #ui.message("llego al final")
                        continue
                    if sibling.role==element.role:
                        index+=1
                    #ui.message("siguiente siblig")  
                    sibling=sibling.previous
                    #ui.message(str(sibling.role))
                    #ui.message("siguiente siblig")
                if index>0:
                    index+=1
                    pathIndex="["+str(index)+"]"
                    index=0
                else:
                    pathIndex=""
                tagName=str(element.role)
                #ui.message("tagName+pathIndex")
                #ui.message(str(tagName+pathIndex))
                ui.message("agrega")
                ui.message(tagName+str(pathIndex))
                paths.append(tagName+str(pathIndex))
                element=element.parent
                ui.message("el padre es rol")
                ui.message(str(element.role))
            #ui.message(str(paths))
            return(str(paths))
        except:
            ui.message("Error en xpath")
            ui.message("las contantes son")
            ui.message(str(len(controlTypes.CONSTANT)))
            return None
    
    def getElementXPath(self,element):
        try:
            ui.message("ejecutando getElementXPath")
            key="id"
            if key in element.IA2Attributes.keys():
                ui.message("el id es")
                id=str('//*[@id="'+str(element.IA2Attributes[key]))
                id=id+'"]'
                return id
            else:
                return self.getElementTreeXPath(element)
        except:
            ui.message("Error al getElementXPat")    
if __name__== '__main__':
    x=XpathInstance()