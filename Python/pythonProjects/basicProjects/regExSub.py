import re

# Uses the regex.sub function to substitute "a" into "@" and "o" into "0".
def changeString(choice):
    subA = re.sub("a", "@",choice)
    subO = re.sub("o", "0", subA)
    print(subO)

# Gets a string from a user then passes it to the changeString Function
def main():
    choice = input("String: ")
    changeString(choice)

if __name__ == "__main__":
    main()