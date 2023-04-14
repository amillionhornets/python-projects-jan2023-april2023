import os
import msvcrt

# Shows the first 20 numbers in the Fibonacci Sequence
# The Fibonacci sequence is a sequence in which each number is the sum of the two preceding ones
def showFib():
    previousNum = 0
    sequence = [1]
    for i in range(1, 20, 1):
        sequence.append(sequence[i - 2] + previousNum)
        previousNum = sequence[i]
    for a in range(0, len(sequence)):
        print(f"Fibonacci #{a + 1} is : {sequence[a]}")

# Shows all the perfect numbers under 1000
# A perfect number is a positive integer that is equal to the sum of its proper divisors
# 6 is a Perfect number because 1 + 2 + 3 = 6
def showPerNum():
    currentNum = 1
    sumList = []
    sum = 0
    while currentNum < 1000:
        for i in range(1, currentNum):
            if (currentNum % i) == 0:
                sumList.append(i)
        if sumList != False:
            for num in sumList:
                sum+=num
        if sum == currentNum:
            print(f"Perfect Number: {currentNum}")
        sumList = []
        sum = 0
        currentNum+=1

# Checks for an input between each showing of either the fib sequence or perfect nums
def checkInput():
    clear = lambda: os.system('cls')
    print("press any key to continue ...")
    while True:
        # input()
        if msvcrt.kbhit() == True:
            clear()
            break
        
def main():
    while True:
        choice = input("1) Show Fibonacci Numbers \n2) Show Perfect Numbers \n3) Exit \nSelect an option: ")
        try:
            choice = int(choice)
            if choice == 1:
                pass
            elif choice == 2:
                pass
            elif choice == 3:
                break
            else:
                 raise Exception("Input a correct choice!")
        except:
            choice = input("Input correct choice: ")   
        if choice == 1:
            showFib()
            checkInput()
        elif choice == 2:
            showPerNum()
            checkInput()
        elif choice == 3:
            break

if __name__ == "__main__":
    main()