#this is Auto translator shinae
import time
import datetime
import pyttsx3
import speech_recognition as sr
import os
import smtplib
from googletrans import Translator 
import gtts
import playsound

translator = Translator()

engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme ():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning!")
    elif hour>=12 and hour<18:
        speak("good afternoon!")
    else :
        speak("good evening!")



def takecom():
    r=sr.Recognizer()
    with sr.Microphone() as source :
        print("listening ... ")
        r.pause_threshold = 0.9
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language=input_lan)
        print(f"User said: {query}\n")

    except Exception :
        print("Say that again please...")
        query=""
        return "None" 
    return query

def tt ():
    translated = translator.translate(query, dest=output_lan)
    print(translated.text)
    converted_audio = gtts.gTTS(translated.text, lang=output_lan)
    converted_audio.save('r.mp3')
    playsound.playsound('r.mp3')
    os.remove('r.mp3')
    
   
    
#i just wanted to add feedback mechanism .... for fun
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('shineeaibot@gmail.com', 'radhakrishna')
    server.sendmail('shineeaibot@gmail.com', to, content)
    server.close() 

#program structure

if __name__ == "__main__":
        wishme()
        speak(" i Shenai welcome you to our project we chat . i am a auto translator to help you have a smooth conversation ")
        print(" i Shenai welcome you to our project we chat .  i am a auto translator to help you have a smooth conversation ")
        speak("kindly choose the languages to use ")
        print("""kindly choose the languages to use :
    code againt each language
    'af': 'afrikaans',
    'sq': 'albanian',
    'am': 'amharic',
    'ar': 'arabic',
    'hy': 'armenian',
    'az': 'azerbaijani',
    'eu': 'basque',
    'be': 'belarusian',
    'bn': 'bengali',
    'bs': 'bosnian',
    'bg': 'bulgarian',
    'ca': 'catalan',
    'ceb': 'cebuano',
    'ny': 'chichewa',
    'zh-cn': 'chinese (simplified)',
    'zh-tw': 'chinese (traditional)',
    'co': 'corsican',
    'hr': 'croatian',
    'cs': 'czech',
    'da': 'danish',
    'nl': 'dutch',
    'en': 'english',
    'eo': 'esperanto',
    'et': 'estonian',
    'tl': 'filipino',
    'fi': 'finnish',
    'fr': 'french',
    'fy': 'frisian',
    'gl': 'galician',
    'ka': 'georgian',
    'de': 'german',
    'el': 'greek',
    'gu': 'gujarati',
    'ht': 'haitian creole',
    'ha': 'hausa',
    'haw': 'hawaiian',
    'iw': 'hebrew',
    'he': 'hebrew',
    'hi': 'hindi',
    'hmn': 'hmong',
    'hu': 'hungarian',
    'is': 'icelandic',
    'ig': 'igbo',
    'id': 'indonesian',
    'ga': 'irish',
    'it': 'italian',
    'ja': 'japanese',
    'jw': 'javanese',
    'kn': 'kannada',
    'kk': 'kazakh',
    'km': 'khmer',
    'ko': 'korean',
    'ku': 'kurdish (kurmanji)',
    'ky': 'kyrgyz',
    'lo': 'lao',
    'la': 'latin',
    'lv': 'latvian',
    'lt': 'lithuanian',
    'lb': 'luxembourgish',
    'mk': 'macedonian',
    'mg': 'malagasy',
    'ms': 'malay',
    'ml': 'malayalam',
    'mt': 'maltese',
    'mi': 'maori',
    'mr': 'marathi',
    'mn': 'mongolian',
    'my': 'myanmar (burmese)',
    'ne': 'nepali',
    'no': 'norwegian',
    'or': 'odia',
    'ps': 'pashto',
    'fa': 'persian',
    'pl': 'polish',
    'pt': 'portuguese',
    'pa': 'punjabi',
    'ro': 'romanian',
    'ru': 'russian',
    'sm': 'samoan',
    'gd': 'scots gaelic',
    'sr': 'serbian',
    'st': 'sesotho',
    'sn': 'shona',
    'sd': 'sindhi',
    'si': 'sinhala',
    'sk': 'slovak',
    'sl': 'slovenian',
    'so': 'somali',
    'es': 'spanish',
    'su': 'sundanese',
    'sw': 'swahili',
    'sv': 'swedish',
    'tg': 'tajik',
    'ta': 'tamil',
    'te': 'telugu',
    'th': 'thai',
    'tr': 'turkish',
    'uk': 'ukrainian',
    'ur': 'urdu',
    'ug': 'uyghur',
    'uz': 'uzbek',
    'vi': 'vietnamese',
    'cy': 'welsh',
    'xh': 'xhosa',
    'yi': 'yiddish',
    'yo': 'yoruba',
    'zu': 'zulu' """)
        speak("please enter your 1st choice")
        input_lan=input("please enter 1st your choice")
        speak("please enter your 2nd choice")
        output_lan=input("please enter 2nd your choice")
        

        #going very basic now ...

        while True:
            query = takecom().lower()
            
        # feedback part
            
            if 'feedback ' in query:
                try:
                    speak("What do you want to say?")
                    print("What do u want say?")
                    content = takecom()
                    to = "shineeaibot@gmail.com"    
                    sendEmail(to, content)
                    speak("Email has been sent successfully !")
                    print("Email has been sent successfully !")
                except Exception as e:
                    speak("Sorry . I am not able to send this email")
                    print("Sorry . I am not able to send this email")
                break
            
            
           
            elif  "quit" in query : 
                break
            tt()

            
          
    

time.sleep(5)
