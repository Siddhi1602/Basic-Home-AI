import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
from guii import Ui_Form
    
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print('Good Morning')
        speak("Good Morning")

    elif hour>=12 and hour<18:
        print('Good Afternoon')
        speak("Good Afternoon")

    else:
        print('Good Evening')
        speak("Good Evening")
    
    
    speak("I am jarvis. How may I help you")

class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.TaskExecution

    def takeCommand(self):
        r=sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            r.pause_threshold=1
            audio=r.listen(source)

        try:
            print("Recognizing...")
            self.query=r.recognize_google(audio, language="en-in")
            print(f"User said:  {self.query}\n")

        except Exception:
            print("Please say it again...")  
            return "None"
        return self.query

    def TaskExecution(self):
        wishMe()
        while True:
            self.query=self.takeCommand().lower()

            if 'wikipedia' in self.query:
                speak("Searching Wikipedia...")
                self.query=self.query.replace("wikipedia", "")
                results=wikipedia.summary(self.query, sentences=2)
                speak("According to wikipedia")
                print(results)
                speak(results)
                
            elif 'open youtube' in self.query:
                speak("Opening...")
                webbrowser.open("youtube.com")

            elif 'open google' in self.query:
                speak("Opening...")
                webbrowser.open("https://www.google.com/")

            elif 'open stackoverflow' in self.query:
                speak("Opening...")
                webbrowser.open("stackoverflow.com")

            elif 'play music' in self.query:
                music_dir='D:\\music'
                song=os.listdir(music_dir)
                print(song)
                os.startfile(os.path.join(music_dir, song[1]))  
            
            elif 'the time' in self.query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                print(f"The time is {strTime}")
                speak(f"The time is {strTime}")

            elif 'date' in self.query:
                strdate = datetime.datetime.now().strftime("%h:%m:%S")
                print(f"The Date is {strdate}")
                speak(f"The Date is {strdate}")
            

            elif "close" in self.query:
                print("I m Quitting")
                speak("I m Quitting")
                exit(0)


 

