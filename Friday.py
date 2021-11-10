#Project Friday

import speech_recognition as sr 
import datetime
import wikipedia
import pyttsx3
import webbrowser
import random
import os
import pyjokes

from requests import get

# Text-to-Speech Conversion
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

#print(voices)

engine.setProperty('voice',voices[0].id)

# Function: Speaks the text and waits
def speak(audio):
    (pyttsx3.init('sapi5')).say(audio)
    (pyttsx3.init('sapi5')).runAndWait()

# Function: Wishes the owner based on the time
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("good morning sir, i am virtual assistant, friday")
    elif hour >= 12 and hour < 18:
        speak("good afternoon sir, i am virtual assistant, friday") 
    else:
        speak("good evening sir, i am virtual assistant, friday")

# Function: Takes the command and recognizes the command using the speech_recognition module
def takeCommand(): 
    r = sr.Recognizer()
    
    # Use Microphone module from the speech_recognition module
    with sr.Microphone() as source:

        print('Listening...')
     
        # Seconds of non-speaking audio before a phrase is considered complete
        r.pause_threshold = 0.7

        audio = r.listen(source)
        
        # Handle Exceptions
        try:
            print("Recognizing")
            
            # Using Google Speech-To-Text Engine
            Query = r.recognize_google(audio, language='en-in')

            print("the command is printed=", Query)
        except Exception as e:
            print(e)
            print("Say that again sir")
            
            return "None"
        
        return Query
    
    with sr.Microphone() as source:
        print("Listning....")
        
        audio = r.listen(source)

    try:
        print("Recognizing...") 

        text = r.recognize_google(audio,language='en-in')

        print(text)
    
    # Handle Exceptions
    except Exception:


        speak("Error!")

        print("Network connection error") 
        
        return "none"

    return text

# Main Function
if __name__ == "__main__":
    wish()

    while True:
        query = takeCommand().lower()

        if "wikipedia" in query:
            speak("Fetching data...")
            speak("Please Wait...")

            query.replace("wikipedia","")

            results = wikipedia.summary(query, sentences=2)
            
            print(results)
            speak(results)

        elif 'open notepad' in query :
            npath = "C:\\Windows\\system32\\nptepad.exe"
            os.startfile(npath)

        elif 'open blender' in query :
            npath = "C:\\Program Files\\Blender Foundation\\Blender 2.93\\blender.exe"
            os.startfile(npath)

        elif 'open pycharm' in query :
            npath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.2.2\\bin\\pycharm.exe"
            os.startfile(npath)

        elif 'open quick heal' in query :
            npath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.2.2\\bin\\quick heal.exe"
            os.startfile(npath)

        elif 'open command prompt' in query :
            os.system("cmd")
        
        elif 'ip address' in query :
            ip = get ('https://api.ipify.org').text

            speak(f"your ip address is{ip}")

        elif 'open stackoverflow' in query or 'stack overflow' in query :
            webbrowser.open("www.stackoverflow.com")

            speak("opening stackoverflow")

        elif 'open youtube' in query or "open video online" in query:
            webbrowser.open("www.youtube.com")

            speak("Opening YouTube")

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
            speak("opening google")

            webbrowser.open("https://google.com")
            
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

        elif 'music from pc' in query or "music" in query or "songs" in query or "play songs" in query :
            speak("ok i am playing music")

            music_dir = "C:\\songs"
            musics = os.listdir(music_dir)
            
            os.startfile(os.path.join(music_dir,musics[0]))

        elif 'video from pc' in query or "video" in query:
            speak("ok i am playing videos")

            video_dir = './video'
            videos = os.listdir(video_dir)

            os.startfile(os.path.join(video_dir,videos[0]))  

        elif 'good bye' in query:
            speak("good bye , have a nice time")

            exit()

        elif "shutdown" in query:
            speak("shutting down")
            
            os.system('shutdown -s') 

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy','i am okey ! How are you']

            ans_q = random.choice(stMsgs)
            speak(ans_q)  

            ans_take_from_user_how_are_you = takecommand("take command")

            if 'fine' in ans_take_from_user_how_are_you or 'happy' in ans_take_from_user_how_are_you or 'okey' in ans_take_from_user_how_are_you:
                speak('Good to hear that!')  

            elif 'not' in ans_take_from_user_how_are_you or 'sad' in ans_take_from_user_how_are_you or 'upset' in ans_take_from_user_how_are_you:
                speak('What can I do to make you happy, sir?')  

        elif 'make you' in query or 'created you' in query or 'develop you' in query:

            ans_m = " For your information Genius Aditya Singh Created me ! I give Lot of Thannks to Him "
            print(ans_m)
            
            speak(ans_m)

        elif "who are you" in query or "about you" in query or "your details" in query:
            about = "I am Friday an A I based computer program but i can help you lot like a your close friend ! i promise you ! Simple try me to give simple command ! like playing music or video from your directory i also play video and song from web or online ! i can also entetain you i so think you Understand me ! ok Lets Start "
            print(about)
            
            speak(about)

        elif "hello" in query or "hello friday" in query:
            hel = "Hello ! How May i Help you.."
            print(hel)

            speak(hel)

        elif "i love you" in query or "i love you friday" in query:
            ans_m = "What the fuck! welcome to friendzone.."
            print(ans_m)

            speak(ans_m)

        elif "your name" in query or "sweat name" in query:
            na_me = "Thanks for Asking my name; myself Friday"  
            print(na_me)

            speak(na_me)

        elif "you feeling" in query:
            print("feeling Very sweet after meeting with you")
            speak("feeling Very sweet after meeting with you") 

        elif query == 'none':
            continue 

        elif 'exit' in query or 'abort' in query or 'stop' in query or 'bye' in query or 'quit' in query :
            ex_exit = 'I am feeling very sweet after meeting with you but you are going! i am very sad'
            speak(ex_exit)
            
            exit()

        elif 'jokes' in query or 'tell me a joke' in query or 'tell me jokes' in query :
            talk =(pyjokes.get_joke())

        else:
            temp = query.replace(' ','+')

            g_url="https://www.google.com/search?q="    

            res_g = 'sorry! i cant understand but i search from internet to give your answer ! okay'
            print(res_g)
            
            speak(res_g)

            webbrowser.open(g_url+temp)  




