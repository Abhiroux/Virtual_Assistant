import pyowm
import pyttsx3
import os
# sapi5 is a microsoft speech API for voice recognition
engine = pyttsx3.init('sapi5')
# Assiging voices that available in device
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    '''defining speak() function that will speak\say the given text/string '''
    engine.say(audio)
    engine.runAndWait()
    pass


token = os.environ['APIKEY']  # Your token goes here
own = pyowm.OWM(token).weather_manager()


def get_weather():
    zip_code = "140301"  # Update this to your zip code
    weather = own.weather_at_zip_code(zip_code, 'IN').weather
    temperature = int(round(weather.temperature(unit='celsius')['temp'], 0))
    print(f"Currently, the temperature is {temperature} degrees")
    speak(f"Currently, the temperature is {temperature} degrees")
