import numpy as np
from row_winner import row_winner
from col_winner import col_winner
from diag_winner import diag_winner

def evaluate_game(board):
    winner = 0
    for player in [1,2]:
        if (row_winner(board, player) or col_winner(board, player) or diag_winner(board, player)):
            
            winner = player
        
    if np.all(board != 0) and winner == 0:
        winner = -1
        
    return winner
            