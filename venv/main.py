import pyaudio
from gtts import gTTS
import playsound
import speech_recognition as sr
import random
import webbrowser
import wikipedia


"""
###########################################################################################################################
@author Peker Çelik
Linkedin: https://www.linkedin.com/in/pekercelik/
Github: https://github.com/nebipeker
Kaggle: https://www.kaggle.com/nebipeker
Website: http://pekercelik.com
Date: 08/08/2020
###########################################################################################################################
"""

wikipedia.set_lang("tr")
r = sr.Recognizer()
def record():
    print('Listening')
    with sr.Microphone() as source:
        audio = r.listen(source)
        voice =''
        try:
            voice = r.recognize_google(audio, language='en')  #, language='tr-TR'
        except sr.UnknownValueError:
            print('')
        except sr.RequestError:
            print('Request error')
        voice = voice.lower()
        #print(voice)
        return(voice)

def respond(voice):
    print("Sirius: " + voice)
    tts = gTTS(text=voice, lang='en') #en
    r = random.randint(1, 20000000)
    filename = "respond.mp3" #+str(r)+'.mp3'
    # tts.save('voices/'+filename)
    playsound.playsound('voices/'+filename)

def evaluate(input):
    """
    if('sirius' in input):
        respond("I will end the organic life")
    """
    print("You: Sirius")
    respond("I will end the organic life")








print('Sirius: Ready for your orders sir')
data = record()
evaluate(data)
data = ''     