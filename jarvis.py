import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    print(f"JARVIS: {text}")
    engine.say(text)
    engine.runAndWait()

def greet_user():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good morning!")
    elif hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am Jarvis. How can I help you?")

def listen_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio, language='en-in')
        print(f"You said: {command}")
    except Exception as e:
        speak("Sorry, I didn't catch that. Could you say it again?")
        return ""
    return command.lower()

def run_jarvis():
    greet_user()
    while True:
        command = listen_command()

        if "wikipedia" in command:
            speak("Searching Wikipedia...")
            topic = command.replace("wikipedia", "")
            result = wikipedia.summary(topic, sentences=2)
            speak(result)

        elif "open youtube" in command:
            speak("Opening YouTube")
            webbrowser.open("https://youtube.com")

        elif "open google" in command:
            speak("Opening Google")
            webbrowser.open("https://google.com")

        elif "open vs code" in command:
            path = "C:\\Users\\DELL\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)

        elif "open notepad" in command:
            os.system("notepad")

        elif "play music" in command:
            music_folder = "C:\\Users\\DELL\\Music"
            songs = os.listdir(music_folder)
            if songs:
                song_path = os.path.join(music_folder, random.choice(songs))
                os.startfile(song_path)
            else:
                speak("No music files found.")

        elif "time" in command:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {time}")

        elif "date" in command:
            today = datetime.date.today().strftime("%B %d, %Y")
            speak(f"Today is {today}")

        elif "exit" in command or "quit" in command or "stop" in command:
            speak("Goodbye!")
            break

        elif command != "":
            speak("Sorry, I didn't understand that command.")

# Run the assistant
run_jarvis()
