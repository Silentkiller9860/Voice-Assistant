import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
from googlesearch import search
import os
import smtplib
import pyaudio
from pygame import mixer #Pygame module contains a Mixer which will load and play a song. 
# import gtts
import random
import pyjokes
import wmi #for telling infoabt pc(Windows Management Instrumentation)
import wolframalpha
import bday
import wolf
import notes
import translator1
from ecapture import ecapture as ec
import background
import ipwifi
import virus


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning! silent killer")

    elif hour>=12 and hour<18:
        speak("Good Afternoon! silent killer")   

    else:
        speak("Good Evening! silent killer ")  

    speak("i'm ready to take command now")       

def takeCommand():


    r = sr.Recognizer()   
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")

    except Exception as e:
        print(e)    
        print("Say that again please...")  
        return "None"
    return query

def searchOnGoogle(query, outputList): 
   speak('The top five search results from Google are listed below.')
   for output in search(query, tld="co.in", num=10, stop=5, pause=2):
    print(output) 
    outputList.append(output) 
    print(outputList) 

def openLink(outputList): 
   speak("Here’s the first link for you.")
   webbrowser.open(outputList[0])


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('cheffoodzone@gmail.com','Chef@1234')
    server.sendmail('cheffoodzone@gmail.com',to,content)
    server.close()

# Starting Our Main Function
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

# wikipedia searching and reading
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

# normal conversions
        elif 'hi' in query or 'hello' in query:
            speak("hello silent killer")

        elif 'goodbye' in query or "stop" in query or 'abort' in query or 'leave' in query:
            speak("good bye..silent killer have a nice day!")
            exit()

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy','i am okey ! How are you']
            ans_q = random.choice(stMsgs)
            speak(ans_q)

        elif "fine" in query or "good" in query:
            print('okay')
            speak('ok')
        
        elif "sad" in query or "not happy" in query:
            print('ohh...sorry')
            speak('ohh..sorry')

        elif 'make you' in query or 'created you' in query or 'develop you' in query:
            ans_m = " Silent Killer made me ! I give Lot of Thannks to Him "
            print(ans_m)
            speak(ans_m)
        
        elif "who are you" in query or "about you" in query or "your details" in query:
            about = "I am Voice Assistance , i have been coded with python"
            print(about)
            speak(about)

        elif "what can you do" in query or "why should i use you" in query or "what are your functions" in query:
            speak("i can tell u time..tell you a joke  may entertain you.")
            speak('I can tell you current weather near you...i can do calculations ..and so many features i have')

        
        elif "your name" in query or "sweat name" in query:
            na_me = "Thanks for Asking my name ...but silent killer didn't give me any name....hahahaha ! "  
            print(na_me)
            speak(na_me)
        
        elif "you feeling" in query or "mood" in query:
            print("feeling Very good after meeting with you")
            speak("feeling Very amazing after meeting with you") 


# opening webpages and searching 

        elif 'search' in query or 'search on google' in query or 'search for me' in query:            
            outputList = []
            speak('What should I search for ?')
            query = takeCommand()            
            searchOnGoogle(query, outputList)
            speak('Should I open up the first link for you ?')
            query = takeCommand()
            if 'yes' in query or 'sure' in query:
              openLink(outputList)
            if 'no' in query:
             speak('Alright.')        

        elif 'open youtube' in query or "open video online" in query:
            webbrowser.open("www.youtube.com")
            speak("opening youtube")
        
        elif 'open github' in query:
            webbrowser.open("https://www.github.com")
            speak("opening github")  
        
        elif 'open facebook' in query:
            webbrowser.open("https://www.facebook.com")
            speak("opening facebook")      
        
        elif 'open instagram' in query:
            webbrowser.open("https://www.instagram.com")
            speak("opening instagram")    
        
        elif 'open google' in query:
            webbrowser.open("https://www.google.com")
            speak("opening google")
            
        elif 'open yahoo' in query:
            webbrowser.open("https://www.yahoo.com")
            speak("opening yahoo")
            
        elif 'open gmail' in query:
            webbrowser.open("https://mail.google.com")
            speak("opening google mail") 
            
        elif 'open snapdeal' in query:
            webbrowser.open("https://www.snapdeal.com") 
            speak("opening snapdeal")  
             
        elif 'open amazon' in query or 'shop online' in query:
            webbrowser.open("https://www.amazon.com")
            speak("opening amazon")
        
        elif 'open flipkart' in query:
            webbrowser.open("https://www.flipkart.com")
            speak("opening flipkart")   
        
        elif 'open ebay' in query:
            webbrowser.open("https://www.ebay.com")
            speak("opening ebay")  

# some functions(music,joke,shutdown,time & clicking image)
        elif 'play music' in query:
            music_dir = 'C:\\Users\\comma\\Desktop\\Jarvis\\Songs'
            songs = os.listdir(music_dir)
            # print(songs)    
            os.startfile(os.path.join(music_dir, songs[15]))
                
                
        elif 'joke' in query or 'laugh me' in query :
            joke1=pyjokes.get_joke(language='en', category= 'all')
            print(joke1)
            speak(joke1)
            speak('wanna listen on more')
            if 'yes' in query:
                joke2=pyjokes.get_joke(language='en', category= 'all')
                print(joke2)
                speak(joke2)
            
            if 'no' in query:
                speak('Alright.')   
        


        elif "shutdown" in query or "off the pc" in query:
            speak("shutting down")
            os.system('shutdown -s') 

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'click me' in query or 'capture' in query or 'take image' in query:
            speak('Capturing Image......')
            ec.capture(0, "Image Captured..", "img.jpg")
            speak('Image Captured and saved in this folder')

