from functions import *

def tic_tac_toe():
    board = empty_board()
    winner = 0
    counter = 1
    print(board)
    sleep(5)
    
    while winner == 0:
        for player in [1, 2]:
            brd = random_place(board, player)
            print("Board After "+ str(counter) + "moves")
            print(brd)
            sleep(5)
            counter += 1
            winner = evaluate_game(brd)
            
            if winner != 0:
                break
    return winner

print("Winner is player: "+ str(tic_tac_toe()))
            
