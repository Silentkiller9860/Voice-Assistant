import wolframalpha  
from win32com.client import Dispatch  # provides access to many of the Windows APIs from Python.

def speak(s):
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(s)

def wolfque(question):
    app_id = 'GHQH9J-QG49AXKKE5'
    client = wolframalpha.Client(app_id) 
    res = client.query(question) 
    answer = next(res.results).text 
    print(answer)
    speak(answer)



def wolfcal(query):
    app_id = "GHQH9J-QG49AXKKE5" 
    client = wolframalpha.Client(app_id) 
    indx = query.lower().split().index('calculate')  
    query = query.split()[indx + 1:]  
    res = client.query(' '.join(query))  
    answer = next(res.results).text 
    print("According to my search the answer is " + answer)  
    speak("According to my search the answer is " + answer)
    



# question = input('Question: ') 
# wolfque(question)

# while True:  
#     question = input('Question: ') 
#     wolfque(question) 
     
#     if(question ==''):
#         print('ok ...bye')
#         break
