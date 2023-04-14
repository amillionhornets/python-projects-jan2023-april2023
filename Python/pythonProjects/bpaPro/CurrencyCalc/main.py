from math import floor
# Each of these functions convert the starting currency to the other three
def convertToDollars(currency, amount):
    if currency == "euros":
        return round(amount / .84, 2)
    elif currency == "pounds":
        return round(amount / .76, 2)
    elif currency == "yen":
        return round(amount / 104.53, 2)

def convertToPounds(currency, amount):
    if currency == "euros":
        return round((amount / .84) * .76, 2)
    elif currency == "dollars":
        return round(amount * .76, 2)
    elif currency == "yen":
        return round((amount / 104.53) * .76, 2)
    
def convertToEuros(currency, amount):
    if currency == "pounds":
        return round((amount / .76) * .84, 2)
    elif currency == "dollars":
        return round(amount * .84, 2)
    elif currency == "yen":
        return round((amount / 104.53) * .84, 2)
    
def convertToYen(currency, amount):
    if currency == "euros":
        return round((amount / .84) * 104.53, 2)
    elif currency == "dollars":
        return round(amount * 104.53, 2)
    elif currency == "pounds":
        return round((amount / .76) * 104.53, 2)

# Finds the min amount of US Dollar bills it would take to fufill the transfer  
def findMinDollar(dollarTotal):
    dollarAmt = floor(dollarTotal)
    hundredAmt = 0
    fiftyAmt = 0
    twentyAmt = 0
    tenAmt = 0
    fiveAmt = 0
    oneAmt = 0
    while dollarAmt > 0:
        if dollarAmt - 100 >= 0:
            hundredAmt+=1
            dollarAmt-=100
        elif dollarAmt - 50 >= 0:
            fiftyAmt+=1
            dollarAmt-=50
        elif dollarAmt - 20 >= 0:
            twentyAmt+=1
            dollarAmt-=20
        elif dollarAmt - 10 >= 0:
            tenAmt+=1
            dollarAmt-=10
        elif dollarAmt -5 >= 0:
            fiveAmt+=1
            dollarAmt-=5
        elif dollarAmt - 1 >= 0:
            oneAmt+=1
            dollarAmt-=1
    print(f"Min USD Bills: \n $100: {hundredAmt} \n $50: {fiftyAmt} \n $20: {twentyAmt} \n $10: {tenAmt}\n $5: {fiveAmt} \n $1 {oneAmt}")

# Gets the currency from the user and converts it to the other three and return the min dollar amount
def main():
    while True:
        print("Start with Dollars, Pounds, Euros, Yen, or Quit: ", end="")
        startCurrency = input().lower()
        if startCurrency == "quit":
            break
        print("Amount: ", end="")
        startAmt = input()
        try:
            startAmt = float(startAmt)
        except:
            print("Enter valid Number")
            continue
        startAmt = round(startAmt, 2)
        if startCurrency == "dollars":
            print(f"Dollars: {startAmt}")
            print(f"Pounds: {convertToPounds(startCurrency, startAmt)}")
            print(f"Euros: {convertToEuros(startCurrency, startAmt)}")
            print(f"Yen: {convertToYen(startCurrency, startAmt)}")
            findMinDollar(startAmt)
        elif startCurrency == "pounds":
            print(f"Dollars: {convertToDollars(startCurrency, startAmt)}")
            print(f"Pounds: {startAmt}")
            print(f"Euros: {convertToEuros(startCurrency, startAmt)}")
            print(f"Yen: {convertToYen(startCurrency, startAmt)}")
            findMinDollar(convertToDollars(startCurrency, startAmt))
        elif startCurrency == "euros":
            print(f"Dollars: {convertToDollars(startCurrency, startAmt)}")
            print(f"Pounds: {convertToPounds(startCurrency, startAmt)}")
            print(f"Euros: {startAmt}")
            print(f"Yen: {convertToYen(startCurrency, startAmt)}")
            findMinDollar(convertToDollars(startCurrency, startAmt))
        elif startCurrency == "yen":
            print(f"Dollars: {convertToDollars(startCurrency, startAmt)}")
            print(f"Pounds: {convertToPounds(startCurrency, startAmt)}")
            print(f"Euros: {convertToEuros(startCurrency, startAmt)}")
            print(f"Yen: {startAmt}")
            findMinDollar(convertToDollars(startCurrency, startAmt))
        else:
            print("Enter a valid currency")
            continue
        
if __name__ == "__main__":
    main()