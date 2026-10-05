from functions import *
from empty_board import empty_board

board = empty_board()

def row_winner(board, player):
    for x in range(len(board)):
        win = True
        
        for y in range(len(board)):
            if board[x, y] != player:
                win = False
                continue
        if win is True:
            return win
    return win

print(row_winner(board, 1))