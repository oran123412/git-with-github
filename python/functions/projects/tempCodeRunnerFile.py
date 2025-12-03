#                                                                Tic-Tac-Toe
#                                                               ==============

board=["1","2","3","4","5","6","7","8","9"]

def display_board(board):
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")

display_board(board)





def player_input(board,player):
    cell_number=int(input("enter number where to write X/Y: "))
    while not 1<=cell_number<=9 :
        cell_number=int(input("please write a number between 1-9"))
    if player == "X":
        board[cell_number-1]='X'
    else:
        board[cell_number-1]='O'
        
    # return cell_number
    



# def check_winner():
    
# check_winner()
count=0
def play_game():
    global count
    if count%2==0:
        player='X'
    else:
        player='O'
    count+=1
    return player


player=play_game()
player_input(board, player)
display_board(board)