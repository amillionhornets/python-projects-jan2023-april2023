import os
if os.path.isfile('file-handling/hello.txt'):
    writeFile = open("file-handling/hello.txt", "a")
else:
    writeFile = open("file-handling/hello.txt", "w")
log = input("Say Hi: ")
writeFile.write("\n" + str(log))
writeFile.close()