import os
import psutil
import pyautogui as tela
from audio import Audio as audio
from programas import Programas as pg


class Services:
    
   
    def abrirProgramas(frase):
    
        programasBase = pg.listarProgramas()
        
        print(programasBase)
        
        if programasBase[frase]: 
            os.startfile(programasBase[frase])
            
            audio.falar('o programa ' + frase +' foi aberto')
            
            return True
        else:
            return False
    
    def digitador(frase):
                
        tela.sleep(5)

        tela.typewrite(frase)
        
    def rastrearPasta(nome):
        
        desktop_path = os.path.join(os.environ["HOMEPATH"], "Desktop")
        
        if os.path.exists(desktop_path + '\\' + nome) and os.path.isdir(desktop_path + '\\' + nome):
            return True
        else: 
            return False
    
    def criadorPasta(nome):
        


