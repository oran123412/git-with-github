# ============================== Tic Tac Toe ==============================

board=["1","2","3","4","5","6","7","8","9"]
count = 0

def display_board(board):
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")

def player_input(board,player):
    cell_number=int(input(f"Player {player}, choose a number (1-9): "))
    while not 1 <= cell_number <= 9 or board[cell_number-1] in ["X","O"]:
        cell_number=int(input("Invalid choice, choose an empty cell (1-9): "))
    board[cell_number-1] = player

def check_winner(board):
    # שורות
    if board[0] == board[1] == board[2]: return board[0]
    if board[3] == board[4] == board[5]: return board[3]
    if board[6] == board[7] == board[8]: return board[6]
    # עמודות
    if board[0] == board[3] == board[6]: return board[0]
    if board[1] == board[4] == board[7]: return board[1]
    if board[2] == board[5] == board[8]: return board[2]
    # אלכסונים
    if board[0] == board[4] == board[8]: return board[0]
    if board[2] == board[4] == board[6]: return board[2]
    return None

def get_player_turn():
    global count
    player = "X" if count % 2 == 0 else "O"
    count += 1
    return player

def reset_game():
    global board, count
    board = ["1","2","3","4","5","6","7","8","9"]
    count = 0

def play_game():
    display_board(board)

    while True:
        player = get_player_turn()
        player_input(board, player)
        display_board(board)

        winner = check_winner(board)
        if winner:
            print(f"Player {winner} wins! 🎉")
            break

        # תיקו
        if all(cell in ["X", "O"] for cell in board):
            print("It's a tie! 🤝")
            break

    # לשחק שוב
    again = input("Play again? (y/n): ").lower()
    if again == "y":
        reset_game()
        play_game()
    else:
        print("Thanks for playing! 👋")

play_game()
