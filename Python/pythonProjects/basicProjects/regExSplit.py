import re

# Using the regex.split function finds all the "a"s and "o"s in a sentence and replaces them with "@" or "0"
def changeLetters(sentence):
    newSent = ""
    finalSent = ""
    splitSent = re.split('(a+)', sentence)
    for item in range(len(splitSent)):
        if splitSent[item] == "a":
           splitSent[item] = "@"
    for char in splitSent:
        newSent+=char
    splitSent = re.split('(o+)', newSent)
    for item in range(len(splitSent)):
        if splitSent[item] == "o":
           splitSent[item] = "0"
    for char in splitSent:
        finalSent+=char
    print(finalSent)

# Gets a sentence from the user then passes it to the changeletters function
def main():
    userSentence = input("Enter a sentence: ")
    #userSentence = ("I like eating a lot of apples.")
    changeLetters(userSentence)

if __name__ == "__main__":
    main()