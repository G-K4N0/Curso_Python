import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Buenos Dias!")

    elif hour>=12 and hour<18:
        speak("Buenas tardes!")   

    else:
        speak("Buenas noches!")  

    speak("Soy su asistente,Digame que vamos a hacer hoy?")       

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        
        print("Escuchando...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Reconociendo...")    
        query = r.recognize_google(audio, language='es-MX')
        print(f"Usted dijo: {query}\n")

    except Exception as e:    
        print("Repitalo de nuevo por favor...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'abre wikipedia' in query:
            speak('Buscando Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'abre youtube' in query:
            webbrowser.get("chrome").open("youtube.com")

        elif 'abre google' in query:
            webbrowser.open("google.com")

        elif 'Abre stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'reproduce musica' in query:
            music_dir = 'E:\\Musica'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'que hora es' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"La hora es {strTime}")

        elif 'abre code' in query:
            codePath = "C:\\Users\\K4TO\\AppData\\Local\\Programs\\Microsoft VS Code\\bin\\Code.exe"
            os.startfile(codePath)