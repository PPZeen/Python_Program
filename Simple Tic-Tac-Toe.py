import random
                     
def main():
    N = int(input('Board size = '))
    board = [["-"]*N for j in range(N)]
    end = False
    print_board(board)
    while(not end):
        print("========== Player Turn ==========")
        player_input(board)
        print_board(board)
        check = check_win(board)
        if(check != "-"):
            if(check == "D"):
                print("############# DRAW ##############")
            else:
                print("\\(^o^)/     YOU WIN !!!     \\(^o^)/")
            break
        print("======== Computer Turn ==========")
        com_fill(board)
        print_board(board)
        check = check_win(board)
        if(check != "-"):
            if(check == "D"):
                print("############# DRAW ##############")
            else:
                print("(;-;)    YOU LOSE!!!    (;-;)")
            break
    print("Game has ended, thanks for playing :D")

def com_fill(board):
    N = len(board)
    new_board = [[x for x in y] for y in board]
    for i in range(N):
        for j in range(N):
            if board[i][j] == "-":
                new_board[i][j] = "O"
                if(check_win(new_board) == "O"):
                    board[i][j] = "O"
                    return
                new_board[i][j] = "X"
                if(check_win(new_board) == "X"):
                    board[i][j] = "O"
                    return
                new_board[i][j] = "-"
    while True:
        i = random.randint(0, N-1)
        j = random.randint(0, N-1)
        if board[i][j] == "-":
            board[i][j] = "O"
            break

def print_board(board):
    N = len(board)
    print(" "*3 , end = "")
    for i in range(N):
        print((str(i+1)+ " "*(3))[:3], end = "")
    print()
    for row in range(N):
        print((str(row+1)+ " "*(3))[:3], end = "")
        for col in range(N):
            print(board[row][col], end = "    ")
        print()

def player_input(board):
    f = False
    while not f:
        try:
            row = int(input("row = "))
            col = int(input("col = "))
            f = fill(board, row, col)
            if (not f):
                print("!!! You can't fill that spot !!!")
                print("---try again---")
        except:
            print("!!! Invalid Input !!!")
            print("---try again---")
#------------------------------------------

def fill(board, r , c):
    if board[r-1][c-1] == "-" :
        board[r-1][c-1] = "X"
        return True
    return False

def check_win(board):
    def win_row(board) :
        N = len(board)
        for i in range(N) :
            s = False
            for j in range(N-1) :
                if board[i][j] == board[i][j+1] : s = True
                else : s = False ; break
            if s == True : return board[i][j+1]
        return s
    def win_cor(board) :
        N = len(board)
        for i in range(N) :
            s = False
            for j in range(N-1) :
                if board[j][i] == board[j+1][i] : s = True
                else : s = False ; break
            if s == True : return board[j+1][i]
        return s
    def win_dia(board) :
        N = len(board)
        s = False
        for i in range(N-1) :
            if board[i][i] == board[i+1][i+1] : s = True
            else : s = False ; break
        if s == True : return board[i+1][i+1]
        else :
            for k in range(N-1,0,-1) :
                if board[N-k-1][k] == board[N-k][k-1] : s = True
                else : return False
        return board[N-k][k-1]
    def aye(board) :
        s = False
        N = len(board)
        for i in range(N) :
            if "X" in board[i] and "O" in board[i] : s = True
            else : return False
        Board = []
        for j in range(N) :
            x = []
            for k in range(N) : x.append(board[k][j])
            Board.append(x)
        k = 0
        for h in range(N) :
            if "X" in Board[h] and "O" in Board[h] : k += 1
        if k < N-1 : return False
        return "D"
    x = win_row(board)
    if x != False : return x
    y = win_cor(board)
    if y != False : return y
    z = win_dia(board)
    if z != False : return z
    a = aye(board)
    if a != False : return "D"
    return "-"        
            
#------------------------------------------

main()