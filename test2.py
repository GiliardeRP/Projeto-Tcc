import win32com.client
from audio import *

shell = win32com.client.Dispatch("Shell.Application")
menu_iniciar = shell.NameSpace(0x0)

names = []
for i in range(menu_iniciar.Items().Count):
    item = menu_iniciar.Items().Item(i)
    nome_item  = item.Name
    names.append(nome_item)
    #print(nome_item)


frase_completa = ', '.join(names)

Audio.falar(frase_completa)

(frase_completa)