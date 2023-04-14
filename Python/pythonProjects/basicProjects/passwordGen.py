from random import choice
from string import ascii_letters

# Generates random characters then joins them into string.
# Then appends string into an array and returns all the generated passwords to the user
def makePass(amt, length):
    passwords = []
    character = ""
    for i in range(amt):
        currentPass = ""
        for x in range(length):
            character = choice(ascii_letters)
            currentPass = currentPass + character
        passwords.append(currentPass)
    return passwords

# Gets how many passwords and the length of the passwords from the user and passes the information into makePass function
def main():
    print("How many passwords would you like: ", end="")
    passAmt = int(input())
    print("How long would you like the password(s): ", end="")
    passLen = int(input())
    print(makePass(passAmt, passLen))
    
if __name__ == "__main__":
    main()