from random import randint
import csv

"""
1. The Hangman program randomly selects a secret word from a list of secret words. The random module will provide this ability, so line 1 in program imports it.
2. The Game: Here, a random word (a fruit name) is picked up from our collection and the player gets limited chances to win the game.
3. When a letter in that word is guessed correctly, that letter position in the word is made visible. 
    In this way, all letters of the word are to be guessed before all the chances are over. 
4. For convenience, we have given length of word + 2 chances. For example, word to be guessed is mango, then user gets 5 + 2 = 7 chances, 
    as mango is a five-letter word.
"""
# Returns a secrete word from the secretWords.csv
def getSecretWord():
    with open("Python\pythonProjects\hangmanCanvas\secretWords.csv", "r") as csvFile:
        randRow = randint(1, 21) # Sets a random row for the csv file to find
        randCol = randint(1, 10) # Sets a random column for the csv file to return
        """
        First for loop returns the random row from the csvFile.
        Second loop finds the column and returns the word to the main function.
        """
        for index, row in enumerate(csvFile):
            if index == randRow:
                rowWords = row.split(",")
                for i in range(len(row)):
                    if i == randCol:
                        return rowWords[i]

# Makes sure the user only entered one character and the character isn't a duplicate
def checkUserInput(userInput, chars):
    uInput = ""
    try:
        if len(userInput) != 1:
            raise
    except:
        while len(uInput) != 1 and uInput not in chars:
            print("Please enter one character and a character you haven't used")
            uInput = input()
    finally:
        return uInput
    
def checkWord(secretWord, userInput):
    if userInput in secretWord:
        print("You got a letter!")
        return True
    else:
        print("This letter is not in the secret word.")
        return False
# If the player wins this function displays that
def won():
    print("You won`")

# If the player loses this function displays that
def lost():
    print("You lost")

# Main Function for hangman game
def main():
    SECRET_WORD = getSecretWord()
    MAX_ATTEMPT = len(SECRET_WORD) + 2
    userGuess = ""
    attempts = 0
    charactersUsed = []
    playing = True
    print(SECRET_WORD)
    print(f"The secret word is {len(SECRET_WORD)} character long!")
    while playing:
        print(f"You have { MAX_ATTEMPT - attempts} attempts left!")
        print(f"What is your guess?: ")
        userGuess = input()
        userGuess = checkUserInput(userGuess, charactersUsed)
        if userGuess == SECRET_WORD:
            won()
            playing = False
        if attempts > MAX_ATTEMPT:
            lost()
            playing = False
        # if checkWord(SECRET_WORD, userGuess):
        #     print(changeLetters())
        charactersUsed.append(userGuess)
        
if __name__ == "__main__":
    main()