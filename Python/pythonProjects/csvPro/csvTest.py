import csv

# with open("python projects\deniro.csv", "a") as csvFile:
#     denrioWriter = csv.writer(csvFile, delimiter=",", lineterminator="\n")
#     year = int(input("Year: "))
#     rating = int(input("Rating: "))
#     title = input("Title: ")
#     denrioWriter.writerow([year, rating, title])


#Opens the csv file in read mode and prints out all the rows
with open("pythonProjects\\csvPro\\deniro.csv", "r") as csvFile:
    denrioReader = csv.reader(csvFile, delimiter=",")
    next(denrioReader)
    for row in denrioReader:
        print(row)