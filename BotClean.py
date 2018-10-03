#!/usr/bin/python

# Head ends here

def next_move(posr, posc, board):
    cur_i,cur_j = dirty_pos(board)
    if posr > cur_i:
        print('UP')
    elif posr < cur_i:
        print('DOWN') 
    else:
        if posc > cur_j:
            print('LEFT') 
        elif posc < cur_j:
            print('RIGHT') 
        else:
            print('CLEAN')
    #print("")

# Function to know the position of dirty block
def dirty_pos(board):
    for i in range(5):
        for j in range(5):
            if board[i][j] == 'd':
                return [i,j]

# Tail starts here

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)
