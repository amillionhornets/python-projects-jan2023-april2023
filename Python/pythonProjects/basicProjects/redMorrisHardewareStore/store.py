import csv
import json

def writeToCSV(name, itemPrice, itemQuantity,total):
    filePath ="C:\\Users\\Dylan Clark\\Desktop\\Python\\pythonProjects\\basicProjects\\redMorrisHardewareStore\\records.csv"
    with open(filePath, "a") as csvFile:
        writer = csv.writer(csvFile, delimiter=",", lineterminator="\n")
        writer.writerow([name,itemPrice,itemQuantity,total])
        readCSV()

def readCSV():
    filePath ="C:\\Users\\Dylan Clark\\Desktop\\Python\\pythonProjects\\basicProjects\\redMorrisHardewareStore\\records.csv"
    with open(filePath, "r") as csvFile:
        reader = csv.reader(csvFile, delimiter=",",lineterminator="\n")
        for row in reader:
            print(row)

def writeToJSON(name, itemPrice, itemQuantity, total):
    filePath ="C:\\Users\\Dylan Clark\\Desktop\\Python\\pythonProjects\\basicProjects\\redMorrisHardewareStore\\records.json"
    with open(filePath, "r+") as jsonFile:
        jsonContent = json.load(jsonFile)
        jsonRow = {
            "Name": name,
            "Price": itemPrice,
            "Quantity": itemQuantity,
            "Total": total
        }
        jsonContent.append(jsonRow)
        jsonFile.seek(0)
        json.dump(jsonContent, jsonFile, indent="    ")
        readJson()

def readJson():
    filePath ="C:\\Users\\Dylan Clark\\Desktop\\Python\\pythonProjects\\basicProjects\\redMorrisHardewareStore\\records.json"
    with open(filePath, "r") as jsonFile:
        jsonContent = json.load(jsonFile)
        for i in range(len(jsonContent)):
            print("Name, Price, Quantity, Total")
            print(f"{jsonContent[i]['Name']}, {jsonContent[i]['Price']}, {jsonContent[i]['Quantity']}, {jsonContent[i]['Total']}")

def main():
    print("Item: ", end="")
    itemName = input()
    print("Price: ", end="")
    price = input()
    print("Quantity: ",end="")
    quantity = input()
    print("Would you like to save to CSV or JSON: ", end="")
    fileChoice = input()
    total = round(float(price) * float(quantity), 2)
    if fileChoice.lower() == "csv":
        writeToCSV(itemName, price, quantity, total)
    else:
        writeToJSON(itemName,price,quantity, total)

if __name__ == "__main__":
    main()