from Services.services import Services 
from Audio.audio import Audio
import threading
import datetime
from Banco.model import *
from Tela.tela import Tela
import keyboard
import sys

def main_loop():
    trava = 1
    while trava == 1:
        
        Audio.falar('Diga o comando')

        frase = Audio.ouvir()
        print(frase)

        if 'abrir' in frase:
            frase = frase.replace('abrir ', '')
            print(frase)
            Services.abrirProgramas(frase)
            trava = 0
        elif 'escreva' in frase:
            Audio.falar('Diga sua frase')
            frase = Audio.ouvir()
            Services.digitador(frase)
            Tela.exibirInformacoes('Frase foi digitalizada, aguardando o próximo comando.')
            trava = 0
        elif 'lista' in frase:
            Audio.falar('Certo, aguarde enquanto listo os programas do seu computador')
            Services.listarProgramas()
            Tela.exibirInformacoes('Listando os programas reconhecidos.')
            trava = 0
        elif 'cancelar' in frase:
            Audio.falar('Certo, estou à sua disposição, caso precise basta acionar o atalho')
            Tela.exibirInformacoes('Comando de voz cancelado.')
            trava = 0
        elif "horas" in frase:
            now = datetime.datetime.now()
            dateStr = now.strftime("%H:%M")
            Audio.falar('Agora são: ' + dateStr)
            Tela.exibirInformacoes(f'Horas: {dateStr}')
            trava = 0
        elif "data" in frase:
            now = datetime.datetime.now()
            dateStr = now.strftime("%d/%m/%Y")
            Audio.falar('Hoje é: ' + dateStr)
            Tela.exibirInformacoes(f'Data: {dateStr}')
            trava = 0
        elif "pesquise" or "pesquisa"   in frase:
            frase = frase.replace('pesquise ', '')
            frase = frase.replace('pesquisa ', '')
            print(frase)
            if "site" in frase: 
                Audio.falar('Diga somente a url de busca')
                frase = Audio.ouvir()
                Services.pesquisaWeb(frase, 'url')
                Audio.falar('O site: ' + frase + ' foi aberto')
                trava = 0 
                return
            Audio.falar('O que você quer pesquisar?')
            frase = Audio.ouvir()
            Services.pesquisaWeb(frase,'')
            Audio.falar('Sua pesquisa sobre: ' + frase + ' foi realizada')
            trava = 0
            return
        else:
            Audio.falar('Não entendi')
            
    return
    
def main():
    Audio.falar('O Zare está iniciando, por favor aguarde')
    check = Services.rastrearPasta()

    if check != False:
        
        Services.start()
        Model.insertDb(check)

        thread_window = threading.Thread(target=Tela.createWindow)
        thread_window.start()
        
        Audio.falar('O Zare já está disponível para uso')
        
        while True:
            
            if Tela.isWindowOpen():
                if keyboard.is_pressed('ctrl+alt+p'):
                    main_loop()
            else: 
                Model.deleteDataDb()
                sys.exit(0)
                
        
    Audio.falar('Houve algum problema com o diretório da pasta de programas')

if __name__ == '__main__':
    main()
