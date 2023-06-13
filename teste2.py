import PySimpleGUI as sg
from Services.services import Services 
from Audio.audio import Audio
import threading
import datetime
from Banco.model import *
import keyboard


def exibir_informacoes(informacoes):
    window['-TEXTO-'].update(informacoes)

def create_window():
    layout = [
        [sg.Text('Informações:', key='-ROTULO-')],
        [sg.Text('', key='-TEXTO-')],
    ]
    global window
    window = sg.Window('ZARE - Janela de Informações', layout,size=(350, 150), finalize=True)
    
    window.finalize()  # Finaliza a criação da janela antes de configurar a posição
    window.TKroot.geometry(f"+{100}+{100}")

    while True:
        event, values = window.read(timeout=100)  # Defina um tempo de espera para atualizar a janela
        if event == sg.WINDOW_CLOSED:
            break

        # Atualize o elemento de texto com as informações relevantes
        # Aqui você pode utilizar variáveis ou funções para obter as informações que deseja exibir

    window.close()

def main_loop():
    while True:

        Audio.falar('Diga o comando')

        frase = Audio.ouvir()
        print(frase)

        if 'abrir' in frase:
            exibir_informacoes('abrindo')
            frase = frase.replace('abrir ', '')
            print(frase)
            Services.abrirProgramas(frase)
            break
        elif 'escreva' in frase:
            frase = frase.replace('escreva ', '')
            print('DIGITATROM: ', frase)
            Services.digitador(frase)
            break
        elif 'lista' in frase:
            Audio.falar('Certo, aguarde enquanto listo os programas do seu computador')
            Services.listarProgramas()
            break
        elif 'cancelar' in frase:
            Audio.falar('Certo, estou à sua disposição, caso precise basta acionar o atalho')
            break
        elif "horas" in frase:
            now = datetime.datetime.now()
            date_str = now.strftime("%H:%M")
            Audio.falar('Agora são: ' + date_str)
            break
        elif "data" in frase:
            now = datetime.datetime.now()
            date_str = now.strftime("%d/%m/%Y")
            Audio.falar('Hoje é: ' + date_str)
            break
        else:
            Audio.falar('Não entendi')

def main():
    Audio.falar('Zare está iniciando, por favor aguarde')
    check = Services.rastrearPasta()

    if check != False:
        
        Services.start()
        Model.insertDb(check)

        thread_window = threading.Thread(target=create_window)
        thread_window.start()
        Audio.falar('O Zare já está disponível para uso')

        keyboard.add_hotkey('ctrl+alt+p', lambda: main_loop())
        keyboard.wait()
        
        thread_window.join()

    Audio.falar('Houve algum problema com o diretório da pasta de programas')

if __name__ == '__main__':
    main()
