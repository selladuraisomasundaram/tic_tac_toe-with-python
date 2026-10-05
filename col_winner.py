def col_winner(board, player):
    for x in range(len(board)):
        
        win = True
        
        for y in range(len(board)):
            if board[y, x] != player:
                win = False
                continue
            
        if win is True:
            return win
    return win


    