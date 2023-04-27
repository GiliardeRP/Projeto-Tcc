import os
 
class Programas:
    
       def listarProgramas():
    
        pasta = r"C:\Users\gilia\OneDrive\Área de Trabalho\teste"

        arquivos = os.listdir(pasta)
        
        arquivos_exe = [arquivo for arquivo in arquivos ]
        
        programasBase = {}  
        # programasBase = {'google chrome': 'chrome.exe',
        #                  'bloco de notas': 'notepad.EXE',
        #                  'calculadora': 'calc.exe',
        #                  'arquivos': 'explorer.exe'}  
         
        for arquivo_exe in arquivos_exe:
            nome_arquivo = os.path.splitext(arquivo_exe)[0]
            programasBase[nome_arquivo] = (os.path.join(pasta, arquivo_exe))
            
        return programasBase

