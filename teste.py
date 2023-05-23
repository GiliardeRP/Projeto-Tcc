import PySimpleGUI as sg
from Services.services import Services as server
from Audio.audio import Audio as audio
import threading

import tkinter as tk
#import time
import keyboard
import datetime
from Banco.model import *



def exibir_informacoes(informacoes):
    window['-TEXTO-'].update(informacoes)


def main_loop():
    while True:
        exibir_informacoes('Ouvindo')  # Exibir "Ouvindo" na tela

        audio.falar('Diga o comando')

        frase = audio.ouvir()
        print(frase)

        if 'abrir' in frase:
            frase = frase.replace('abrir ', '')
            print(frase)
            server.abrirProgramas(frase)
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
    layout = [
        [sg.Text('Informações:', key='-ROTULO-')],
        [sg.Text('', key='-TEXTO-')],
    ]

    global window  # torna a variável window global

    window = sg.Window('Janela de Informações', layout, finalize=True)

    thread_loop = threading.Thread(target=main_loop)
    thread_loop.start()

    while True:
        event, values = window.read(timeout=100)  # Defina um tempo de espera para atualizar a janela
        if event == sg.WINDOW_CLOSED:
            break

        # Atualize o elemento de texto com as informações relevantes
        # Aqui você pode utilizar variáveis ou funções para obter as informações que deseja exibir
        informacoes = "Informações atualizadas"
        exibir_informacoes(informacoes)

    # Aguarde o término do loop principal antes de fechar a janela
    thread_loop.join()
    window.close()


check = server.rastrearPasta()

if check != False:
    Model.insertDb(check)

    keyboard.add_hotkey('ctrl+alt+p', lambda: main())
    keyboard.wait()

audio.falar('Houve algum problema com o diretório da pasta de programas')
