#import threading
from Services.services import Services as server
from Audio.audio import Audio as audio
from tkinter import *
#import time
import keyboard
import datetime
from Banco.model import *


class Main:

        
    def start():
            
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
                frase = frase.replace('digite ', '')
                print('DIGITATROM: ', frase)
                server.digitador(frase)
                start = 0
            elif 'lista' in frase:
                audio.falar('Certo aguarde enquanto listarei os programas do seu computador')
                server.listarProgramas()
                start = 0
            elif 'cancelar' in frase:
                audio.falar('Certo, estou a sua disposição, caso precise basta acionar o atalho')
                start = 0
            elif "horas" in frase:
                now = datetime.datetime.now()
                date_str = now.strftime("%H:%M")
                audio.falar('Agora são: ' + date_str)
                start = 0
            elif "data" in frase:
                now = datetime.datetime.now()
                date_str = now.strftime("%d/%m/%Y")
                audio.falar('Hoje é: ' + date_str)
                start = 0
            else:
                audio.falar('Nao entendi')


check = server.rastrearPasta()

if check != False:
    Model.insertDb(check)
    
    keyboard.add_hotkey('ctrl+alt+p', lambda: Main.start() )
    keyboard.wait()

audio.falar('Tem algo de errado com o diretório da pasta de programas')










# janela = Tk()
# janela.title('Assistente')
# textoOrientacao = Label(janela, text='Diga o comando')
# textoOrientacao.grid(column=3, row=3, padx=10, pady=10)

# t = threading.Thread(target=lambda: (time.sleep(1), audio.falar('Diga o comando')))
# t.start()

# janela.mainloop()