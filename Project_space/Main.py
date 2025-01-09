import speech_recognition as sr #dont forgot pyaudio ah lmao
import pyttsx3
import pywhatkit
import datetime
import wikipedia
from google.cloud import texttospeech


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

talk('Hi I am Jarvis, what is your focus today?')

while True:
    try:
        with sr.Microphone() as source:
            print('listening...')
            engine.runAndWait()
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            
            command = command.lower()
            print(command)

            if ('play' or 'song') in command:
                talk('playing'+ command) 
                pywhatkit.playonyt(command)
            elif 'time' in command:
                time = datetime.datetime.now().strftime('%H:%M %p')
                print(time)
                talk('Çurrent time is ' + time)
            elif 'who is' in command:
                search = command.replace('who is', '')
                info = wikipedia.summary(search, 1)
                print(info)
                talk(info)
            elif 'open' in command:
                from dictapp import openappweb
                openappweb(command)
            elif 'whatsapp' in command:
                from Whatsapp import sendMessage
                sendMessage()
            elif 'close' in command:
                from dictapp import closeappweb
                closeappweb(command)
            elif 'chat' in command:
                from chatbot import chatbot
                chatbot()
            elif 'study' in command:
                from ust import webopener
                webopener()
            elif 'draw' in command:
                from image_generation import draw
                draw()
            #elif 'master' in command:
                
            elif 'bye' in command:
                talk('Bye and have a nice day')
                break
            
    except sr.UnknownValueError:
        pass