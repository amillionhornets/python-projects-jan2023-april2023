import csv
import json
import os
import msvcrt
from prettytable import PrettyTable

# Checks to see if the user hit their keyboard to continue the program
def keyBoardHit():
    clear = lambda: os.system('cls')
    hitKeyboard = True
    print("Press any key to continue...")
    while hitKeyboard:
        if msvcrt.kbhit() == True:
            clear()
            hitKeyboard = False

# Takes the user's inputs and puts it into a temp csv file
def insertCSV(userName, userCert, userYear):
    if os.path.isfile("pythonProjects\\csvJsonPro\\student.csv"):    
        with open("pythonProjects\\csvJsonPro\\student.csv", "a") as csvFile:
            writer = csv.writer(csvFile, delimiter=",", lineterminator="\n")
            writer.writerow([userName,userCert,userYear])
    else:
        with open("pythonProjects\\csvJsonPro\\student.csv", "w") as csvFile:
            writer = csv.writer(csvFile, delimiter=",", lineterminator="\n")
            writer.writerow(['Name','Certification','Year'])
            writer.writerow([userName,userCert,userYear])

# Displays the CSV in a table from the PrettyTable
def displayCSV():
    csvTable = PrettyTable()
    jsonToCSV()
    with open("pythonProjects\\csvJsonPro\\student.csv", "r") as csvFile:
        reader = csv.reader(csvFile, delimiter=",")
        next(reader)
        for line in reader:
            csvTable.add_row([line[0],line[1],line[2]])
    print(csvTable)
    os.remove("pythonProjects\\csvJsonPro\\student.csv")

# Converts the CSV to JSON
def convertToJSON():
    if os.path.isfile("pythonProjects\\csvJsonPro\\student.csv"):    
        with open("pythonProjects\\csvJsonPro\\student.csv", "r+") as csvFile:
            csvContents = csv.reader(csvFile, delimiter=",")
            next(csvContents)
            with open("pythonProjects\\csvJsonPro\\students.json", "r+") as jsonFile:
                jsonContents = json.load(jsonFile)
                for row in csvContents:
                    fileRow = {
                        "Name": row[0],
                        "Certification": row[1],
                        "Year": row[2]
                    }
                    jsonContents["students"].append(fileRow)
                jsonFile.seek(0)
                json.dump(jsonContents, jsonFile, indent="    ")
    else:
        print("Write to CSV File!")
        return


# Creates a temp CSV file if there isn't one. Opens the JSON and converts it each entry into a CSV record
def jsonToCSV():
    if os.path.isfile("pythonProjects\\csvJsonPro\\student.csv"):
        convertToJSON()
    with open("pythonProjects\\csvJsonPro\\students.json", "r") as jsonFile:
        jsonContent = json.load(jsonFile)
        jsonLength = len(jsonContent['students'])
        with open("pythonProjects\\csvJsonPro\\student.csv", "w") as csvFile:
            writer = csv.writer(csvFile, delimiter=",", lineterminator="\n")
            for i in range(jsonLength):
                name = f"{jsonContent['students'][i]['Name']}"
                cert = f"{jsonContent['students'][i]['Certification']}"
                year = f"{jsonContent['students'][i]['Year']}"
                writer.writerow([name,cert,year])

# Gets a CSV input at makes a temp CSV file, Displays a json, inserts CSV into the students.json file
def main():
    while True:
        userChoice = input("1) Enter CSV Record \n2) Display CSV \n3) Convert CSV to JSON \n0) Exit \nPlease pick an option: ")
        try:
            userChoice = int(userChoice)
            if userChoice not in [1,2,3,0]:
                raise
        except:
            while userChoice not in [1,2,3,0]:
                userChoice = input("Enter a correct choice: ")
                try:
                    userChoice = int(userChoice)
                except:
                    print("Enter a number!")
        if userChoice == 1:
            name = input("Enter Name: ")
            certification = input("Enter Certification: ")
            year = input("Enter Year: ")
            insertCSV(name, certification, year)
        elif userChoice == 2:
            displayCSV()
        elif userChoice == 3:
            convertToJSON()
            if os.path.isfile("pythonProjects\\csvJsonPro\\student.csv"):
                os.remove("pythonProjects\\csvJsonPro\\student.csv")
        elif userChoice == 0:
            break
        keyBoardHit()

if __name__ == "__main__":
    main()