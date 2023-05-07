import threading
from services import Services as server
from audio import Audio as audio
from tkinter import *
import time

# janela = Tk()
# janela.title('Assistente')
# textoOrientacao = Label(janela, text='Diga o comando')
# textoOrientacao.grid(column=3, row=3, padx=10, pady=10)

# t = threading.Thread(target=lambda: (time.sleep(1), audio.falar('Diga o comando')))
# t.start()

# janela.mainloop()
    
start = 1

while start !=0:
    
    audio.falar('Diga o comando')

    frase = audio.ouvir()
    print( frase)

    if 'abrir' in frase:
        
        frase = frase.replace('abrir ', '')
        print(frase)
        server.abrirProgramas(frase)
        start = 0
        
    elif 'digite' in frase:
        print('DIGITATROM: ', frase)
        server.digitador(frase)
        start = 0
    elif 'lista' in frase:
        audio.falar('Certo aguarde enquanto listarei os programas do seu computador')
        
        server.listarProgramas()
    
    audio.falar('Nao entendi')





        
    













