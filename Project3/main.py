import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibary
import requests
from openai import OpenAI

recognition = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "Enter API Key"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def aiProcess(command):
    client  = OpenAI(api_key = "Enter api key"),

    response = client.responses.create(
    model="gpt-5",
    input=[
        {
            "role": "user",
            "content": [
                {
                    "type": "input_text",
                    "text": "What teams are playing in this image?",
                },
                {
                    "type": "input_image",
                    "image_url": "https://api.nga.gov/iiif/a2e6da57-3cd1-4235-b20e-95dcaefed6c8/full/!800,800/0/default.jpg"
                }
            ]
        }
    ]
)

    return(response.output_text)

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com/")
    elif "open facebook" in c.lower():
        webbrowser.open("https://www.facebook.com/")
    elif "open youtube" in c. lower():
        webbrowser.open("https://www.youtube.com/")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get("Enter API Link") # News API
        if r.status_code == 200:

            # prase the JSON response
            data = r.json()

            # Extract the articals
            articles = data.get('articles', [])

            # Print the headlines
            for article in articles:
                print(article['title'])

    else:
        # Let OpenAPI handle the request
        output = aiProcess(c)
        speak(output)

if __name__ == "__main__":
    speak("Initializing Jarvis....")

    while True:
     # Listen for th wake word "Jarvis"
       r = sr.Recognizer()

       print("recognizing....")

       try:
           with sr.Microphone() as source:
              print("Listening....")
              audio = r.listen(source, timeout=2, phrase_time_limit=1)
        
           word = r.recognize_google(audio)
           if (word.lower() == "jarvis"):
              speak("Ya")
           # Listen for command
           with sr.Microphone() as source:
              print("Jarvis Active....")
              audio = r.listen(source)
              command = r.recognize_google(audio)

              processCommand(command)

       except Exception as e:
          print("Error: {0}".format(e))