def empty_places(board):
    empty_list = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                empty_list.append((i,j))
    return empty_list

    