#r = read, w = write, b = binary, a = append
workFile = open("Python Gmetrix Course\\file-handling\\hello.txt", "r") 
workFileContents = workFile.read()
print(workFileContents)
workFile.close() # Must have an open and close unless you have with