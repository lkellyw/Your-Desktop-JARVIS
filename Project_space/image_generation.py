#paid service
import openai
import speech_recognition as sr
from PIL import Image
import pyttsx3

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

# Set the API key
openai.api_key = "YOURAPI_KEY"

# Set the model to use the DALL-E 2 API
model = "image-alpha-001"

# Set the response format to be an image
response_format = "url"

# Initialize the speech recognition object
r = sr.Recognizer()


def draw():
    # Start listening for speech
    talk("Say something to generate an image")
    with sr.Microphone() as source:
        audio = r.listen(source)

    # Transcribe the speech to text
    try:
        prompt = r.recognize_google(audio)
        print(f"You said: {prompt}")
    except sr.UnknownValueError:
        print("Sorry, I could not understand what you said")

    # Generate the image
    response = openai.Image.create(
        prompt=prompt,
        model=model,
        response_format=response_format
    )

    # Open the image using PIL
    image = Image.open(response.content)

    # Display the image in a window
    image.show()
