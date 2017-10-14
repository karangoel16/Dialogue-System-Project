import speech_recognition as sr
import pyttsx3 #we will use this to implment module to speak the text when needed
from time import sleep
class speech:
    def __init__(self):
         self.r = sr.Recognizer()
         self.engine = pyttsx3.init()
    def listen(self):
        with sr.Microphone() as source:
            audio = self.r.listen(source)
        try:
            return self.r.recognize_google(audio)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request result from Google Speech Recognition Service; {0}".format(e) )
    def speak(self,text):
        self.engine.say(text)
        self.engine.runAndWait()
        
if __name__ == "__main__":
    speech=speech()
    speech.speak(speech.listen())