board = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
]

def printBoard():
    global board
    b = ""
    for i in board:
        b += "|"
        for o in i:
            if o == 1: b += "⬛"
            elif o == 2: b += "⬜"
            else: b += "  "
        b += "|\n"
    b += "| 1 2 3 4 5 6 7 |\n-----------------"
    print(b)

def placeTile(team, column):
    global board
    column -= 1
    for i in range(6):
        if board[5 - i][column] == 0:
            board[5 - i][column] = team
            return True
    return False

def checkForZeros(fullboard):
    q = 0
    for i in range(6):
        q += fullboard[i].count(0)
    return q

def checkForWinComp(team):
    for i in range(6):
        for o in range(4):
            if board[i][o] == board[i][o + 1] == board[i][o + 2] == board[i][o + 3] == team: return True
    for i in range(3):
        for o in range(7):
            if board[i][o] == board[i + 1][o] == board[i + 2][o] == board[i + 3][o] == team: return True
    for i in range(3):
        for o in range(4):
            if board[i][o] == board[i + 1][o + 1] == board[i + 2][o + 2] == board[i + 3][o + 3] == team: return True
            if board[i + 3][o] == board[i + 2][o + 1] == board[i + 1][o + 2] == board[i][o + 3] == team: return True

winner = 0
printBoard()
while True:
    inp = False
    while not inp:
        try:
            Inp = int(input("Player 1's turn!\nInput a number and press enter."))
            inp = placeTile(1, Inp)
        except:
            print("Bad input, please input a number between 1 and 7.")
    printBoard()
    if checkForWinComp(1):
        winner = 1
        break
    if checkForZeros(board) == 0:
        break
    inp = False
    while not inp:
        try:
            Inp = int(input("Player 2's turn!\nInput a number and press enter."))
            inp = placeTile(2, Inp)
        except:
            print("Bad input, please input a number between 1 and 7.")
    printBoard()
    if checkForWinComp(2):
        winner = 2
        break
    if checkForZeros(board) == 0:
        break

if not winner:
    print("Tie!")
else:
    print("Player " + str(winner) + " wins!")
