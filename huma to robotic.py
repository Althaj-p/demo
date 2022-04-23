import speech_recognition as sr
from gtts import gTTS
import os
voice= "" ''
while True:
    e=sr.Recognizer()
    with sr.Microphone ( ) as source :
        try:
            audio=e.listen(source)
            text=e.recognize_google(audio)
            print(text)
            if text=="top" :
                break
            text=e.recognize_google(audio)
            voice=voice+str(text)
        except:
            print("say something")
we-gTTS(text=voice,lang="en",slow=false)
we.save("A.wav")
