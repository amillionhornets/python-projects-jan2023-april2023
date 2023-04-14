
# Uses modulo to check if a user inputed number is odd or even
def checkOddorEven(userNumber):
    number = int(userNumber) % 2
    if(number == 1):
        print("The number is odd!")
    else:
        print("The number is even!")

userNum = input("Enter a number: ")
checkOddorEven(userNum)