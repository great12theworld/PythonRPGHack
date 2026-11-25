class phantomRouteEvents:
    def __init__(self, player, print_cool, minigame_type_word):
        self.player = player
        self.print_cool = print_cool
        self.minigame_type_word = minigame_type_word

    def event1(self): #the first event
        self.print_cool("Event of the year.\nYou are offered a job from Initiative Enterprises.\n")
        self.print_cool("'Hello. My name is irrelevant.'\n")
        self.print_cool("... \n\n")
        self.print_cool("'I was requested to give you a task.'\n\n")
        self.print_cool("SYSTEM: Choices will be presented in parentheses as such: (1) do nothing (2) talk back")
        self.print_cool("\nThis is your choice for this interaction: ")
        self.print_cool("(1) communicate (2) stay silent")
        while True:
            choice = input(",  1 or 2? ")
            if choice.strip() == "1":
                self.player.charisma += 10
                self.print_cool("\nYou: 'The job is?'")
                self.print_cool("\nHim: 'Oh, uuhm yes, please hack out 100k chips into Initiative Accounts, Thank you!'")
                break
            if choice.strip() == "2":
                self.print_cool("\nThe task is to pull 100k chips into Initiative Accounts. Complete it for a sum of 20k chips.")
                break
            else:
                self.print_cool("Please pick a number 1 or 2")
        success = self.minigame_type_word("hacking rn")
        if success == True:
            self.print_cool("\nYou accquire 100k chips for the Initiative by stealing from a variety of other companies.\nClaiming 20k from the man who hired your services.")
            self.player.money += 20000
            self.player.karma -= 20
        if success == False:
            self.print_cool("\nYou fail to hack through the systems, losing yourself reputation, but your refutation of fufiling the request to hack grants you additional karma points.")
            self.player.streetCred -= 20
            self.player.karma += 10
    def event2(self):
        self.print_cool("You are met with a tiny child.\n")
        self.print_cool("He looks at you longingly.\n")
        self.print_cool("As if he wants something from you.\n")
        self.print_cool("(1) Give him a few chips [- 20 chips]")
        self.print_cool("(2) Dont give him anything and continue on with your day")
        self.print_cool("(3) Tell him to get a job and yell at him")
        while True:
            choice = input("")
