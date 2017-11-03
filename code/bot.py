import configparser #we will need it to read the config file which we will create later will contain voice and id
import os
from PyDictionary import PyDictionary
import nltk
from speech import Speech
from universal import Universal
from time import sleep
import lxml
import webbrowser
import apiai

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
        
    def speak(self):
        sent = self.speech.listen()
        print(sent)
        if 'meaning of' in sent:
            for i in [key for key,val in nltk.pos_tag(nltk.word_tokenize(sent)) if val== "NN"]:
                if i != "meaning" and i != "word":
                    map=self.dictionary.meaning(i)
                    for key in map:
                        self.speech.speak("When "+ i +"used as "+key)
                        #sleep(0.15)
                        for j in map[key]:
                            print(i+ ":"+ j)
                            self.speech.speak(j)
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