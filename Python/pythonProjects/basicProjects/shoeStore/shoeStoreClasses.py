import csv

class record:
    def __init__(self, desc, quantity, listPrice):
        self.desc = desc
        self.quantity = quantity
        self.listPrice = listPrice
    def getRetailPrice(self,quantity, listPrice):
        if quantity < 50:
            return listPrice * 1.5
        elif quantity < 100:
            return listPrice * 2
        elif quantity == 100 or quantity < 500:
            return listPrice * 2.25
        elif quantity == 500 or quantity < 1000:
            return listPrice * 3
        else:
            return listPrice * 5

def main():
    print("Item Description: ", end="")
    itemDesc = input()
    print("Quantity: ", end="")
    quantity = int(input())
    print("List Price: ", end="")
    listPrice = float(input())
    row = record(itemDesc,quantity,listPrice)
    retailPrice = round(row.getRetailPrice(row.quantity, row.listPrice), 2)
    with open("basicProjects\\shoeStore\\records.csv", "a") as csvFile:
        writer = csv.writer(csvFile, delimiter=",",lineterminator="\n")
        writer.writerow([row.desc,row.quantity,row.listPrice,retailPrice])
        
if __name__ == "__main__":
    main()