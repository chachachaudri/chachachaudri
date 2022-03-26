from platform import java_ver
from subprocess import REALTIME_PRIORITY_CLASS
import pyttsx3
import requests
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pywhatkit
import wolframalpha
from pyfirmata import Arduino,util
from pyfirmata import OUTPUT
import os
from requests import *
from bs4 import BeautifulSoup

board = Arduino('com5')
board.digital[11].mode = OUTPUT
board.digital[12].mode = OUTPUT
board.digital[13].mode = OUTPUT

board.digital[11].write(1)
board.digital[12].write(1)
board.digital[13].write(1)


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

    

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("good morning sir")

    elif hour >=12 and hour <18:
        speak("good afternoon sir")

    else:
        speak("good evening sir")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') 
        print(f"User said: {query}\n")  

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None" 
    return query  

if __name__ == "__main__":

    wishme()
    speak(' i am your assistant jarvis, how can i help you ')
    while True:
        query = takecommand().lower()


        if'how are you'in query:
            speak("i am fine sir how about you?")

        elif"fine"in query:
            speak('oh, good sir ')

        
        elif 'wikipedia'in query:
            speak('searching wiki sir...')
            query = query.replace('wikipedia','')
            results = wikipedia.summary(query,sentences = 2)
            speak('according to wiki')
            speak(results)
            print(results)

        elif 'open youtube' in query:
            webbrowser.open('https://youtube.com/')

        elif 'search google' in query:
            speak('sir what should i search on google sir')
            cm = takecommand().lower()
            webbrowser.open(f'{cm}')

        elif 'play' in query:
            song = query.replace('play','')
            speak('playing'+ song)
            pywhatkit.playonyt(song)

        elif('open whatsapp')in query:
            speak("opening whatsapp sir....")
            webbrowser.open('https://web.whatsapp.com/')
            

        elif'send message' in query:
            speak('what should i send sir')
            pywhatkit.sendwhatmsg('+919418694877',takecommand(),int(input()),int(input()))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            print(f"Sir, the time is {strTime}") 

        elif'work'in query:
            pdf_Dir = "C:\\Users\\aryav\\OneDrive\Desktop\\all items\\python\\pdf"              
            pdf = os.listdir(pdf_Dir)
            print(pdf)
            os.startfile(os.path.join(pdf_Dir,pdf[0]))
        
        elif"thank you"  in query:
            speak("your welcome sir")

        elif"remember" in query:
            remembeMSG = query.replace("remember jarvis","")
            speak("you told me to remind you that:"+remembeMSG)
            remeber = open('rmb.txt','w')
            remeber.write(remembeMSG)
            remeber.close()

        elif'remind'in query:
            hour = int(datetime.datetime.now().hour)
            
        elif"IP" in query:
            speak ("let me check sir")
            try:
                ip = requests.get("https://api.ipify.org").text
                speak("sir you current IP is"+ip)
                print("sir you current IP is"+ip)


            except:
                pass
            

        elif 'keep quiet'  in query:
            speak('ok sir,,,, Iam going to rest please call me when you need')
            break
        
        elif 'shutdown system'in query:
            os.system('shutdown/1/i')

        elif "search" in query:
            meaning = takecommand().lower()
            ur = f"https://www.google.com/search?q={meaning}"
            t = requests.get(ur)
            data = BeautifulSoup(t.text,"html.parser")
            tem = data.find("div",class_="BNeawe").text
            speak(f" {meaning} is {tem}")
            print(f" {meaning} is {tem}")

        elif "current location" in query:
            ip = requests.get("https://api.ipify.org").text
            sea = "search this" + ip
            utr = f"https://www.google.com/search?q={ip}"
            ty = requests.get(utr)
            dat = BeautifulSoup(ty.text,"html.parser")
            te = dat.find("div",class_="BNeawe").text
            speak(f" {sea} is {te}")
            print(f" {sea} is {te}")

        
        elif'turn off light' in query:
            speak('turning off the lights')
            board.digital[11].write(0)

        elif'turn on light' in query:
            speak('turning on the lights')
            board.digital[11].write(1)

        elif'turn on my light' in query:
            speak('turning off lights')
            board.digital[12].write(0)

        elif'turn off my light' in query:
            speak('turning on lights')
            board.digital[12].write(1)

        
     

        