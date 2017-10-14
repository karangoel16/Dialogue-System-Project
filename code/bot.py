import configparser #we will need it to read the config file which we will create later will contain voice and id
import os
import PyDictionary as dict
import nltk
from speech import Speech

DirName='/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])
config = configparser.ConfigParser()
config.read(DirName+"/Config.ini");

class Bot:
    def __init__(self):
        self.speech = Speech()
    def speak(self):
        sent = self.speech.listen()
        if 'meaning' in sent:
            print(nltk.pos_tags(nltk.word_tokenize(sent)))
        return sent
if __name__ == "__main__":
    bot = Bot()
    print(bot.speak())
