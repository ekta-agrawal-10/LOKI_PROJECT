from pydub.playback import play
from pydub import AudioSegment
from io import BytesIO
from gtts import gTTS
import pyttsx3
from googletrans import Translator

engine = pyttsx3.init()

translator = Translator()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


text = input("Enter text: ")
translated_text = translator.translate(text, dest='en')
print(translated_text.text)
speak(translated_text.text)


def speak(translated_text):
    tts = gTTS(translated_text.text)
    fp = BytesIO()
    tts = tts.write_to_fp(fp)
    fp.seek(0)
    song = AudioSegment.from_file(fp, format="mp3")
    play(song)


def speak0(txt):
    translator = Translator()
    translated_text = translator.translate(txt)
    speak(translated_text)


translator = Translator()
destlang = input("Please enter code of destination language: ")
filename = input("Enter Filename: ")

with open(filename, encoding='utf8') as f:
    text = f.read()

translated_text = translator.translate(text, dest=destlang)
print(translated_text.text)
speak(translated_text)
