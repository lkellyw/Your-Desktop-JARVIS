import ctypes
import pyautogui
import pywinauto
import pyttsx3
import speech_recognition as sr
import subprocess
import pyperclip

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

# Find the window handle of the application
subprocess.Popen("chatgpt")
hwnd = ctypes.windll.user32.FindWindowW(None, "chatgpt")
# Maximize the window
ctypes.windll.user32.ShowWindow(hwnd, 3)


while True:
    try:
        with sr.Microphone() as source:
            print('listening...')
            engine.runAndWait()
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'bye' in command:
                break
            # Move the mouse to the desired position
            pyautogui.moveTo(800, 950)
            # Simulate a left mouse click
            pyautogui.click()
            pyautogui.typewrite(command)
            pyautogui.press('enter')
            # Move the mouse cursor to the specific position
            pyautogui.moveTo(800, 800)

    except sr.UnknownValueError:
        pass
