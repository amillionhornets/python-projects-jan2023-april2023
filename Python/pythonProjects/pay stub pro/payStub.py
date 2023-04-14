import re
import json
from payroll import payRoll

#checks to make sure letters are letters
def validateLetters(fname):
    return any(char.isdigit() for char in fname)

# Makes sures the numbers are valid numbers ie not string
def validateNumbers(numbers):
    pattern = "[0-9]"
    zipSplit = []
    for num in numbers:
        if num == "-":
            continue
        zipSplit.append(num)
    for number in zipSplit:
        if len(zipSplit) == 9:
            if(re.search(pattern, number)):
                continue
            else:
                return False
        else:
            return False
    return True

# Only displays the last 4 numbers in SSN
def lastFour(ssNum):
    numberList = []
    lastDigits = []
    for num in ssNum:
        if num == "-":
            continue
        numberList.append(num)
    for i in range(-4, 0, 1):
        lastDigits.append(str(numberList[i]))
    number = ""
    for item in lastDigits:
        number += str(item)
    return number

def main():
    # Asks the user for the first name and validate there are no nums in it
    fname = input("First Name: ")
    while(validateLetters(fname)):
        print("Input a valid first name.")
        fname = input("First Name: ")
    # Asks the user for the last name and validate there are no nums in it
    lname = input("Last Name: ")
    while(validateLetters(lname)):
        print("Input a valid first name.")
        lname = input("First Name: ")
    # Ask the user for SSN
    ssn = input("Enter your SSN: ")
    while(validateNumbers(ssn) != True):
        print("Enter a valid social security number")
        ssn = input("Enter your SSN: ")

    # Asks the user for their grosspay and validates it
    userHoursWorked = input("Hours Worked: ")
    while(validateLetters(userHoursWorked) != True):
        userHoursWorked = input("Hours Worked: ")
    userHourlyPay = input("Hourly Pay: ")
    while(validateLetters(userHourlyPay) != True):
        userHourlyPay = input("Hourly Pay: ")

    grossPay = payRoll(int(userHoursWorked), int(userHourlyPay))
    SSA = round((grossPay * 0.124), 2)
    medicare = round(((grossPay - SSA) * 0.029), 2)
    lastDigits = lastFour(ssn)
    print(f"{fname} {lname} XXX-XX-{lastDigits}, made {grossPay} this year! Social Security Tax: {SSA} and Medicare Tax: {medicare}")

if __name__ == "__main__":
    main()







"""
UNFINISHED CODE BELOW
"""

# def checkGrossPay(grossPay):
#     try:
#         grossPay = float(grossPay)
#     except:
#         while type(grossPay) != int or type(grossPay) != float:
#             print("You must enter a number.")
#             grossPay = float(input("Gross Pay: "))
#             try:
#                 grossPay = float(grossPay)
#             except:
#                 continue
            
#     return True



# def checkAdd(address):
#     pattern = "[a-zA-Z0-9]"
#     splitAdd = []
#     for letter in address:
#         if letter == " ":
#             continue
#         splitAdd.append(letter)
#     for item in splitAdd:
#         if(re.search(pattern, item)):
#             continue
#         else:
#             print("Input a Vaild Address.")
#             return False
#     return True

# def validateState(userState):
#     row = 0
#     with open("python projects\\pay stub pro\\states.json", "r") as jsonFile:
#         data = json.load(jsonFile)
#         for state in data:
#             if(data[row]["name"] == userState):
#                 return True
#             elif(data[row]["abbreviation"] == userState):
#                 return True
#             row+=1
#         return False

    # # Asks the user for their address and validates it
    # address = input("Address: ")
    # while(checkAdd(address) != True):
    #     address = input("Address: ")

    # # Asks the user to input their city and validates it
    # city = input("City: ")
    # while(checkNums(city)):
    #     print("Input a valid city!")
    #     city = (input("City: "))

    # # Asks the user to input their state and validates it through a json file
    # state = input("State: ")
    # while validateState(state) != True:
    #     print("Input a valid state or abbreviation")
    #     state = input("State: ")

    # # Asks the user to input their zip code and makes sure it is only numbers.
    # zipCode = input("ZIP Code: ")
    # while validateZip(zipCode) != True:
    #     print("Invalid ZIP Code.")
    #     zipCode = input("Zip Code: ")
