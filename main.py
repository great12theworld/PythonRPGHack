import time
import sys

currentPage = "Setup"

year = 1

timeForMessage = 0.03

class player:
    def __init__(self, money, health, karma, hacklLevel, streetCred, type):
        self.money = money
        self.health = health
        self.karma = karma
        self.hackLevel = hacklLevel
        self.streetCred = streetCred
        self.type = type

p1 = player()

def printCool(string):
    for x in string:
        print(x,end="",flush=True)
        time.sleep(timeForMessage)
def opening():
    printCool("Welcome to the CyberRealm choom.\n")
    printCool("How you doing?")
    doing = input(" Answer: ")
    if (doing == "bad"):
        printCool("Shucks, try to feel better before playing\nbut ok.") # BRO I KEEP TYPING IN JS ON ACCIDENT IM GONNA TWEAKK
    else:
        printCool("Glad to hear it! Unless you said you felt bad in which case\nI am deeply sorry. Have fun!")
    printCool("\nHeres the Game!!!")

def setup():
    printCool("This is the setup page\n")            
    printCool("What life do you want to begin with?\n")
    printCool("(1) Life of a Criminal, you start with low everything, but you'll have moderate street credit and high hacking level")


def main():
    global timeForMessage


    while True:
        if currentPage == "Homepage":
            printCool("It is currently your number" + year + " year. Once you turn 60 you die.\n")
            printCool("You can do the following \n(1) Hack Rando\n(2) Focus on yourself\n(3)Settings")
            currentInput = input("This is the homepage, what do you want to do?  ")
 
            if currentInput == "3":
                printCool("For speed of text please input a number from 1-100\nSmaller number means faster text.")
                printSettingInput = input("a number from 1-100, this is tenths of a millisecond  ")
                timeForMessage =  float(printSettingInput)/10
                printCool("This is the text")
 
        else:
            printCool("This system is terminating as it has run it's course.")
            sys.exit(0)

opening()
