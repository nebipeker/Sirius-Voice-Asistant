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

wikipedia.set_lang("en")
r = sr.Recognizer()
def record():
    print('listening')
    with sr.Microphone() as source:
        audio = r.listen(source)
        voice =''
        try:
            voice = r.recognize_google(audio)  #, language='tr-TR'
        except sr.UnknownValueError:
            print('You are not recognized')
        except sr.RequestError:
            print('Request error')
        voice = voice.lower()
        print(voice)
        return(voice)

def respond(voice):
    tts = gTTS(text=voice, lang='en') #en
    r = random.randint(1, 20000000)
    filename = "respond" +str(r)+'.mp3'
    tts.save('voices/'+filename)
    playsound.playsound('voices/'+filename)

def evaluate(input):
    if('who am i' in input): # Who am i without ego :)
        return respond('You are the supreme leader')
    elif ('make a search' in input):  # Making search at google
        search_term = input.split("for")[-1]
        url = f"https://google.com/search?q={search_term}"
        webbrowser.get().open(url)
        return respond('This is what i find for '+ str(search_term))

    elif ('search location' in input):  #making a search on google maps
        search_term = input.split("for")[-1]
        url = f"https://www.google.com.tr/maps/place/{search_term}"
        webbrowser.get().open(url)
        return respond('This is what i find for location' + str(search_term))

    elif ('search wikipedia' in input): # Wikipedia search
        data = input.split('for')[-1]

        if('chrome' in input):
            data = input.split('with')
            url = wikipedia.page(data).url
            webbrowser.get().open(url)
            return (respond('Opened in browser sir'))
        else:
            page = wikipedia.summary(str(data),sentences=2)
            return respond(page)

    elif ('go to admin website' in input): # Administrator website
        url = 'http://pekercelik.com'
        webbrowser.get().open(url)
        return respond('confirmed')

    elif ('search youtube' in input): # Youtube search
        key = input.split('for')[-1]
        url = 'https://www.youtube.com/results?search_query='+key
        webbrowser.get().open(url)


while True:
    print('Ready for your orders sir')
    data = record()
    if('sirius' in data):
        respond('At your service sir')
        evaluate(record())
    data = ''