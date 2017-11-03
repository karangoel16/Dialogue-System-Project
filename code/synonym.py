import os
import configparser
import nltk
import 
DirName='/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])
config = configparser.ConfigParser()
config.read(DirName+"/Config.ini");

#in this class we will have to send the object of the speech that has been initialised in the initial array 
class Synonym:
    def __init__(self,speech):
        self.speech=speech