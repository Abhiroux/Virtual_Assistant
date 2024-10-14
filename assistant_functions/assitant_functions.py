import pywhatkit  # play youtube video
import random  #
import webbrowser
from AppOpener import open, close
import pyjokes
import datetime
import os  # FOR Accessing System files
import pyttsx3  # text to speech lib
import wikipedia
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


def Leave():
    response = "Bye! Have a great day"
    print(f"Assistant: {response}")
    speak(response)
    quit()


def Open_exe(text):
    if 'open' in text:
        text = text.replace('open', '')
        print(f"Assistant: opening {text}")
        if open(f"{text}") == True:
            speak(f"opening {text}")
        else:
            webbrowser.open(f"{text}")


def Close_exe(text):
    if 'close' in text:
        text = text.replace('close', '')
        print(f"Assistant: closing {text}")
        speak(f"closing {text}")
        close(f"{text}")


def AssistantIntro():
    print(f"Assistant: I am your personal assistant, Shirley. please tell me how can I help you.")
    speak("I am your personal assistant, Shirley. please tell me how can I help you.")


def get_Greetings():
    response = "Hello! How can I assist you?"
    print(f"Assistant: {response}")
    speak(response)


def YoutubePlayer(text):
    text = text.replace("play", "")
    text = text.replace("on", "")
    text = text.replace("youtube", "")
    speak(f"playing {text}")
    pywhatkit.playonyt(text)


def openSpotify():
    print(f"Assistant: Opening Spotify")
    open("spotify")


def well_being(text):
    if 'how are you' in text:
        print(f"Assistant: I am fine. you are very kind to ask, especially in these tempestuous times")
        speak("I am fine. you are very kind to ask, especially in these tempestuous times")
    elif 'fine' in text:
        print(f"I'm glad to hear it.")
        speak("I'm glad to hear it.")
    elif 'thank you' in text:
        print(f"Assistant: You are welcome!")
        speak(f"you are welcome!")


def send_email():
    print("Assitant: Okay! Opening Email")
    speak("Okay! Opening Email")
    webbrowser.open("https://mail.google.com/mail/u/0/#inbox?compose=new")


def play_song():
    music_dr = 'F:\My Music World\Audios'
    songs = os.listdir(music_dr)
    player = random.choice(songs)
    print(f"Assistant: Playing {player}")
    speak("Playing")
    os.startfile(os.path.join(music_dr, player))


def getTime():
    timenow = datetime.datetime.now().strftime("%H:%M:%S")
    # print(f"sir the time is {timenow}")
    speak(f"sir the time is {timenow}")
    return f"sir the time is {timenow}"


def date():
    now = datetime.datetime.now()
    my_date = datetime.datetime.today()

    month_name = now.month
    day_name = now.day
    month_names = ['January', 'February', 'March', 'April', 'May', 'June',
                   'July', 'August', 'September', 'October', 'November', 'December']
    ordinalnames = ['1st', '2nd', '3rd', ' 4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th', '13th', '14th', '15th',
                    '16th', '17th', '18th', '19th', '20th', '21st', '22nd', '23rd', '24rd', '25th', '26th', '27th', '28th', '29th', '30th', '31st']

    print("Today is " + month_names[month_name-1] +
          " " + ordinalnames[day_name-1] + '.')
    speak("Today is " + month_names[month_name-1] +
          " " + ordinalnames[day_name-1] + '.')


def jokes():
    joke = pyjokes.get_joke()
    print(f"Assistant: {joke}")
    speak(joke)


def getWikipedia(text):
    speak("Searching.")
    text = text.replace("wikipedia", "")
    text = text.replace("search", "")
    text = text.replace("on", "")
    result = wikipedia.summary(text, sentences=3)
    if result == True:
        print(f"Assistant: {result}")
        speak(result)
    else:
        print("Assistant: Result not found")
        speak("Result not found")
