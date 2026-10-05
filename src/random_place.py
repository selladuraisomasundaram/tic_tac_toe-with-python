import random as rd
from empty_places import empty_places

def random_place(board, player):    
    select = empty_places(board)
    current_location = rd.choice(select)
    board[current_location] = player
    return board
    