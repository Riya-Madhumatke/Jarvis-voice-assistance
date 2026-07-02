import speech_recognition as sr

import webbrowser
import pyttsx3
import musicLibrary
import requests
#pip install pockectsphinx

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "  "

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
   if "open google" in c.lower():
      webbrowser.open("https://google.com")
   elif "open facebook" in c.lower():
      webbrowser.open("https://facebook.com")
   elif "open youtube" in c.lower():
      webbrowser.open("https://youtube.com")
   elif "open linkedin" in c.lower():
      webbrowser.open("https://linkedin.com")
   elif c.lower().startswith("play"):
      song = c.lower().split("")[1]
      link = musicLibrary.music[song]  
      webbrowser.open(link) 

   elif "new" in c.lower():
        r = requests.get("")

if __name__=="__main__":
    speak("Initializing Jarvis....")
    while True:
#     #listen for the wake word "jarvis"
    
     r = sr.Recognizer()

     print("recognizing...")

   #recognize sppech using sphinx
   
try:

     with sr.Microphone() as source:

       print("Listening..")
       audio = r.listen(source, timeout=2,phrase_time_limit=1) 

       word = r.recognize_google(audio)
       if(word.lower()=="jarvis"):
          speak("yaa")
          with sr.Microphone() as source:

           print("Jarvis Active..")
           audio = r.listen(source) 
           command = r.recognize_google(audio)

           processCommand(command)
          #listen for a command
    #   print("Sphinx thinks you said" +r.recognize_sphinx(audio))
# except sr.UnknownValueError:
#       print("sphix cold not understand audio"

    # print("Sphinx thinks you said" +r.recognize_sphinx(audio))
except Exception as e:
    print("Error; {0}".format(e))
