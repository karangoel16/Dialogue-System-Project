from tkinter import *
from bot import Bot
import configparser 
import webbrowser
import os

DirName='/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])
config = configparser.ConfigParser()
config.read(DirName+"/Config.ini");

class menuItems(object):
    def __init__(self):
        menubar = Menu(app)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="New...", command=self.new())
        filemenu.add_command(label="Open...", command=self.open())
        filemenu.add_command(label="Save", command=self.save())
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=app.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        app.config(menu=menubar)

    def new(self):
        pass

    def open(self):
        pass

    def save(self):
        print("You have saved the file")

def init():
    global app, menu
    app = Tk()
    bot = Bot()
    app.title("Words with Python")
    bot.speech.speak("hello how are you? I am wordie your personnel dictionary to know more abour words and learn about it, I can tell meaning of words or I can tell you synonym of words, some of the features are getting build")
    app.geometry("800x500+50+50")
    menu = menuItems()
    frame = Frame(app)
    scrollbar = Scrollbar(frame, orient=VERTICAL)
    textbox = Text(frame, yscrollcommand=scrollbar.set)
    scrollbar.config(command=textbox.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    textbox.pack(side=LEFT, fill=BOTH, expand=1)
    frame.pack(fill=BOTH, expand=1)

    #button = Button(app, text="Nothing", command=this_will_run_even_though_it_should_not())

    return

if __name__ == "__main__":
    """
    bot = Bot()
    root= Tk()
    frame = Frame(root)
    button = Button(frame)
    frame.pack()
    button['text'] ="Good-bye."
    button['command'] = close_window
    button.pack()
    root.mainloop()
    bot.speech.speak("hello how are you? I am wordie your personnel dictionary to know more abour words and learn about it")
    webbrowser.open('http://gatedin.com')
    """
    init()
    app.mainloop()
    webbrowser.open('http://gatedin.com')