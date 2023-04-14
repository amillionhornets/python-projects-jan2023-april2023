import os
if os.path.isfile('file-handling/bye.txt'):
    os.remove('file-handling/bye.txt')
    print('\"bye.txt\" has been removed')
else:
    print("There is no file to remove. Creating \"bye.txt\"")
    file = open('file-handling/bye.txt', "w")
    file.write("goodbye")
    file.close()