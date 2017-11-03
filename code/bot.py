import configparser #we will need it to read the config file which we will create later will contain voice and id
import os
from PyDictionary import PyDictionary
import nltk
from speech import Speech
from universal import Universal
from time import sleep
from meaning import Meaning
from synonym import Synonym
from antonym import Antonym
import lxml
import webbrowser
import apiai
import nltk

DirName='/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])
config = configparser.ConfigParser()
config.read(DirName+"/Config.ini");

class Bot:
    def __init__(self):
        """
            here the main speech module is speech which is in the file
            here the dictionary modusle is PyDictionary which will be using 
        """
        self.speech = Speech()
        self.dictionary = PyDictionary() 
        self.universal = Universal(self.speech)
        self.meaning = Meaning(self.speech)
        self.synonym = Synonym(self.speech)
        self.antonym = Antonym(self.speech)
    def speak(self):
        sent = self.speech.listen()
        print(sent)
        if 'meaning of' in sent:
            self.meaning.Start_Meaning(sent)
        elif 'synonyms' in sent:
            for i in [key for key,val in nltk.pos_tag(nltk.word_tokenize(sent)) if val== "NN"]:
                if i != "synonyms" and i != "word":
                    synList=self.dictionary.synonym(i)
                    print(synList)
                    if(len(synList)>0):
                        self.speech.speak("Other word for" + i + "are")
                        for j in synList:
                            print(j)
                            self.speech.speak(j)
                    else:
                        self.speech.speak("I am sorry . I don't know this word")
        elif 'antonyms' in sent:
            for i in [key for key, val in nltk.pos_tag(nltk.word_tokenize(sent)) if val == "NN"]:
                if i != "synonyms" and i != "word":
                    synList = self.dictionary.antonym(i)
                    print(synList)
                    if (len(synList) > 0):
                        self.speech.speak("Antonyms of" + i + "are")
                        for j in synList:
                            print(j)
                            self.speech.speak(j)
                    else:
                        self.speech.speak("I am sorry . I don't know this word")

        else:
            self.universal.check(sent)
            self.speech.speak("Invalid Response how can I help you")
        return sent
if __name__ == "__main__":
    bot = Bot()
    bot.speech.speak("hello how are you? I am wordie your personnel dictionary to know more abour words and learn about it")
    while(True):
        key=input("Ready to continue? Yes/No")
        if(key=="Yes"):
            bot.speak()
        if(key=="No"):
            break
    webbrowser.open("https://goo.gl/forms/iAhwQjjpAB1iMzEZ2")