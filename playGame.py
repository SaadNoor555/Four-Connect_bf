from boardManagement import *

GAMEOVER = False
turn = 1

board = makeBoard()

while not GAMEOVER:
    col = int(input("Player "+ str(turn) +" turn place (0-6):"))
    while(col<0 and col>6):
        print("invalid input, try again")
        col = int(input("Player "+ str(turn) +" turn place (0-6):"))

    dropPiece(board, col, turn)
    print(board)
    if turn==1: turn=2
    else: turn=1