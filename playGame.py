from curses.ascii import isdigit
import math
from boardManagement import *
import sys
import pygame

def save_game(pvp, turn, board):
    f = open("saved_game.txt", "w+")
    print(pvp, file=f)
    print(turn, file=f)
    print(board, file=f)
    f.close()

def load_game():
    f = open("saved_game.txt", "r")
    pvp = int(f.readline())
    turn = int(f.readline())
    board = f.read()
    x = []
    p_board = []
    for i in range(len(board)):
        ch = board[i]
        if isdigit(ch):
            x.append(int(ch))
            if len(x)==7:
                p_board.append(x)
                x = []
                
    return pvp, turn, np.array(p_board)

def playC4(pvp=1, curr=1, init_board=[]):
    GAMEOVER = False
    turn = curr
    if init_board==[]:
        board = makeBoard()
    else:
        board = init_board
    print(board)
    draw_board(board, screen)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_game(pvp, turn, board)
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN and not GAMEOVER:
                print(event.pos)
                print("down")
                col = int(math.floor(event.pos[0]/SQUARE_LEN))

                row = dropPiece(board, col, turn)
                if row == -1:
                    print('cannot make move here, try again')
                    continue
                draw_board(board, screen)
                print(board)
                if checkWin(board, col, row, turn)==True: 
                    print("player "+str(turn)+" has won!")
                    GAMEOVER = True
                    show_msg("Player "+str(turn)+" has won!", screen)
                if turn==1: turn=2
                else: turn=1


# graphics()
screen = board_graphics_init()
pygame.display.set_caption('Connect4')
choice = main_menu(screen)
if choice==1:
    playC4(1)
elif choice==2:
    playC4(0)
elif choice==3:
    print('hello')
    pvp, turn, init_board=load_game()
    playC4(pvp, turn, init_board)
else:
    print(choice)


