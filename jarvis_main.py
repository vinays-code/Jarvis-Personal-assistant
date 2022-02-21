import datetime
from os import name
import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import subprocess
import os
from gtts import gTTS
audio = gTTS(text='I love Python for text to speech, and you?', lang='en-US', slow=True)
audio.save('message.mp3')
os.system('afplay message.mp3')
audio_en = gTTS('hello', lang='en')
audio_it = gTTS('ciao', lang='it')

with open('hello_ciao.mp3', 'wb') as f:
    audio_en.write_to_fp(f)
    audio_it.write_to_fp(f)
    
os.system("afplay hello_ciao.mp3")
def say(text):
    engine.setProperty('voice', 'com.apple.speech.synthesis.voice.samantha')
    engine.say("Hi, vinay welcome to singhaania industries") 
    engine.runAndWait() 
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate+100)
    volume = engine.getProperty('volume')
    engine.setProperty('volume', volume-0.50)
name=input('plz enter your name:')
say("hi {} sir welcome to singhania industries".format(name))


r = sr.Recognizer()
mic = sr.Microphone()
with mic as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
    transcript = r.recognize_google(audio)
    transcript.lower()
    print(transcript)

d = '/Applications'
apps = list(map(lambda x: x.split('.app')[0], os.listdir(d)))

engine = pyttsx3.init()
voices = engine.getProperty('voices') 

for voice in voices:
    if 'en_US' in voice.languages or 'en_GB' in voice.languages:
        print(voice.id)






if 'open imovie' in transcript:

    app = 'imovie'
    os.system('open ' +d+'/%s.app' %app.replace(' ','\ '))


elif 'open prodcasts' in transcript:

    app = 'prodcasts'
    os.system('open ' +d+'/%s.app' %app.replace(' ','\ '))


elif 'open safari' in transcript:

    app = 'safari'
    os.system('open ' +d+'/%s.app' %app.replace(' ','\ '))
elif 'open chrome' in transcript:

    app = 'chrome'
    os.system('open ' +d+'/%s.app' %app.replace(' ','\ '))
elif 'the time' in transcript:
    strTime= datetime.datetime.now()
    strTime('%H:%M:%S')
    say(f"sir the time is {strTime}")

else:
    say('plz say it again ')