# opening desktop application/Changing Background

        elif 'open vs code' in query:
            codePath = "C:\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open microsoft word' in query or 'open word' in query:
            codePath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            os.startfile(codePath)

        elif 'open chrome' in query or 'open browser' in query or 'open google' in query:
            codePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(codePath)   

        elif 'change background' in query:
            speak('which background You want to apply')
            speak('first...')
            speak('second...or')
            speak('third')
            bg = takeCommand()
            # bg = input('which one:=> ')
            if (bg == 'first'):
                background.wallpaper1()
                speak('First wallpaper applied sucessfully..')

            elif (bg == 'second'):
                background.wallpaper2()
                speak('Second wallpaper applied sucessfully..')

            elif (bg == 'third'):
                background.wallpaper3()
                speak('Third wallpaper applied sucessfully..')

            else:
                speak('Sorry..I am not able to get you...or you have choosen another option')


# mailing and info of pc
        elif 'email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "soham.jain.cs@ghrcem.raisoni.net"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry I am not able to send this email")

        elif 'pc' in query or 'laptop' in query or 'features of os' in query:
            
 
            c = wmi.WMI()    
            my_system = c.Win32_ComputerSystem()[0]
            
            print(f"Manufacturer: {my_system.Manufacturer}")
            speak(f"This pc is Manufacturer by: {my_system.Manufacturer}")
            print(f"Model: {my_system. Model}")
            speak(f"The Model is: {my_system. Model}")
            print(f"Name: {my_system.Name}")
            speak(f"With the Name: {my_system.Name}")
            print(f" The Number Of Processors in this pc: {my_system.NumberOfProcessors}")
            speak(f"The Number Of Processors in this pc: {my_system.NumberOfProcessors}")
            print(f"SystemType: {my_system.SystemType}")
            speak(f"The System Type is : {my_system.SystemType}")
            print(f"SystemFamily: {my_system.SystemFamily}")
            speak(f"The Family of the system is: {my_system.SystemFamily}")

# Calculation,Distance,Temprature,Population
        # elif "can you do calculations" in query or 'will you calculate for me'in query:
        #     print("yes..why not i will try my best")
        #     speak('yes..why not I will try my best')
        
        elif 'calculate' in query:
            wolf.wolfcal(query)
                

        elif "where is" in query: 
            query1 = query.replace("where is", "") 
            location = query1
            speak("User asked to Locate") 
            speak(location) 
            webbrowser.open("https://www.google.com/maps/place/" + location + "")

        elif 'can you calculate distance' in query or 'tell me distance' in query:
            print("yes....tell me from where to where i should calculate")
            speak('yes....tell me from where to where i should calculate distance') 
            question = takeCommand()
            wolf.wolfque(question)

        elif 'temperature' in query or 'weather' in query:
            print("yes...Tell me which area you want weather info")
            speak('yes...Tell me which area you want weather informationn') 
            question = takeCommand() 
            wolf.wolfque(question)

        elif 'population' in query or 'peoples' in query:
            print('Which City population you want to know about')
            speak('Which City population you want to know about')
            question = takeCommand()
            wolf.wolfque(question)

        elif 'locate' in query:
            import locator
            speak('which city or country you want to locate')
            city = takeCommand()
            locator.geolocator(city)

# Digital Clock
 
        elif 'show me clock' in query or 'digital clock' in query:
            import dclock

#Writing a note & Translating

        elif 'write note' in query:
            speak('what should i write in notes')
            content = takeCommand()
            notes.writef(content)
            

        elif 'read note' in query:
            speak('Reading Your Notes')
            print('Reading Your Notes')
            speak("opening file")
            print('opening file')
            notes.readf()

        
        elif 'translate' in query:
            speak('What should i translate')
            print('What should i translate')
            text = takeCommand()
            print('In which language you want to translate')
            speak('In which language you want to translate')
            lan = takeCommand()
            translator1.tran(text,lan)

#Getting News
        elif 'news for today' in query or 'tell me news' in query:
            import news1          

#Ip,wifi,fuel
        elif 'ip' in query:
            ipwifi.ip()

        elif 'wi-fi' in query:
            ipwifi.wifi()

        elif 'fuel' in query:
            import fuel


#covid 19

        elif 'covid' in query:
            print('For which country you want to chech the covid info')
            speak('For which country you want to chech the covid info')
            country=takeCommand()
            virus.countries(country)
        
        

# # Finallly Searching Query directly on google
#         else:
#             temp = query.replace(' ','+')
#             g_url="https://www.google.com/search?q="    
#             res = 'sorry! i cannot but i search from internet to give your answer ! is it okay'
#             print(res)
#             speak(res)
#             inp = takeCommand()
#             if (inp=='ok'):
#                 webbrowser.open(g_url+temp)

#             elif (inp=='no'):
#                 speak('okay..then speak again...')
#                 query = takeCommand().lower()
#                 # if __name__ == '__main__':
#                 #     query = takeCommand().lower()
                    
