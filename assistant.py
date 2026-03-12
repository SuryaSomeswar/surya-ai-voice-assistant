import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import pywhatkit
import wikipedia 
import pyjokes
import os
import sys
import warnings

warnings.filterwarnings("ignore")

engine = pyttsx3.init()
engine.setProperty('rate', 170)

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def talk(text):
    print("🤖 SURYA:", text)
    engine.say(text)
    engine.runAndWait()


def take_command():
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("🎤 Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=7)

        command = recognizer.recognize_google(audio)
        command = command.lower()
        print("🗣️ You said:", command)

        return command

    except:
        return ""


def run_surya():

    command = take_command()

    if not command:
        return

    if "play" in command:
        song = command.replace("play", "")
        talk("Playing " + song)
        pywhatkit.playonyt(song)

    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        talk("Current time is " + time)

    elif "date" in command:
        date = datetime.datetime.now().strftime("%d %B %Y")
        talk("Today's date is " + date)

    elif "who is" in command:
        person = command.replace("who is", "")
        try:
            info = wikipedia.summary(person, sentences=2)
            talk(info)
        except:
            talk("Sorry, I couldn't find information.")

    elif "joke" in command:
        talk(pyjokes.get_joke())

    elif "open youtube" in command:
        talk("Opening YouTube")
        webbrowser.open("https://youtube.com")

    elif "open google" in command:
        talk("Opening Google")
        webbrowser.open("https://google.com")

    elif "open linkedin" in command:
        talk("Opening LinkedIn")
        webbrowser.open("https://linkedin.com")

    elif "open whatsapp" in command:
        talk("Opening WhatsApp")
        webbrowser.open("https://web.whatsapp.com")

    elif "open instagram" in command:
        talk("Opening Instagram")
        webbrowser.open("https://instagram.com")

    elif "open vscode" in command or "open code" in command:
        talk("Opening Visual Studio Code")
        os.system("code")

    elif "search" in command:
        query = command.replace("search", "")
        talk("Searching for " + query)
        webbrowser.open("https://www.google.com/search?q=" + query)

    elif "exit" in command or "stop" in command:
        talk("Goodbye! Have a great day.")
        engine.stop()
        sys.exit()

    else:
        talk("I didn't understand that command.")


talk("👋 Hello! I am Surya, your AI voice assistant.")

while True:
    run_surya()