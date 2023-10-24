# Prog-11: Tetris
# Fill in your ID & Name
# ...
# Declare that you do this by yourself

import pygame
import copy
import random

def make_shape(): 
    shape = [[[1,1,1],[1,0,0]], [[2,2,2],[0,0,2]], [[3,3,3],[0,3,0]], [[4,4,4,4]], [[5,5,0],[0,5,5]], [[6,0],[6,6],[0,6]], [[7,7],[7,7]]]
    return shape[random.randrange(len(shape))]

def show_text(x,y,size,text,screen):
    text_surface = pygame.font.Font(pygame.font.match_font('arial'), size).render(text, True, (255,255,255))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    screen.blit(text_surface, text_rect)

def top(board):
    row = min([i for i in range(len(board)) if board[i]!=[0]*len(board[0])],default=0)-1
    return 60*(2+(row-1)//6) if row>6 else 120

def scoring(board):
    count = len([i for i in board if 0 not in i])
    return 50*count*(count-1)*max(1,(count-2)) if count>1 else 40*count

def pgame():
    width,height,FPS = 480,720,60
    all_color = [(255,128,0),(0,0,255),(255,0,255),(0,255,255),(255,0,0),(0,255,0),(255,255,0)]
    board = [[0]*10 for i in range(23)]
    shape = make_shape()
    score,time,end,column = 0,0,0,0
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((width,height))
    pygame.display.set_caption("ComProg-10: Tetris")

    while end == 0:
        screen.fill((0,0,0))
        time_cap = top(board)
        clock.tick(FPS)
        frame = [board]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    frame = animate_drop(shape,board,column)
                    if len(frame)!=0:
                        score += scoring(frame[-1])
                        frame = frame + animate_clear(frame[-1])
                        board = frame[-1]
                        shape = make_shape()
                        column,time = 0,0
                    else:
                        end = 1
                elif event.key == pygame.K_LEFT:
                    column = column-1 if column>0 else column
                elif event.key == pygame.K_RIGHT:
                    column = column+1 if column<len(board[0])-len(shape[0]) else column
                elif event.key == pygame.K_z:
                    shape = rotateL(shape)
                    column = min(column,len(board[0])-len(shape[0]))
                elif event.key == pygame.K_x:
                    shape = rotateR(shape)
                    column = min(column,len(board[0])-len(shape[0]))
        time+=1
        if time >= time_cap:
            frame = animate_drop(shape,board,column)
            if len(frame)!=0:
                score += scoring(frame[-1])
                frame = frame + animate_clear(frame[-1])
                board = frame[-1]
                shape = make_shape()
                column,time = 0,0
            else:
                end = 1
        for i in frame:
            screen.fill((0,0,0))
            clock.tick(FPS)
            board_row, board_column = len(i), len(i[0])
            shape_row, shape_column = len(shape), len(shape[0])
            for j in range(shape_row):
                for k in range(shape_column):
                    if shape[j][k]!=0:
                        pygame.draw.rect(screen,all_color[shape[j][k]-1],[30+column*24+k*24,20+j*24,20,20],0)
            for j in range(board_row):
                for k in range(board_column):
                    if i[j][k]!=0:
                        pygame.draw.rect(screen,all_color[i[j][k]-1],[30+k*24,124+j*24,20,20],0)
            for i in range(board_column+1):
                if i >= column and i <= column + shape_column:
                    pygame.draw.line(screen,(255,255,255),[28+i*24,672],[28+i*24,116],3)
                else:
                    pygame.draw.line(screen,(128,128,128),[28+i*24,672],[28+i*24,116])
            show_text(380,120,50,"TIME",screen)
            show_text(380,500,50,"SCORE",screen)
            show_text(240,685,15,"Z/X for rotating      Right/Left Arrow Key for moving      Spacebar for dropping",screen)
            pygame.display.flip()
        show_text(380,180,150,str(time//60)+"."+str((time//6)%10),screen)
        show_text(380,550,75,str(score),screen)
        pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pygame.quit()
                    return 
        screen.fill((0,0,0))
        show_text(240,150,50,"TOTAL SCORE",screen)
        show_text(240,250,250,str(score),screen)  
        show_text(240,550,25,"press enter to exit the game",screen) 
        pygame.display.flip()

#-------------------------------------------------------

def rotateR(shape):
    result = []
    for i in range(len(shape[0])):
        m = []
        for j in range(len(shape)-1,-1,-1) :
            m.append(shape[j][i])
        result.append(m)
    return result

def rotateL(shape):
    result = []
    for i in range(len(shape[0])-1,-1,-1):
        m = []
        for j in range(len(shape)) :
            m.append(shape[j][i])
        result.append(m)
    return result
    

def animate_drop(shape, board, c):
    a = []
    for i in range(len(board)-len(shape)+1) :
        boards = copy.deepcopy(board) 
        for j in range(len(shape)-1,-1,-1) :
            for k in range(len(shape[0])) :
                if shape[j][k] != 0 :
                    if k+c >= len(boards[0]) :
                        return a
                    if boards[j+i][k+c] == 0 :
                        boards[j+i][k+c] = shape[j][k]
                    else :
                        return a
        a.append(boards)    
    return a

def animate_clear(board):
    alle=[]
    boards=copy.deepcopy(board)
    b = 0
    for i in range(len(board)):
        if 0 not in board[i] :
            boards[i] = [0 for e in range(len(board[i]))]
            b = i
    if b == 0 :
        return []
    alle.append(boards)
    while True :
        board2 = copy.deepcopy(boards)
        for j in range(len(boards)-1,0,-1):
            if board2[j]==[0 for e in range(len(board[i]))]:
                x=board2.pop(j)
                board2.insert(j-1,x)
        if board2 in alle :
            break
        alle.append(board2)
        boards = copy.deepcopy(board2)
    return alle
#----------------------------------------------        

pgame()