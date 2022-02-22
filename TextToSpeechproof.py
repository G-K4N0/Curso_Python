import pyttsx3
import datetime
import os
import smtplib

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def hablar(audio):
    engine.say(audio)
    engine.runAndWait()


def saludo():
    hora = int(datetime.datetime.now().hour)

    strTime = datetime.datetime.now().strftime("%H:%M:%S")

    if hora >=0 and hora <12:
        hablar(f"Buenos Dias, son las {strTime}")
    
    elif hora>=12 and hora <18:
        hablar(f"Buenas tardes!, son las {strTime}")
    else:
        hablar(f"Buenas noches!, son las {strTime}")

if __name__== "__main__":
    saludo()