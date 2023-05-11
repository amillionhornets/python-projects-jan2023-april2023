from random import randint
import csv

"""
1. The Hangman program randomly selects a secret word from a list of secret words. The random module will provide this ability, so line 1 in program imports it.
2. The Game: Here, a random word is picked up from our collection and the player gets limited chances to win the game.
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
    try:
        if len(userInput) != 1:
            raise Exception()
        if not userInput.isalpha():
            raise Exception()
        if userInput in chars:
            raise Exception()
    except:
        while len(userInput) != 1 or userInput in chars:
            print("Please enter one character and a character you haven't used")
            userInput = input()
    finally:
        return userInput

    
def checkWord(secretWord, userInput):
    if userInput in secretWord:
        print("You got a letter!")
        return True
    else:
        print("This letter is not in the secret word.")
        return False   

# If the player wins this function displays that
def won(secretWord):
    print("You won!")
    print(f"The secret word was {secretWord}")
    return False

# If the player loses this function displays that
def lost(secretWord):
    print("You lost")
    print(f"The secret word was {secretWord}")
    return False

def appendCurrentWord(uGuess, currentWord, Secretword):
    finalWord = ""
    for i in range(len(Secretword)):
        if currentWord[i] == Secretword[i]:
            finalWord+=currentWord[i]
            continue
        elif Secretword[i] == uGuess:
            finalWord = finalWord + uGuess
        else:
            finalWord+="_"
    return finalWord
        
# Main Function for hangman game
def main():
    SECRET_WORD = getSecretWord()
    # SECRET_WORD = "apple"
    max_attempts = len(SECRET_WORD) + 2
    userGuess = ""
    attempts = 0
    currentWord = ""
    for i in range(len(SECRET_WORD)):
        currentWord+="_"
    charactersUsed = []
    playing = True
    # print(SECRET_WORD)
    print(f"The secret word is {len(SECRET_WORD)} character long!")
    while playing:
        print(f"-----------------------------------------------------")
        print(f"You have { max_attempts} attempt(s) left!")
        print(f"What is your guess?: ")
        userGuess = input()
        userGuess = checkUserInput(userGuess, charactersUsed)
        if userGuess in SECRET_WORD:
            # print(userGuess)
            currentWord = appendCurrentWord(userGuess, currentWord, SECRET_WORD)
            
            if currentWord == SECRET_WORD: 
                playing = won(SECRET_WORD)
                break
        else:
            max_attempts-=1
        if max_attempts <= 0:
            playing = lost(SECRET_WORD)
            break
        
        charactersUsed.append(userGuess)
        print(currentWord)
        
if __name__ == "__main__":
    main()