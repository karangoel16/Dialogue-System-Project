import speech_recognition as sr
import pyttsx3 #we will use this to implment module to speak the text when needed
import os
import configparser
from time import sleep

DirName='/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])
config = configparser.ConfigParser()
config.read(DirName+"/Config.ini");

class Speech:
    def __init__(self):
         self.r = sr.Recognizer()
         self.engine = pyttsx3.init()

    def listen(self):
        with sr.Microphone() as source:
            audio = self.r.listen(source)
        try:
            if config.get('Bot','Google_Api')=="None":
                return self.r.recognize_google(audio)
            else:
                return "Api needs to be added "
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request result from Google Speech Recognition Service; {0}".format(e) )

    def speak(self,text):
        self.engine.setProperty('rate',int(config.get('Bot','Voice_Rate')))
        #self.engine.setProperty('rate', 200)
        self.engine.setProperty('voice', config.get('Speech','voice'))
        self.engine.say(text)
        self.engine.runAndWait()

        
if __name__ == "__main__":
    speech=Speech()
    speech.speak(speech.listen())