import time

timeForMessage = 0.03

class player:
    def __init__(self):
        self.money = 100
        self.health = "Good"

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

def main():
    while True:
        

opening()
