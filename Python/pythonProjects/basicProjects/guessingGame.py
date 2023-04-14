from random import randrange

# Uses randrange from random to generate a random number
randNum = randrange(0,100)

# Gets the user's initial Guess
userGuess = input("Guess a num between 1-100(You have 5 attempts): ")
userGuess = (int(userGuess))
attempts = 1
print(f"Attempts left: {5-attempts}")
won = True

# While the user's guess is not equal to the random number have the user keep guessing
while(userGuess != randNum): 
    print(f"--------------------------------------------------------")
    if(attempts >= 5): # Checks to make sure the user has used less than 5 attempts
        print("You ran out of attempts.")
        won = False
        break
    else: # Tells the user to guess higher or lower based on last guess
        if(userGuess < randNum):
            userGuess = (int(input("Guess Higher: ")))
        else:
            userGuess = (int(input("Guess Lower: ")))
    attempts+=1
    print(f"Attempts Left: {5-attempts}")

if(won):
    print("You win !!!")