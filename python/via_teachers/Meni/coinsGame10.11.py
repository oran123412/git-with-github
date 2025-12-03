MIN_CELLS = 10
MAX_CELLS = 30
NUM_COINS = 4



def print_welcome_message() -> None:
    print("Welcome all") 


def get_cellnum() -> int :
    cellnum=int(input("Enter the number of cell's: "))
    while cellnum<MIN_CELLS or cellnum>MAX_CELLS:
        cellnum=int(input("Enter the number of cell's between 10 to 30: "))
    return cellnum

def place_coins(cellnum: int) -> list[int] :
    coins=[]
    for i in range(4):    
        coin=int(input("enter the cells which the coins are at: "))
        while (len(coins) > 0 and coin <= coins[-1]) or coin > cellnum or coin < 1 or coin in coins:
             coin=int(input("your numbers need to be only raising and never the same and not bigger than you table: "))
        coins.append(coin)
    return coins
        
        
def draw_board(coins: list[int], cellnum: int) -> None:
    for i in range(1, cellnum + 1):
        if i in coins:
            print("|🪙  |", end="")
        else:
            print("|⬛ |", end="")
    print()
    print("Coin positions:", coins)   # ← תיקון קטן וחשוב



def gameover(coins: list[int]) -> bool:
    for i in range(len(coins)):
        if coins[i] > 1 and (i == 0 or coins[i] - 1 > coins[i-1]):
            return False
    return True


def make_move(coins: list[int], num_player: int) -> None :
    while True:
        coin_index=int(input("Which coin do you want to move? "))
        number_of_moves=int(input("How many steps do you want to make? "))

        if coin_index < 0 or coin_index >= len(coins):
            print("Invalid coin index.")
            continue

        new_pos = coins[coin_index] - number_of_moves

        if new_pos < 1:
            print("Can't move outside the board.")
            continue

        if new_pos in coins:
            print("Can't move onto another coin.")
            continue
        
        for other in coins:
            if other != coins[coin_index] and new_pos < other < coins[coin_index]:
                print("Can't jump over another coin.")
                break
        else:
            coins[coin_index] = new_pos
            coins.sort()
            break



def print_game_summary(winner: int) -> None :
    print(f'The winner is {winner} ')

def draw_line(length: int) -> None :
    print("-"*length)


def main():
    num_player = 1
    coins=[]
    print_welcome_message()
    cellnum = get_cellnum()
    coins = place_coins(cellnum)
    draw_board(coins, cellnum)
    draw_line(cellnum)

    while not gameover(coins):
        print(f"Player {num_player}'s turn")   # ← תוספת חשובה
        make_move(coins, num_player)
        draw_board(coins, cellnum)
        draw_line(cellnum)
        num_player = 3 - num_player 
    print_game_summary(3 - num_player)
    
main()


