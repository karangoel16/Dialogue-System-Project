import os
import configparser
from synonym import Synonym
from universal import Universal
from PyDictionary import PyDictionary
import nltk

DirName='/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])
config = configparser.ConfigParser()
config.read(DirName+"/Config.ini");

#in this class we will have to send the object of the speech that has been initialised in the initial array 
#here the universal function is added to break the entire code such as exit statement should be called from this point

class Meaning:
    def __init__(self,speech):
        self.speech=speech
        self.synonym = Synonym(self.speech)
        self.universal = Universal(self.speech)
        self.dictionary = PyDictionary() 
        
    #when we start from the meaning and have to get the word of utterance
    def Start_Meaning(self,sent):
        for i in [key for key,val in nltk.pos_tag(nltk.word_tokenize(sent)) if val== "NN"]:
            if i != "meaning" and i != "word":
                map=self.dictionary.meaning(i)
                for key in map:
                    self.speech.speak("When "+ i +"used as "+key)
            #sleep(0.15)
                    for j in map[key]:
                        print(i+ ":"+ j)
                        self.speech.speak(j)
        #Need to add synonym of the word function from here