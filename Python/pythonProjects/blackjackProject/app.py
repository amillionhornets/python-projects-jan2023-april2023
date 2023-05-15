from random import choices, randint
import csv
from re import sub,split

def bust():
    pass

def hit(playerCard1, playerCard2, usedCards):
    draw = ""
    with open(r"Python\pythonProjects\blackjackProject\cards.csv") as csvFile:
        pass
    while draw not in usedCards:
        pass

def dealCards(usedCards):
    with open(r"Python\pythonProjects\blackjackProject\cards.csv", "r") as cardFile:
        csvReader = csv.reader(cardFile, delimiter=",")
        next(csvReader)
        playerHand = []
        dealerHand = []
        card = ""
        for i in range(4):
            randRow = randint(2,53)
            for index, row in enumerate(cardFile):
                if index == randRow:
                    card = sub("\n","",row)
            if (i % 2) == 0:
                playerHand.append(card)
            else:
                dealerHand.append(card)
        usedCards = dealerHand + playerHand + usedCards
        return {"Player Hand": playerHand, "Dealer Hand": dealerHand, "Used Cards": usedCards}
def main():
    usedCards = []
    playerCard1 = split(",", dealCards(usedCards)["Player Hand"][0]) 
    playerCard2 = split(",", dealCards(usedCards)["Player Hand"][1])
    dealerHand = dealCards(usedCards)["Dealer Hand"]
    usedCards = dealCards(usedCards)["Used Cards"]
    playerTotal = 0
    print(playerCard1[0])
    print(playerCard2[0])
    if playerCard1[0] == '"ace"':
        playerTotal = str(11 + int(playerCard2[2])) + " or " + str(1 + int(playerCard2[2]))
    elif playerCard2[0] == '"ace"':
        playerTotal = str(11 + int(playerCard1[2])) + " or " + str(1 + int(playerCard1[2]))
    else:
        playerTotal = int(playerCard1[2]) + int(playerCard2[2])
    print("Your total is " + str(playerTotal))
    print("Would like to Hit(h) or Stand(s): ", end="")
    choice = input()
    if choice == "h":
        hit(playerCard1, playerCard2, usedCards)
    else:
        pass

if __name__ == "__main__":
    main()