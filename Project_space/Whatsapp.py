import pywhatkit
import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
from bs4 import BeautifulSoup
from time import sleep
import os 
from datetime import timedelta
from datetime import datetime

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    try:
        with sr.Microphone() as source:
            print('listening...')
            engine.runAndWait()
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            return command
    except:
        pass

strTime = int(datetime.now().strftime("%H"))
update = int((datetime.now()+timedelta(minutes = 2)).strftime("%M"))

def sendMessage():
    talk("Who do you want to message")
    a = int(input('''Winnie - 1
    ME - 2'''))
    if a == 1:
        talk("Whats the message")
        message = str(input("Enter the message- "))
        pywhatkit.sendwhatmsg("+YOURNUMBER",message,time_hour=strTime,time_min=update)
    elif a==2:
        pass
