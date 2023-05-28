import os
from Banco.model import *
 
class Programas:
    
       def programaPasta():
        
        banco = Model.selectDb()
        
        pasta = r''+banco[0][1]

        arquivos = os.listdir(pasta)
        
        arquivos_exe = [arquivo for arquivo in arquivos ]
        
        programasBase = {}  
         
        for arquivo_exe in arquivos_exe:
            nome_arquivo = os.path.splitext(arquivo_exe)[0]
            programasBase[nome_arquivo] = (os.path.join(pasta, arquivo_exe))
            
        return programasBase

