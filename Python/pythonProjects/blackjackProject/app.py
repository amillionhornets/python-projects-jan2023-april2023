from random import choices, randint
import csv

def bust():
    pass

def hit():
    pass

def dealCards():
    with open(r"Python\pythonProjects\blackjackProject\cards.csv", "r") as cardFile:
        csvReader = csv.reader(cardFile, delimiter=",")
        next(csvReader)
        for i in range(2):
            randRow = randint(2,53)
            



def main():
    dealCards()

if __name__ == "__main__":
    main()