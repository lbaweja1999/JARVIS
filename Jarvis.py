import ctypes
import pyttsx3
import speech_recognition as sr
import datetime
import winsound
import wikipedia
import webbrowser                     #MODULES
import os
import smtplib
import calendar
import math
import numpy as np




engine = pyttsx3.init('sapi5')            #speech api
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  #setting up voice

rate = engine.getProperty('rate')
vol = engine.getProperty('volume')
newVoiceRate = 145
newvol = 2
engine.setProperty('volume', newvol)
engine.setProperty('rate', newVoiceRate)


def speak(audio):  #speaks audio
    engine.say(audio)
    engine.runAndWait()


def wishMe():      #wishes you according to the time and introduces himself
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning,Lakshay!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon,Lakshay!")
    else:
        speak("Good Evening,Lakshay!")
    speak("Hello, My name is Jarvis!How may I help you?")

def myCommand(): #takes voice input and returns string
    r = sr.Recognizer()
    with sr.Microphone() as source:
        winsound.Beep(frequency = 2500, duration = 100) #beep to inform that it's listening
        print("Listening....")
        r.pause_threshold = 0.5
        audio = r.listen(source)
    
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")
        
    except Exception as e:
        #print(e)
        speak('Sorry! I couldnt hear it,Can you please repeat?')
        print("Pardon Please!")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()                                                   #send mail function
    server.login('lbaweja4@gmail.com', '99711728690')
    server.sendmail('aa', to, content)
    server.close()



