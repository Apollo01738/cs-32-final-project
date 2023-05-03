import random


current_player = "X"
winner = None
gameRunning = True

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
connectors = "------"




def BoardInitialize(board): 
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(connectors)
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(connectors)
    print(board[6] + "|" + board[7] + "|" + board[8])


def Input(board):
    while True:
        playerInput = int(input(f"Please chose a number between 1 and 9: Player {current_player}:"))
        if playerInput <= 9 and playerInput >= 1 and board[playerInput-1] == "-":
            board[playerInput-1] = current_player
            break

        elif playerInput >= 9  or (not playerInput):
            print("Please input a number between 1 and 9")
        elif board[playerInput-1] != "-" or playerInput == "O" or playerInput == "X":
            print("Someone has already chosen that spot! Please pick a different number between 1 and 9")



def horizontal(board):
    global winner
    if "-" != board[0] == board[1] == board[2]:
        winner = board[2]
        return True
    elif "-" != board[3] == board[4] == board[5]:
        winner = board[5]
        return True
    elif "-" != board[6] == board[7] == board[8]:
        winner = board[8]
        return True

    
def vertical(board):
    global winner
    if "-" != board[0] == board[3] == board[6]:
        winner = board[6]
        return True
    elif "-" != board[1] == board[4] == board[7]:
        winner = board[7]
        return True
    elif "-" != board[2] == board[5] == board[8]:
        winner = board[8]
        return True
        
    
def diagonal(board):
    global winner
    if "-" != board[0] == board[4] == board[8]:
        winner = board[8]
        return True
    elif "-" != board[6] == board[4] == board[2]:
        winner = board[2]
        return True



def changeOpponent():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"

def tie(board):
    global gameRunning
    if "-" not in board and checkWin() == False:
        BoardInitialize(board)
        print("It's a tie")
        gameRunning = False


def checkWin():
    global gameRunning
    won = False
    if horizontal(board) or vertical(board) or diagonal(board):
        gameRunning = False
        BoardInitialize(board)
        if winner == "X":
            print("Yay! Player", winner , "has won this round!")
            won = True
        if winner == "O":
            print("Darn! Player", winner , "has won this round! You lost ((")
            #BoardInitialize(board)
    return won


def automated(board):
    global current_player
    while current_player == "O":
        computer = random.randint(0, 8)
        if board[computer] == "-":
            board[computer] = "O"
            break



def endgame():
    global board
    global current_player
    replay = False
    if gameRunning == False:
        while True:
            try:
                board = ["-", "-", "-",
                         "-", "-", "-",
                         "-", "-", "-"]
                current_player = "X"
                print('1. Play again')
                print('2. Return to main menu')
                hangman_option = input('Enter your selection:')
                if hangman_option == "1":
                    replay = True
                    break
                elif hangman_option == "2":
                    replay = False
                    break
                else:
                    raise ValueError()
            except ValueError:
                print("Please choose either '1' or '2'")
    return replay



def tictactoe_main1():
    global gameRunning
    gameRunning = True
    while gameRunning:
        BoardInitialize(board)
        Input(board)
        won = checkWin()
        tie(board)
        changeOpponent()
    
        if gameRunning:
            automated(board)
            checkWin()
            tie(board)
            changeOpponent()
    replay = endgame()
    return won, replay
    #BoardInitialize(board)


if __name__ == '__main__':
    tictactoe_main1()
    

