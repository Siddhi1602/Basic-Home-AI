from PyQt5 import QtWidgets, QtGui,QtCore
from PyQt5.QtGui import QMovie
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
import pyttsx3
import speech_recognition as sr
import os
import time
import smtplib
import webbrowser
import datetime
import speedtest
import requests
import wikipedia
from weather import give_temp
from email_send import sendEmail
from PyQt5.QtCore import QTime


flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)

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

class mainT(QThread):
    def __init__(self):
        super(mainT,self).__init__()
    
    def run(self):
        self.JARVIS()

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
            speak("Please say it again...")  
            return "None"
        return self.query

    def JARVIS(self):
        wishMe()
        while True:
            self.query=self.takeCommand().lower()

            if 'Hi jarvis' in self.query:
                speak("Hello, How are you")

            if 'wikipedia' in self.query:
                speak("Searching Wikipedia...")
                self.query=self.query.replace("wikipedia", "")
                results=wikipedia.summary(self.query, sentences=2)
                speak("According to wikipedia")
                print(results)
                speak(results)
                
            elif 'open youtube' in self.query:
                speak("Opening...")
                webbrowser.open("https://www.youtube.com/")

            elif 'open google' in self.query:
                speak("Opening...")
                webbrowser.open("https://www.google.com/")

            elif 'open stackoverflow' in self.query:
                speak("Opening...")
                webbrowser.open("stackoverflow.com")

            elif 'play music' in self.query:
                self.music_dir='D:\\music'
                self.song=os.listdir(self.music_dir)
                print(self.song)
                os.startfile(os.path.join(self.music_dir, self.song[1]))  
            
            elif 'the time' in self.query:
                self.strTime = datetime.datetime.now().strftime("%H:%M:%S")
                print(f"The time is {self.strTime}")
                speak(f"The time is {self.strTime}")

            elif 'date' in self.query:
                self.strdate = datetime.datetime.now().strftime("%A, %d %B")
                print(f"The Date is {self.strdate}")
                speak(f"The Date is {self.strdate}")

            elif 'internet speed' in self.query:
                st=speedtest.Speedtest()
                dl=st.download()
                correct_dl=int(dl/800000)
                up=st.upload()
                correct_up=int(up/800000)
                print(f"sir you have download speed of {correct_dl} mbps and upload speed of {correct_up} mbps")
                speak(f"sir you have download speed of {correct_dl} mbps and upload speed of {correct_up} mbps")
            

            elif 'temperature' in self.query:
                speak("say the location")
                self.query=self.takeCommand()
                self.query= give_temp(self.query)
                speak(f"Temperature is {self.query}C")
            
            # elif 'email' in self.query:
            #     try:
            #         speak("what should i write?")
            #         content = self.takecommand()
            #         speak("To whom should i send?")
            #         to = self.takecommand().replace(' ','')+'@gmail.com'
            #         sendEmail(to,content)
            #         speak("Email has been sent!")

            #     except Exception as e:
            #         print(e)
            #         speak("Sorry the email was not send")



            elif "close" in self.query:
                print("I m Quitting")
                speak("I m Quitting")
                exit(0)

                



FROM_MAIN,_ = loadUiType(os.path.join(os.path.dirname(__file__),"./gui_page.ui"))
class Main(QMainWindow,FROM_MAIN):
    def __init__(self,parent=None):
        super(Main,self).__init__(parent)
        self.setupUi(self)
        self.label_7 = QLabel
        self.setWindowFlags(flags)
        Dspeak = mainT()

        #jarvis.gif
        self.label_7 = QMovie(":/rec/jarvis", QByteArray(), self)
        self.label_7.setCacheMode(QMovie.CacheAll)
        self.jarvis.setMovie(self.label_7)
        self.label_7.start()

        # full ironman.gif
        self.label_7 = QMovie(":/rec/iron_man.gif", QByteArray(), self)
        self.label_7.setCacheMode(QMovie.CacheAll)
        self.iron_man_gif.setMovie(self.label_7)
        self.label_7.start()

        # face ironman.gif
        self.label_7 = QMovie(":/rec/iron_man_face.gif", QByteArray(), self)
        self.label_7.setCacheMode(QMovie.CacheAll)
        self.iron_man_face.setMovie(self.label_7)
        self.label_7.start()

        Dspeak.start()
        
        today_date = time.strftime("%A, %d %B")  #today's_date
        strTime = datetime.datetime.now().strftime("%H:%M") #current_time
            
        #internet speed
        st=speedtest.Speedtest()  
        dl=st.download()
        correct_dl=int(dl/800000)
        # up=st.upload()
        label_dl= correct_dl.__str__()

        # temperature 
        weather_key ='5c314085f3baa18bdf91b82999484f5b'
        link = 'http://api.openweathermap.org/data/2.5/weather?q=virar&appid='+weather_key
        data = requests.get(link)
        final_data = data.json()
        temp = int(final_data['main']['temp']-273.15)

        #today's_date_setText()
        self.bg.setPixmap(QPixmap(":/rec/black.png"))
        self.date.setText("<font size=8 color='white'>"+today_date+"</font>")
        self.date.setFont(QFont(QFont('Acens',8)))

        #current_time_setText()
        self.time.setText("<font size=8 color='white'>"+strTime+"</font>")
        
        self.internet_speed.setText(f"<font size=8 color='white'>{label_dl} mbps""</font>")

        self.temp_2.setText(f"<font size=8 color='white'>{temp}°C""</font>")


app = QtWidgets.QApplication(sys.argv)
form = Main()
form.show()
sys.exit(app.exec_())