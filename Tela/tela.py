import PySimpleGUI as sg

class Tela:

    def exibirInformacoes(informacoes):
        window['-TEXTO-'].update(informacoes)

    def createWindow():
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
        
    def isWindowOpen():
        return window.TKroot.winfo_exists()
    
    
    