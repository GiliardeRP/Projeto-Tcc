import os
from Audio.audio import *
import pyautogui as tela
from Programas.programas import Programas as pg
import win32com.client
import re
import pythoncom

class Services:
    
    def abrirProgramas(frase):
        pythoncom.CoInitialize()

        shell = win32com.client.Dispatch("Shell.Application")
        menu_iniciar = shell.NameSpace(0x0)

        for i in range(menu_iniciar.Items().Count):
            item = menu_iniciar.Items().Item(i)
            if hasattr(item, 'Name'):
                nome_item = item.Name
                if re.search(frase, nome_item, re.IGNORECASE):
                    item.InvokeVerb("open")
                    break
        else:
            print("checando pasta.")
    
            programasBase = pg.listarProgramas()
            
            if frase in programasBase and programasBase[frase] is not None:

                os.startfile(programasBase[frase])
                
                Audio.falar('o programa ' + frase +' foi aberto')
                
                return True
            else:
                Audio.falar('Programa não encontrado')
                return False
    
    def digitador(frase):

        tela.sleep(5)

        tela.typewrite(frase)
        Audio.falar('Sua frase foi digitalizada')
        
    def rastrearPasta():
        
        caminhos = [
            os.path.join(os.path.expanduser("~"), "Desktop", "zare"),
            os.path.join(os.path.expanduser("~"), "Área de Trabalho", "zare"),
            os.path.join(os.path.expanduser("~"), "OneDrive", "Área de Trabalho", "zare"),
            os.path.join(os.path.expanduser("~"), "OneDrive", "Desktop", "zare"),
        ]

        for caminho in caminhos:
            if os.path.exists(caminho) and os.path.isdir(caminho):
                return caminho

        return False
    
    def listarProgramas():
        pythoncom.CoInitialize()

        shell = win32com.client.Dispatch("Shell.Application")
        menu_iniciar = shell.NameSpace(0x0)

        names = []
        for i in range(menu_iniciar.Items().Count):
            item = menu_iniciar.Items().Item(i)
            nome_item  = item.Name
            names.append(nome_item)

        frase_completa = ', '.join(names)
        programasBase = pg.listarProgramas()

        programasBase = programasBase.keys()
        
        programasBase = ', '.join(programasBase)
        time.sleep(2)
        Audio.falar('Primeiro os programas encontrados na pasta especial.')
        Audio.falar(programasBase)
        time.sleep(2)
        Audio.falar('Agora os programas que foram encontrados no sistema')
        time.sleep(2)
        Audio.falar(frase_completa)
        


    
    
    #def criadorPasta(nome):
        


