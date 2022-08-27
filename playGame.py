from curses.ascii import isdigit
import math
from boardManagement import *
import sys
import pygame
from c4_AI import *

def save_game(pvp, turn, board):
    f = open("saved_game.txt", "w+")
    print(pvp, file=f)
    print(turn, file=f)
    print(board, file=f)
    f.close()

def load_game():
    f = open("saved_game.txt", "r")
    try:
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
        p_board = np.array(p_board)
        if is_terminal_node(p_board):
            print('terminal')
            p_board = []
    except:
        return -1, -1, []
    return pvp, turn, p_board

def playC4(pvp=1, curr=1, init_board=[]):
    GAMEOVER = False
    turn = curr
    if init_board==[]:
        board = makeBoard()
    else:
        board = init_board
    print(board)
    draw_board(board, screen)
    moves = []
    while True:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                save_game(pvp, turn, board)
                sys.exit()

            if event.type == pygame.MOUSEMOTION and not GAMEOVER:
                posX = event.pos[0]
                pygame.draw.rect(screen, BLACK, (0, 0, W*SQUARE_LEN, SQUARE_LEN))
                if turn == 1:
                    pygame.draw.circle(screen, RED, (posX, SQUARE_LEN//2), RADIUS)
                elif pvp == 1 and turn==2:
                    pygame.draw.circle(screen, YELLOW, (posX, SQUARE_LEN//2), RADIUS)
            pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button==3:
                    print('stack:', moves)
                    if len(moves)!=0:
                        undo_move(board, moves.pop())
                        draw_board(board, screen)
                        if turn==1: turn=2
                        else: turn=1

                if event.button==1 and not GAMEOVER:
                    print(event.pos)
                    print("down")
                    if turn==1:
                        col = int(math.floor(event.pos[0]/SQUARE_LEN))
                    elif pvp==0 and turn==2:
                        show_msg("AI's Turn", screen)
                        col, minimax_score = minimax(board, 5, -math.inf, math.inf, True)
                    elif pvp==1 and turn==2:
                        col = int(math.floor(event.pos[0]/SQUARE_LEN))
                    row = dropPiece(board, col, turn)
                    if row == -1:
                        print('cannot make move here, try again')
                        continue
                    draw_board(board, screen)
                    moves.append(col)
                    print(board)
                    if checkWin(board, col, row, turn)==True: 
                        print("player "+str(turn)+" has won!")
                        GAMEOVER = True
                        show_msg("Player "+str(turn)+" has won!", screen, (YELLOW,RED)[turn==1])
                        continue
                    if turn==1: turn=2
                    else: turn=1
                    
                if turn == 1:
                        pygame.draw.circle(screen, RED, (posX, SQUARE_LEN//2), RADIUS)
                elif pvp == 1 and turn==2:
                    pygame.draw.circle(screen, YELLOW, (posX, SQUARE_LEN//2), RADIUS)
                pygame.display.update()


# graphics()
def start():
    choice = main_menu(screen)
    if choice==1:
        playC4(pvp=1)
    elif choice==2:
        playC4(pvp=0)
    elif choice==3:
        print('hello')
        pvp, turn, init_board=load_game()
        print(init_board)
        if init_board!=[]:
            playC4(pvp, turn, init_board)
        else:
            start()
    else:
        print(choice)

screen = board_graphics_init()
pygame.display.set_caption('Connect4')
start()


# undo in continue
# config file