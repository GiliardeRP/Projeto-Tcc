import PySimpleGUI as sg
from Services.services import Services as server
from Audio.audio import Audio as audio
import threading
import datetime
from Banco.model import *
import keyboard
import sys

def exibir_informacoes(informacoes):
    window['-TEXTO-'].update(informacoes)

def create_window():
    layout = [
        [sg.Text('Informações:', key='-ROTULO-')],
        [sg.Text('', key='-TEXTO-')],
    ]
    global window
    window = sg.Window('Janela de Informações', layout, finalize=True)
    
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
        exibir_informacoes('Ouvindo')  # Exibir "Ouvindo" na tela

        audio.falar('Diga o comando')

        frase = audio.ouvir()
        print(frase)

        if 'abrir' in frase:
            exibir_informacoes('abrindo')
            frase = frase.replace('abrir ', '')
            print(frase)
            server.abrirProgramas(frase)
            break
        elif 'digite' in frase:
            frase = frase.replace('digite ', '')
            print('DIGITATROM: ', frase)
            server.digitador(frase)
        elif 'lista' in frase:
            audio.falar('Certo, aguarde enquanto listo os programas do seu computador')
            server.listarProgramas()
        elif 'cancelar' in frase:
            audio.falar('Certo, estou à sua disposição, caso precise basta acionar o atalho')
            break
        elif "horas" in frase:
            now = datetime.datetime.now()
            date_str = now.strftime("%H:%M")
            audio.falar('Agora são: ' + date_str)
        elif "data" in frase:
            now = datetime.datetime.now()
            date_str = now.strftime("%d/%m/%Y")
            audio.falar('Hoje é: ' + date_str)
        else:
            audio.falar('Não entendi')

def main():
    check = server.rastrearPasta()

    if check != False:
        Model.insertDb(check)

        thread_window = threading.Thread(target=create_window)
        thread_window.start()

        keyboard.add_hotkey('ctrl+alt+p', lambda: main_loop())
        keyboard.wait()
        

        thread_window.join()

    audio.falar('Houve algum problema com o diretório da pasta de programas')

if __name__ == '__main__':
    main()
