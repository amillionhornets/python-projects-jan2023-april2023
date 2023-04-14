import re

# Check to see if the user has won
def checkWin(secretWord, guess, currentFinds,currentMan,nextMan):
    attempts = drawMan(guess,currentMan,nextMan)
    currentWord = ""
    for char in currentFinds:
        currentWord+=char
    if attempts < 6 and secretWord != currentWord:
        return False
    elif attempts >= 6:
        print("You lost!")
        return True
    else:
        print("You won!")
        return True

# Searches through the secret word and returns len of the same letters
def findLetter(word, letter):
    guess = re.findall(letter, word)
    return len(guess)    

# If the user gets a wrong letter draws the next man
def drawMan(letters,currentMan,nextMan):
    if letters > 0:
        for item in currentMan:
            print(f'{item}, ' , end='')
    else:
        currentMan.append(nextMan[0])
        nextMan.pop(0)
        for item in currentMan:
            print(f'{item}, ' , end='')
    print("\n")
    return len(currentMan)

# Displays the current string of user guesses
def display(word, letter, currentWord):
    for i in range(len(word)):
        if word[i] == letter:
            currentWord[i] = letter
    for letter in currentWord:
        print(letter, end='')
    print("\n")

# Gets the secret word and plays the hangman game
def main():
    secretWord = input("Input a word: ")
    currentFinds = []
    currentMan = []
    nextMan = ['head','body','R arm','L arm','R leg','L leg']
    for item in secretWord:
        if item == " ":
            currentFinds.append(" ")
            continue
        currentFinds.append("_")
    while True:
        guess = input("Guess a letter: ")
        lettersFound = findLetter(secretWord, guess)
        if lettersFound > 0:
            display(secretWord,guess, currentFinds)
            if checkWin(secretWord,lettersFound,currentFinds,currentMan,nextMan):
                break
        else:
            if checkWin(secretWord,lettersFound,currentFinds,currentMan,nextMan):
                break

if __name__ == "__main__":
    main()