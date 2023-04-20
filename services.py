import os
import pyautogui as tela
from audio import Audio as audio
from programas import Programas as pg


class Services:
    
   
    def abrirProgramas(frase):
    
        programasBase = pg.listarProgramas()
        
        if programasBase[frase]: 
            os.startfile(programasBase[frase])
            audio.falar('o programa ' + frase +' foi aberto')
            
            return True
        else:
            return False
    
    def digitador(frase):
                
        tela.sleep(5)

        tela.typewrite(frase)