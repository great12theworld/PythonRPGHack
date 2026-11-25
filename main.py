import time
import sys
import random
from phantom_route_events import phantomRouteEvents





timeForMessage = 0.01

class player:
    def __init__(self, money, health, karma, hackLevel, streetCred, charisma, type):
        self.money = money
        self.health = health
        self.karma = karma
        self.hackLevel = hackLevel
        self.streetCred = streetCred
        self.charisma = charisma
        self.type = type
        self.year = 1

        def removeMoney(self,amount): #basicaly, if you have the money then returns and takes away that money, if not then doesnt and reutrns false
            if amount <= self.money:
                self.money -= amount
                printCool("\nPaid out " + str(amount) + " chips")
                return True
            else:
                printCool("\nUnable to pay that out right now")
                return False 

def minigameTypeWord(stringToType):
    printCool("\n Your goal is to type the following string EXACTLY the same within the next 10 seconds to successfully hack the system\n")
    duration = 10
    print("line to write: '" + stringToType + "'  ")
    x = input("\nPress enter to begin.") #its not meant to be accessed computa'
    start_time = time.perf_counter()
    y = input("\nGo! >")
    elapsed = time.perf_counter() - start_time

    if elapsed > duration:
        printCool("You failed.")
        return False
    elif y == stringToType:
        printCool("You Succeed. Well done.")
        return True
    else:
        printCool("You made a typo, you failed.")
        return False

def minigameGuessTheNumber(guessCount):
    printCool("Your goal is to guess a number 1-100, you have " + str(guessCount) + " tries.\n")
    number = random.randint(1,100)
    current = guessCount -1
    while True:
        guess = input("Pick a number 1-100\n")
        if current == 0:
            printCool("You failed to guess in the number of tries provided.\n")
            break
        if current > 0:
            if int(guess) == number:
                printCool("You got the number!\n")
                break
            elif int(guess) > number:
                printCool("Too high\n")
                current = current -1
            elif int(guess) < number:
                printCool("Too low\n")
                current = current -1






p1 = None

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
    global p1
    printCool("\nThis is the setup page\n")
    printCool("What life do you want to begin with? Note: there are more stats that are not shown here.\n")
    printCool("(1) Life of a Criminal, you start with low money, health, and karma, but you'll have moderate street credit and better hacking level\n\n")
    printCool("(2) Life of an Average, you have slightly below average money (you're in night city choom.), moderate health, neutral karma, no street cred, and no hacking level\n\n")
    printCool("(3) Life of the Rich, you have good money, good health, bad karma from shady deals, no street cred, no hacking level, people despise you for holding all the wealth and you are a big target.\n\n")
    printCool("(4) Life of the Phantom, you work as a phantom, insane money, good health, neutral karma, no street cred, incredible hacking level, people dont see you, you are a ghost hacker working for big corpo. \n\n")

    while True:
        pathway = input("Pick one (1-4): ").strip()
        if pathway == "1":
            p1 = player(10, 30, -20, 4, 50, 10, "Criminal")
            break
        elif pathway == "2":
            p1 = player(50, 60, 0, 1, 0, 40, "Average")
            break
        elif pathway == "3":
            p1 = player(100, 100, -40, 1, 0, 10, "Rich")
            break
        elif pathway == "4":
            p1 = player(300, 100, 0, 0, 5, 0, "Phantom")
            break
        else:
            printCool("Please enter a number from 1 to 4.\n")

    printCool("You have selected the route of the " + p1.type + ". Good luck, your setup has been complete, type in SETTINGS in all caps to enter the settings page.")


def eventPhantom():
    events = phantomRouteEvents(p1, printCool, minigameTypeWord)
    if p1.year == 1:
        events.event1()
        p1.year += 1
    elif p1.year == 2:
        printCool("Event two here")
    elif p1.year == 3:
        printCool("Event three here")

def eventCriminal():
    printCool("Add criminal event class and event segments here")
        



def main():
    global timeForMessage
    currentPage = "Homepage"

    while True:
        if currentPage == "Homepage":
            printCool("It is currently your number " + str(p1.year) + " year. Once you turn 60 you die.\n")
            printCool("To enter settings type the number (1)  \n")
            printCool("To advance to the next year type (2)  \n")
            printCool("To end the game type (3)  \n")
            currentInput = input("This is the homepage, what do you want to do?")
            if currentInput == "1":
                printCool("For speed of text please input a number from 1-100\nSmaller number means faster text.")
                while True:
                    printSettingInput = input("Enter a number from 1-100: ").strip()
                    try:
                        speed = int(printSettingInput)
                        if 1 <= speed <= 100:
                            break
                        printCool("Please enter a number from 1 to 100.\n")
                    except ValueError:
                        printCool("Please enter a number from 1 to 100.\n")
                timeForMessage = speed / 100
                printCool("Text speed set to " + str(speed) + ".")

            if currentInput == "2":
                if p1.type == "Phantom":
                    eventPhantom()
                if p1.type == "Rich":
                    printCool("Rich event here")
                if p1.type == "Average":
                    printCool("Average event here")
                if p1.type == "Criminal":
                    printCool("Criminal event here")

            if currentInput == "3":
                currentPage = "End"
 
        if currentPage == "End":
            printCool("This system is terminating as it has run it's course.\n")
            printCool("You ended with the following stats: \n")
            print(vars(p1))
            insert = input("Terminate program? ")
            choice = insert.strip().lower()
            if choice in ("yes", "y", "ye"):
                printCool("Terminating...")
            elif choice in ("no", "n"):
                timeForMessage = 0.07
                printCool("Too bad.")
            else:
                printCool("I didn't understand. Terminating anyway.")
            time.sleep(3)
            sys.exit(0)


opening()
setup()
main()
