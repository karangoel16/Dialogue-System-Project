import os
import configparser
from universal import Universal
from PyDictionary import PyDictionary
import nltk

DirName='/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])
config = configparser.ConfigParser()
config.read(DirName+"/Config.ini");

class Antonym:
    def __init__(self,speech):
        self.speech=speech
        self.universal = Universal(self.speech)
        self.dictionary = PyDictionary() 
    def Start_Antonym(self,sent):
        print("I am start antonyms1")
        for i in [key for key, val in nltk.pos_tag(nltk.word_tokenize(sent)) if val == "NN"]:
          if i != "antonyms" and i != "word":
            print("I am start antonyms")
            self.Word_Antonym(i)
    def Word_Antonym(self,word):
        antList = self.dictionary.antonym(word)
        print(antList)
        if (len(antList) > 0):
            self.speech.speak("Antonyms of" + word + "are")
            for j in antList:
                print(j)
                self.speech.speak(j)
        else:
            self.speech.speak("I am sorry . I don't know this word")