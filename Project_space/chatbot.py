import openai
import pyttsx3
import speech_recognition as sr


openai.api_key = "YOURAPI_KEY"

engine = pyttsx3.init()

r = sr.Recognizer()
mic = sr.Microphone(device_index=1)


conversation = ""
user_name = "You"
bot_name = "Jarvis"

def chatbot():
    engine.say('I am ready to chat')
    while True:
        conversation = ""
        with mic as source:
            print("\nlistening...")
            r.adjust_for_ambient_noise(source, duration=0.2)
            audio = r.listen(source)
        print("no longer listening.\n")

        try:
            user_input = r.recognize_google(audio)
        except:
            continue

        if "terminate" in user_input:
            engine.say("chatbot function has been terminated")
            break
        prompt = user_name + ": " + user_input + "\n" + bot_name+ ": "

        conversation += prompt  # allows for context

        # fetch response from open AI api
        response = openai.Completion.create(engine='text-davinci-003', prompt=conversation, max_tokens=100)
        response_str = response["choices"][0]["text"].replace("\n", "")
        response_str = response_str.split(user_name + ": ", 1)[0].split(bot_name + ": ", 1)[0]

        conversation += response_str + "\n"
        print(response_str)

        engine.say(response_str)
        engine.runAndWait()