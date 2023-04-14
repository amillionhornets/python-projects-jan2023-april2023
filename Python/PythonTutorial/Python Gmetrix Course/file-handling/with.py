with open("file-handling/hello.txt", "a") as file:
    fLog = input("Write to this file: ")
    file.write("\n" + fLog)