if __name__ == "__main__":
    
    query = myCommand().lower()
    
    if 'hey jarvis' in query or 'hi jarvis' in query:

      wishMe()
      while True:
    # if 1:
        query = myCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Ok Sir!Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=4)        #wikipedia
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif 'youtube' in query:
            speak('Ok Sir! opening youtube')
            webbrowser.open("https://www.youtube.com/")         #youtube
        
        elif 'google' in query:
            speak('Ok Sir! opening google')
            webbrowser.open("https://www.google.com")   #google
        
        elif 'gmail' in query:
            speak('Ok Sir! opening gmail')
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox") #gmail

        elif 'erp' in query:
            speak('Ok Sir! opening  ncu erp')
            webbrowser.open("https://erp.ncuindia.edu/Welcome_iie.aspx")  #erp
        
        elif 'lms' in query:
            speak('Ok Sir! opening ncu lms')
            webbrowser.open("http://lmsncu.ncuindia.edu/login/index.php") #lms
        
        elif 'otms' in query:
            speak('Ok Sir! opening otms ncu')
            webbrowser.open("http://otms.local.ncuindia.edu/")  #otms
          
        elif 'github' in query:
            speak('Ok Sir! opening github')
            webbrowser.open("https://github.com/")  #github
        
        elif 'S P A' in query or 's p a' in query or 'spa' in query:
            speak('Ok sir! opening S P A ncu')
            webbrowser.open("http://www.spa.ncuindia.edu/user/login")  #spa ncu


        elif 'webopac' in query:          
            speak('Ok Sir! opening webopac ncu')                          
            webbrowser.open("http://opac.ncuindia.edu:8380/opac/")      #webopac
        
        elif 'whatsapp' in query:
            speak('Ok Sir! opening whatsapp')
            webbrowser.open("https://web.whatsapp.com/")      #whatsapp
        
        elif 'news' in query:
            speak('Ok Sir! opening the best news channel for you')
            webbrowser.open("https://aajtak.intoday.in/")   #news

        elif 'netflix' in query:
            speak('Ok Sir! opening netflix')
            webbrowser.open("https://www.netflix.com/in/")  #netflix

        elif 'stackoverflow' in query:
            speak('Ok sir!opening stackoverflow')
        
        elif 'name' in query:
            speak('Hello!My name is Jarvis.')               #name
        
        elif 'greet' in query or 'wish' in query:
            hour = int(datetime.datetime.now().hour)       #wishes you
            if hour>=0 and hour<12:
                 speak("Good Morning,Lakshay Sir!")
            elif hour>=12 and hour<18:
                 speak("Good Afternoon,Lakshay Sir!")
            else:
                 speak("Good Evening,Lakshay Sir!")


        elif 'date' in query or 'time' in query:
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")   #date and time
            speak(f"Lakshay, the date and time is {str(now)} ")
            print("Lakshay,the date and time is:\n",str(now))

        elif 'calendar' in query:
            speak('Ok Sir! opening the calendar in terminal')
            cal_display = calendar.TextCalendar(calendar.MONDAY)
            # Year: 2019
            # Column width: 1
            # Lines per week: 1 
            # Number of spaces between month columns: 0
            # No. of months per column: 2
            print(cal_display.formatyear(2019, 1, 1, 0, 2))

        elif 'who are you' in query or 'introduce' in query:            #introduction
            speak('Hi! My name is Jarvice!I am your voice assistant!I was developed by Mr.Lakshay!I can open various famous websites and your computer applications!I can also tell you the date and time!I can also tell you the information of wikipedia!I can open the calendar for you!I can also send emails to anyone!I can also do some basic calculations !')
        
        elif 'android studio' in query:
            speak('Ok Sir! opening android studio in few minutes')                                   #android studio
            os.startfile("C:\\Program Files\\Android\\Android Studio\\bin\\studio64.exe")
        
        elif 'eclipse' in query:
            speak('Ok Sir! opening eclipse')       #eclipse
            os.startfile("C:\\Users\\Lakshay\\Downloads\\eclipse-java-luna-SR2-win32-x86_64\\eclipse\\eclipse.exe")
         
        elif 'vscode' in query:   #vscode
            speak('Ok Sir! opening vscode')
            os.startfile("C:\\Program Files\\Microsoft VS Code\\Code.exe")
         
       
        elif 'male' in query or 'female' in query:
            speak('I am male.')                                           #gender

        elif 'send email' in query:
            try:
                speak("Whom do you want to send email?")                                #send mail
                to = myCommand()
                speak("What should I say?")
                content = myCommand()
                sendEmail(to, content)
                speak("Email has been sent!")
                print("Email sent successfully!!")
            except Exception as e:
                print(e)
                speak("Sorry my friend Lakshay. I am not able to send this email")  
                print("Sorry,Cant send this mail.")
        
        elif 'calculator' in query or 'calci' in query:
            speak("Enter the following")                           #calculator
            ans=input("Do you want to do 1 single operation(+,-,*,/) or many operations (single/many) ")
            if(ans=="single"):
              n1=eval(input("enter number 1 "))
              n2=eval(input("Enter number 2 "))
              exp=input("Enter expression add(+),sub(-),mul(*),div(/) ")
              res=str(n1)+exp+str(n2)
              print("The answer is ",eval(res))
            elif(ans=="many"):
              expression=input("Enter whole expression ")
              print("your answer is",eval(expression))
      

        elif 'power' in query or 'raise' in query:
            speak('Enter the two numbers')              #x raise to y
            x=float(input("Enter the number\n"))
            y=float(input("Enter the power\n"))
            print('The multiplication of the above two numbers is:',pow(x, y))        
    
        
        elif 'table' in query:
            speak('Enter the number')
            num = int(input("Enter the number \n"))
            print("Multiplication Table of", num)       #multiplication table
            for i in range(1, 11):
                print(num,"X",i,"=",num * i)
        
        elif 'factorial' in query:
            speak('Enter the number')
            num = int(input("Enter the number\n"))        #factorial
            print('Factorial of',num,'is',math.factorial(num)) 

        elif 'anaconda' in query:
            speak("Opening anaconda navigator in few minutes")
            os.startfile("D:\\Anaconda3\\pythonw.exe D:\\Anaconda3\cwp.py D:\\Anaconda3 D:\\Anaconda3\\pythonw.exe D:\\Anaconda3\\Scripts\\anaconda-navigator-script.py")

        elif 'gcd' in query or 'greatest common divisor' in query: 
            speak('Enter the two numbers')           #gcd
            x=int(input("Enter first number\n"))
            y=int(input("Enter second number\n"))
            print('Greatest Common divisor of',x,'and',y,'is',math.gcd(x, y))
        
        elif 'square root' in query:
            speak('Enter the number')                   #square root
            x=float(input('Enter number\n'))
            print("Square root of",x,"is",np.sqrt(x))
        elif 'lock' in query:
            speak('Ok Sir! your pc is being locked')       #lock the pc
            for value in ['pc', 'system', 'windows']:
                ctypes.windll.user32.LockWorkStation()
        
        elif 'music' in query:
            speak("Ok sir!Opening your music folder")     #mymusic
            os.startfile("D:\\downloads\\Mymusic")

        elif 'movies' in query:
            speak('Ok sir!Opening your movies folder')        #mymovies
            os.startfile("D:\\downloads\\MyMovies")
           
        
        
        elif 'quit' in query or 'bye' in query: #terminate the loop
            speak("Bye Lakshay, Have a good day.")
            exit()
        
        elif 'thank you' in query:
            speak("Your welcome sir")
            exit()
        
       

