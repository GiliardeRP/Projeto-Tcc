import os
from Audio.audio import Audio
import pyautogui as tela
from Programas.programas import Programas as pg
import win32com.client
import re
import pythoncom
import keyboard
import webbrowser

from Tela.tela import Tela

class Services:
    
    def start():
        if(os.path.exists("listaPrograma.mp3")):
            os.remove('listaPrograma.mp3')
            
        pythoncom.CoInitialize()

        shell = win32com.client.Dispatch("Shell.Application")
        menu_iniciar = shell.NameSpace(0x0)

        names = []
        for i in range(menu_iniciar.Items().Count):
            item = menu_iniciar.Items().Item(i)
            nome_item  = item.Name
            names.append(nome_item)

        fraseCompleta = ', '.join(names)

        Audio.recordAudio(fraseCompleta)
    
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
                    Audio.falar('o programa ' + frase +' foi aberto')
                    Tela.exibirInformacoes(f'Abrindo: {frase}.' )
                    break
        else:
            print("checando pasta.")
    
            programasBase = pg.programaPasta()
            
            if frase in programasBase and programasBase[frase] is not None:

                os.startfile(programasBase[frase])
                
                Audio.falar('o programa ' + frase +' foi aberto')
                Tela.exibirInformacoes(f'Abrindo: {frase}.' )
                
                return True
            else:
                Audio.falar('Programa não encontrado, aquardando o próximo comando')
                Tela.exibirInformacoes('Programa não encontrado')
                return False
    
    def digitador(frase):

        tela.sleep(4)
    
        keyboard.write(frase)

        Audio.falar('A seguinte frase:   ' + frase + 'foi digitalizada' )
        
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
    
        if (os.path.exists("listaPrograma.mp3")):
            
            programasBase = pg.programaPasta()

            programasBase = programasBase.keys()
        
            programasBase = ', '.join(programasBase)
        
            Audio.falar('Primeiro os programas encontrados na pasta especial.')
            Audio.falar(programasBase)
        
            Audio.falar('Agora os programas que foram encontrados no sistema')
            Audio.loadAudio()
        else:
            
            pythoncom.CoInitialize()

            shell = win32com.client.Dispatch("Shell.Application")
            menu_iniciar = shell.NameSpace(0x0)

            names = []
            for i in range(menu_iniciar.Items().Count):
                item = menu_iniciar.Items().Item(i)
                nome_item  = item.Name
                names.append(nome_item)

            frase_completa = ', '.join(names)
            programasBase = pg.programaPasta()

            programasBase = programasBase.keys()
            
            programasBase = ', '.join(programasBase)
            
            Audio.falar('Primeiro os programas encontrados na pasta especial.')
            Audio.falar(programasBase)
            
            Audio.falar('Agora os programas que foram encontrados no sistema')
            
            Audio.falar(frase_completa)
        
    def pesquisaWeb(frase, type):

        if type == "url":
            webbrowser.open(frase)
            return
            
        url = f'https://www.google.com/search?q={frase}'
        webbrowser.open(url)