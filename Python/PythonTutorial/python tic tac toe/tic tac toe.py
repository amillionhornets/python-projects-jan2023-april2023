from tkinter import *

#Changes the turn and checks to find a winner
def nextTurn(row, column):
    global player
    if buttons[row][column]['text'] == "" and checkWinner() is False:
        if player == players[0]:
            buttons[row][column]['text'] = player
            if checkWinner() is False:
                player = players[1]
                label.config(text=(players[1]+"'s turn"))
            elif checkWinner() is True:
                label.config(text=(players[0]+" wins"))
            elif checkWinner() == "Tie":
                label.config(text=("Tie"))
        else:
            buttons[row][column]['text'] = player
            player = players[0]
            if checkWinner() is False:
                label.config(text=(players[0]+"'s turn"))
            elif checkWinner() is True:
                label.config(text=(players[1]+" wins"))
            elif checkWinner() == "Tie":
                label.config(text=("Tie"))
            
                
#Checks for a winner or a tie
def checkWinner():
    global player
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True
    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg="green")
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")
            return True
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True
    elif emptySpaces() is False:
        for row in range(3):
            for column in range(3):
                label.config(text=("Tie!"))
                buttons[row][column].config(bg="yellow")
        return "Tie"
    else:
        return False
    
    
#Finds all the empty spaces
def emptySpaces():
    spaces = 9
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -=1
    if spaces == 0:
        return False
    else:
        return True
#On reset button click, starts a new game
def newGame():
    global player
    player = player[0]

    label.config(text=(player + "'s turn"))
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="#F0F0F0")

#Defines the app, player, and board.
window = Tk()
window.title("Tic Tac Toe")
players = ["X", "O"]
player = players[0]
buttons = [[0,0,0], #Multidimensional list representing the board
           [0,0,0],
           [0,0,0]]

label = Label(text= player + "'s turn", font=('console',40))
label.pack(side="top")

resetBut = Button(text="restart", font=("console",20), command=newGame)
resetBut.pack(side="top")

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="",font=('consolas', 40), width = 5, height=2,
                        command= lambda row=row, column=column: nextTurn(row, column))
        buttons[row][column].grid(row=row, column=column)

window.mainloop()