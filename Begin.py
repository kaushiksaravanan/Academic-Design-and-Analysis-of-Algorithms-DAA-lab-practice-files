# Begin
#    if all columns are filled, then
#       return true
#    for each row of the board, do
#       if isValid(board, i, col), then
#          set queen at place (i, col) in the board
#          if solveNQueen(board, col+1) = true, then
#             return true
#          otherwise remove queen from place (i, col) from board.
#    done
#    return false
# End

n=4
board=[['-' for i in range(n)] for i in range(n)]
print(board)
def fill(n,col):
    if col>=n:

        # To print all possible solutions
        # print('-----------')
        # for i in board:
        #     print(*i)
        return True
    for i in range(n):
        if isvalid(board,n,i,col):
            board[i][col]='Q'
            if fill(n,col+1)==True:
                return True
            else:
                board[i][col]='-'

    #To show backtracking
    # print('-----------')
    # for i in board:
    #     print(*i)
    # return False

def isvalid(board,N,row,col):
    for i_ in range(col):
        if board[row][i_]=='Q':
            return False

    #check diagonal
    for i, j in zip(range(row, -1, -1),range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False
    for i, j in zip(range(row, N, 1),range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False
    return True

try:    
    fill(4,0)
except:
    print('Not possible')
print(board)
for i in board:
    print(*i)