import speech_recognition as sr
import webbrowser   # open something from brouser through voice command
import pyttsx3  # text to speech
# pip install pocketsphinx
import musicLibrary
import requests
# 1. ek recognizer object bnayenge, taki hm jab bolenge to wo recoginze karega.

recoginzer = sr.Recognizer() # Recognizer ek class hai
engine = pyttsx3.init()
newsapi = "74f23151ba9f46f5ae815447608011f4"

# make a speak function which takes a text and do speak
def speak(text): 
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://intagram.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open whatsapp" in c.lower():
        webbrowser.open("https://whatsapp.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)   
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()

            # Extract the articles
            articles = data.get('articles',[])

            # Print the headlines 
            for article in articles:
                speak(article['title']) 
    else:
        # let OpenAI handle the request
        pass

if __name__=="__main__":
    speak("Initializing jarvis....")
    # Listen for the awake word "Jarvis"
    while True:
        # listen for the wake word "Jarvis"
        # obtain audio from microphone
        r = sr.Recognizer()

        print("recognizing....")
        try:
            with sr.Microphone() as source:
                print("listening....")
                audio = r.listen(source,timeout=2,phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower()=="jarvis"):
                speak("Ya")
                # listen for command 
                with sr.Microphone() as source:
                    print("jarvis active....")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    processCommand(command)
        except Exception as e:
            print("Error; {0}".format(e))