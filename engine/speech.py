import pyttsx3
from engine import readpdf
from gtts import gTTS
from playsound import playsound
import os
async def textToSpeech():   
    engine = pyttsx3.init()
    txt = readpdf.return_text()
    voice = engine.getProperty('voices')
    # speed = engine.getProperty('rate')
    engine.setProperty('rate',190)
    engine.setProperty('voice', voice[1].id)
    engine.say(txt)
    engine.runAndWait() 
    engine.stop()

async def usingGoogle():
    Message = readpdf.return_text()
    speech = gTTS(text = Message,lang = 'en')
    speech.save('temp.mp3')
    playsound('temp.mp3')
    os.remove('temp.mp3')

async def usingGoogle2():
    message = readpdf.return_custom()

    if(len(message)==0):
        speech = gTTS(text = "No text Detected",lang = 'en')
    else: 
        speech = gTTS(text = message,lang = 'en')
    
    speech.save('temp2.mp3')
    playsound('temp2.mp3')
    os.remove('temp2.mp3')
    os.remove('ourpdf.pdf')
