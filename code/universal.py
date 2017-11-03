import nltk

class Universal:
    def __init__(self,speech):
        """
            We will have parameterized speech from the bot module
        """
        self.speech = speech

    def check(self,text):
        """
            This is the main check module which will keep the identity of universal function to be used 

        """
        self.exit(text)
        return False
    def exit(self,text):
        """
            here the text is the sentence which we will get from the main bot module we will need to see
            if it has "word" exit in it or not
        """
        print("We are in exit module now")
        print("exit" in text)
        if "exit" in text:
            self.speech.speak("Do you want to exit, Please press Yes in 10 sec")     
        
        
    
