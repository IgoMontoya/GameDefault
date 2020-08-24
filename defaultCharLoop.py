print ("Welcome to Chose your own adventure python edition")
print ("")


players = []

playerCharacters = []

def playerNames():
    playerNum = int(input("How many players are playing? "))
    if playerNum > 4:
        print("I am sorry, unfortunately only four players are permitted.")

        return


    for playerId in range(playerNum):

        newPlayerName = input("What is player {}'s name? ".format(playerId + 1));
        players.append(newPlayerName)
    print("Welcome: {} !".format(" & ".join(players)));

def characters():
    charAmount = 3

    for index, player in enumerate(players):

        playerCreate = input("{} (player {}), do you have a character to create. (y/n)".format(
            player, str(index+1)))
        if playerCreate.lower() =="y":
            charAmount = int(input("How many characters does this player begin the game with?"))
            
            for x in range(0,(charAmount)):
                getCharName = input("Enter Next Char name ")
                getCharDice = input("Please enter the number of dice this char will use. ")
                getCharRole = input("Please enter the villagers role. ")

                charData = {
                    "name": getCharName,
                    "diceCount": getCharDice,
                    "role": getCharRole,
                    "playerName": player
                }
                
                newCharacter = Character(characterData=charData)
                newCharacter.printSummary()
                playerCharacters.append(newCharacter)
            

        if playerCreate.lower() == "n":
            defaultCapture = input("Would you like to begin with the default charatures. (y/n)?" )
            if defaultCapture.lower == "y":
                for x in range (0,3):
                    
                    DefaultCharName = ["Bob", "Sally", "Tommy"]
                    DefaultDiceCount = 1
                    DefaultRole = ['Builder', "Recruiter" , "Nothing"]



                    charData = {
                        "name": DefaultCharName(x),
                        "diceCount": DefaultDiceCount,
                        "role": DefaultRole(x),
                        "playerName": player
                    }

                    DefaultCharacters = Character(characterData=charData)
                    DefaultCharacters.printSummary()
                    playerCharacters.append(DefaultCharacters)
            if defaultCapture.lower == "n":
                print("Well it looks as though you dont really want to play.")

            
                continue





    print("Summary ==========================")
    for player in playerCharacters:
        print("{characterName} Controlled by {playerName}".format(
            playerName=player.playerName,
            characterName=player.name ))
    return

class Character:
    
    name = "default name"
    playerName = "john/jane doe"
    diceCount = "1"
    role = "vanillaPaste"

    def __init__(self, characterData):
        
        self.playerName = characterData['playerName']
        self.role = characterData['role']
        self.diceCount = characterData['diceCount']
        self.name = characterData['name']

    def printSummary(self):
        print("{player} summary: \r\n \r\nCharacters:\r\nName: {characterName} \r\nDice: {dice} \r\nRole: {role} \r\n"
                .format(
                    characterName=self.name, 
                    player=self.playerName,
                    dice=self.diceCount,
                    role=self.role));


playerNames()
characters()
