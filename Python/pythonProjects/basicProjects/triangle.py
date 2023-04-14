
runs = 7
# Makes a Triangle using two for loops
for i in range(7):
    for x in range(runs):
        print("*",end="")
    print("\r")
    runs-=1

# Reverses the previous triangle using two for loops
for i in range(8):
    for x in range(runs):
        print("*",end="")
    print("\r")
    runs+=1