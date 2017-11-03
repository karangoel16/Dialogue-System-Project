import os
import configparser
from PyDictionary import PyDictionary
import nltk

DirName='/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])
config = configparser.ConfigParser()
config.read(DirName+"/Config.ini");

#in this class we will have to send the object of the speech that has been initialised in the initial array 
class Synonym:
    def __init__(self,speech):
        self.speech=speech

    def Start_Synonym(self,sent):
        for i in [key for key,val in nltk.pos_tag(nltk.word_tokenize(sent)) if val== "NN"]:
            if i != "synonyms" and i != "word":
                self.Word_Meaning(i)
    def Word_Synonym(self,word)
        synList=self.dictionary.synonym(word)
        print(synList)
        if(len(synList)>0):
            self.speech.speak("Other word for" + word + "are")
            for j in synList:
                print(j)
                self.speech.speak(j)
        else:
            self.speech.speak("I am sorry . I don't know this word")