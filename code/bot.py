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
                        #sleep(0.15)
                        for j in map[key]:
                            print(j)
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
            self.speech.speak("Invalid Response how can I help you")
        return sent
if __name__ == "__main__":
    bot = Bot()

    #speech.speak("hi, How are you doing")
    # sleep(0.15)
    bot.speech.speak("hi, How are you doing")
    while(True):
        bot.speak()
        bot.speech.speak("Would you like to exit or do something else?")
        print("Would you like to exit or Continue?")
        val=bot.speech.listen()
        if "exit" in [i.lower() for i in nltk.word_tokenize(val)]:
            bot.speech.speak("Thankyou! have a nice day")
            break
