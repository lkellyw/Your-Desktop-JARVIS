import os
import pyautogui
import webbrowser
import pyttsx3
import speech_recognition as sr
from time import sleep

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

dictapp = {"commandprompt":"cmd", 
            "paint": "paint",
            "word":"winword", 
            "excel": "excel",
            "chrome":"chrome", 
            "vscode":"vscode", 
            "powerpoint":"powerpnt",
            "gpt":"chatgpt",}

def openappweb(command):
    talk('Launching')
    command = command.replace("open","")
    command = command.replace("jarvis","")
    command = command.replace("launch","")
    command = command.replace(" ","")
    if '.com' in command or '.co.in' in command or '.org' in command:
        webbrowser.open(f"https://www.{command}")
    else:
        pyautogui.press("super")
        pyautogui.typewrite(command)
        pyautogui.sleep(2)
        pyautogui.press("enter")

        """
        keys = list(dictapp.keys())
        for app in keys:
            if app in command:
                os.system(f"start {dictapp[app]}")
        """

def closeappweb(command):
    talk('Closing')
    if "one tab" in command or "1 tab" in command:
        pyautogui.hotkey("ctrl","w")
    elif "2 tab" in command or "2 tab" in command:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w") 
        talk("All tabs closed")
    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in command:
                os.system(f"taskkill /f /im {dictapp[app]}.exe")

    