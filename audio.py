import speech_recognition as voz
from playsound import playsound as ps # tocador de som 
import gtts #modulo do google para convertter texto em voz 

class Audio:
    
    def ouvir():
        mic = voz.Recognizer() 
             
        with voz.Microphone() as source:
        
            mic.adjust_for_ambient_noise(source)
            audio = mic.listen(source)
            frase = mic.recognize_google(audio, language='pt-BR')
            
            return frase.lower()
    
    def falar(frase):
        
        print(frase)
        
        objFrase =gtts.gTTS(frase, lang='pt-br')
        objFrase.save('audio.mp3')
        ps('audio.mp3')
