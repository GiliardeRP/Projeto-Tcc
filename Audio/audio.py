import speech_recognition as voz
from playsound import playsound as ps # tocador de som 
import gtts #modulo do google para convertter texto em voz 
import time
import os
import pygame



class Audio:
    def ouvir():
        mic = voz.Recognizer()
        while True:
            with voz.Microphone() as source:
                mic.adjust_for_ambient_noise(source)
                audio = mic.listen(source, timeout=5, phrase_time_limit=15)
            try:
                frase = mic.recognize_google(audio, language='pt-BR')
                if frase:
                    return frase.lower()
            except voz.UnknownValueError:
                Audio.falar("Não consegui entender o que você disse.")
                
            except voz.RequestError:
                Audio.falar("Não foi possível se conectar ao serviço de reconhecimento de voz.")
             
            except KeyboardInterrupt:
                Audio.falar("Processo de reconhecimento de voz cancelado pelo usuário.")
                
                return False
        
    def falar(frase):

        objFrase =gtts.gTTS(frase, lang='pt-br')
        objFrase.save( 'audio.mp3')
        
        pygame.mixer.init()

        pygame.mixer.music.load('audio.mp3')

        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

        pygame.mixer.quit()
        
        os.remove('audio.mp3')
       
        
        


       
