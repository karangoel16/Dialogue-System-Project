import os
import configparser
from synonym import Synonym
from universal import Universal
from PyDictionary import PyDictionary
import nltk

DirName='/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])
config = configparser.ConfigParser()
config.read(DirName+"/Config.ini");

class Antonym:
    def __init__(self,speech):
        self.speech = speech
        self.universal = Universal(speech)
        self.meaning = Meaning(speech)
        self.synonym = Synonym(speech)