import smtplib
from pas import pas,g

def sendEmail(to, content):
    gmail = g
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login(gmail, pas)
    server.sendmail(gmail, to, content)
    server.quit()

# main
    if 'email' in query:
        try:
            speak("what should i write?")
            content = takecommand()
            speak("To whom should i send?")
            to = takecommand().replace(' ','')+'@gmail.com'
            sendEmail(to,content)
            speak("Email has been sent!")

        except Exception as e:
            print(e)
            speak("Sorry the email was not send")


