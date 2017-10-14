import configparser #we will need it to read the config file which we will create later will contain voice and id
import os
from PyDictionary import PyDictionary
import nltk
from speech import Speech
from time import sleep
import lxml

DirName='/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])
config = configparser.ConfigParser()
config.read(DirName+"/Config.ini");

class Bot:
    def __init__(self):
        self.speech = Speech()
        self.dictionary = PyDictionary() 
    def speak(self):
        sent = self.speech.listen()
        print(sent)
        if 'meaning' in sent:
            for i in [key for key,val in nltk.pos_tag(nltk.word_tokenize(sent)) if val== "NN"]:
                if i != "meaning" and i != "word":
                    map=self.dictionary.meaning(i)
                    for key in map:
                        self.speech.speak("When "+ i +"used as "+key)
                        sleep(0.15)
                        for j in map[key]:
                            print(j)
                            self.speech.speak(j)
        else:
            self.speech.speak("Invalid Response how can I help you")
        return sent
if __name__ == "__main__":
    bot = Bot()
    bot.speak()
