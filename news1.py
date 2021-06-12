import requests
import json
import time
from win32com.client import Dispatch

def speak(s):
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(s)

data = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=d093053d72bc40248998159804e0e67d")

result = data.json()
print(result['status'])
# print(result)

news = result['articles']

speak("welcome Silent killer")
speak("Here are the top ten news of our country India")
speak("So our first news is ")
for i  in range(0,4):
    print(i)
    print(news[i]['description'])
    print('To Read full News Follow this link Given Below')
    print(news[i]['url'])
    speak(news[i]['description'])
    if i>=3:
        break
    time.sleep(2)
    if i == 3:
        speak("So our last news for today is ")
    else:
        speak("Moving To Our next news")


speak("Thanks for listening ! Have a nice day")