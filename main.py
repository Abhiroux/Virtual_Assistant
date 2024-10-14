from tkinter import *
import threading
from PIL import Image
import customtkinter
import speech_recognition as sr
from assistant_functions.assitant_functions import *
from assistant_functions.weather import get_weather
import pyttsx3
import datetime
from intent_classification.intent_classification import IntentClassifier

intent_classifier = IntentClassifier()

# sapi5 is a microsoft speech API for voice recognition
engine = pyttsx3.init('sapi5')
# Assiging voices that available in device
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)  # Voice setting


def speak(audio):
    '''defining speak() function that will speak\say the given text/string '''
    engine.say(audio)
    engine.runAndWait()
    pass


def takeCommand():
    ''' it takes voice input form the user and returns that input as a stirng'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f": {query}\n")
    except Exception as e:
        print(e)
        print("say that again please...")
        return "none"
    return query


class Assistant:
    def __init__(self, name):
        self.name = name

    def reply(self, text):
        intent = intent_classifier.predict(text)
        replies = {
            'weather': get_weather,
            'greeting': get_Greetings,
            'leaving': Leave,
            'app_open': Open_exe(text),
            'assist_intro': AssistantIntro,
            'open spotify': openSpotify,
            'well_being': well_being(text),
            'play_music': play_song,
            'app_close': Close_exe(text),
            'tell_time': getTime,
            'joke': jokes,
            'mailling': send_email,
            'reply_date': date
        }
        reply_func = replies[intent]
        if callable(reply_func):
            try:
                return reply_func()
            except Exception as e:
                print(f"Error: {e}")

    def wishMe(self):
        '''defining wishMe() for Assistant to greet according to time'''
        hour = int(datetime.datetime.now().hour)
        if hour >= 3 and hour < 12:
            speak("Good Morning!")
        elif hour >= 12 and hour < 18:
            speak("Good Afternoon!")
        else:
            speak("Good Evening!")

    def main(self):
        self.wishMe()
        speak("please select voice or text command")
        choice = input("please select voice or text command: ")
        choice.lower()
        if (choice == 'voice'):
            while True:
                said = takeCommand()
                self.reply(said)
        elif (choice == 'text'):
            while True:
                query = input("you: ").lower()
                self.reply(query)


assistant = Assistant("Shirley")
assistant.main()
