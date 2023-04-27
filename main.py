
from services import Services as server
from audio import Audio as audio


while True:
    frase = audio.ouvir()
    frase = frase.replace('abrir ', '')
    print(frase)
    
    server.abrirProgramas(frase)

