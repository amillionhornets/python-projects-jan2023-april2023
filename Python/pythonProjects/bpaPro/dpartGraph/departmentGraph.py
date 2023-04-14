import os
import msvcrt
import matplotlib.pyplot as plt
import numpy
import time

# Makes the user press a key on their keyboard before displaying the vertical graph
def waitForKbhit():
    clear = lambda: os.system("cls")
    while True:
        if msvcrt.kbhit() == True:
            time.sleep(.5)
            keyHit = input("clearing")
            clear()
            break

# Displays the list of all the departments at Up Town University and Returns them to the user
def getDepartment():
    print('Up Town University\n 0. English Department\n 1. Mathmatics Department\n', 
          '2. Computer Science Department\n 3. Business Department\n 4. Kinesiology',
          'Department\n 5. Archeiture Dpeartment\n ')
    choice = input("Please pick the department: ")
    while True:
        try:
            choice = int(choice)
            if choice >= 10 or choice < 0:
                raise
        except:
            choice = input("Enter a number 0-9")
        else:
            break
    return choice

# Check the class size for all the class in a department. All the departments have 10 classes
def checkClassSize(department):
    classes = []
    for i in range(0,10):
        print("Class sizes are from 0 - 40 students.")
        classSize = input(f"{(department*100) + i}: ")
        while True:
            try:
                classSize = int(classSize)
                if classSize > 40 or classSize < 0:
                    raise
            except:
                classSize = input("Please enter numbers only 0-40: ")
            else: 
                break
        classes.append(classSize)
    return classes

# Gets the department data then puts it into a console graph using for loops
def displayHoriGraph(department, classSizes):
    print("Department                               Students")
    for i in range(len(classSizes)):
        print(f"{department}0{i} ", end='')
        for a in range(0, 40):
            if a < classSizes[i]:
                print("*",end="")
            else:
                print(" ",end="")
        print(f" {classSizes[i]}")
    print("Press ANY key to see vertical graph.")
    waitForKbhit()

# Gets the department data an puts it into a matplotlib.pyplot graph
def displayVertGrap(department, classSizes):
    classes = []
    for i in range (0,10):
        classes.append(f"{department}0{i}")
    x = numpy.array([classes[0],classes[1],classes[2],classes[3],classes[4],classes[5],classes[6],classes[7],classes[8],classes[-1]])
    y = numpy.array([classSizes[0],classSizes[1],classSizes[2],classSizes[3],classSizes[4],classSizes[5],classSizes[6],classSizes[7],classSizes[8],classSizes[-1]])
    plt.bar(x,y)
    try:
        plt.show()
    except:
        pass

# Gets information about the departments and returns them in a graph format to the user
def main():
    while True:
        clear = lambda: os.system('cls')
        department = getDepartment()
        classSizes = checkClassSize(department)
        clear()
        displayHoriGraph(department, classSizes)
        displayVertGrap(department, classSizes)
        runAgain = input("Run the program again (y\\n)?: ")
        if runAgain == "y":
            continue
        else:
            break

if __name__ == "__main__":
    main()