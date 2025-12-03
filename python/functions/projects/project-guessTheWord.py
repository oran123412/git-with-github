import sys
from random import choice
from english_words import get_english_words_set


if len(sys.argv) > 1:
    word_file = sys.argv[1]
    with open(word_file, "r") as file:
        words = [line.strip() for line in file if line.strip()]
else:
    web2lowerset = get_english_words_set(['web2'], lower=True)
    words = list(web2lowerset)
    
num_turns=0
stop=False
player_one_points = 0
player_two_points = 0
player_one_name = input("Please enter your name: ")
player_two_name = input("Please enter your name: ")

def correct_word(player_one_name,player_two_name,letters_used):
    letter_guess_player_one=input(f"{player_one_name}, choose a letter: ").lower()
    letter_guess_player_two=input(f"{player_two_name}, choose a letter: ").lower()
    while len(letter_guess_player_one)>1 or letter_guess_player_one in letters_used or not "a"<=letter_guess_player_one<="z":
            letter_guess_player_one=input(f"{player_one_name},enter one character only which is not used and make sure its only in English: ")
    letters_used.append(letter_guess_player_one)
    while len(letter_guess_player_two)>1 or letter_guess_player_two in letters_used or not "a"<=letter_guess_player_two<="z" :
            letter_guess_player_two=input(f"{player_two_name},enter one character only which is not used and make sure its only in English: ")
    letters_used.append(letter_guess_player_two)

    return letter_guess_player_one,letter_guess_player_two

while not stop:
    word = choice(words)
    hidden_word = "_" * len(word)
    letters_used = []
    # print("\n", word)
    print(hidden_word)
    
    
    while "_" in hidden_word:
    #player one
        letter_guess_player_one, letter_guess_player_two = correct_word(player_one_name, player_two_name, letters_used)
        found=False
        for i in range(len(word)):
            if word[i]==letter_guess_player_one:
                hidden_word = hidden_word[:i] + letter_guess_player_one + hidden_word[i+1:]
                player_one_points+=1
                found =True
        if found==False:
            print("Letter not in the word")
        print(*letters_used)
        print(hidden_word)
        
        if "_" in hidden_word:
    #player two
            found =False
            for i in range(len(word)):
                if word[i]==letter_guess_player_two:
                    hidden_word = hidden_word[:i] + letter_guess_player_two + hidden_word[i+1:]
                    player_two_points+=1
                    found =True
            if found==False:
                print("Letter not in the word")
            print(*letters_used)
            print(hidden_word)
            print(f"{player_one_name}: {player_one_points}")
            print(f"{player_two_name}: {player_two_points}")
            if not "_" in hidden_word:
                print(f"You have finished the word:\n {word}\n{player_one_name}: {player_one_points}\n{player_two_name}: {player_two_points}")
                num_turns+=1
                if num_turns>=10:
                    stop=True
                    if player_one_points>player_two_points:
                        print(f"{player_one_name} is the winner!")
                    elif player_one_points<player_two_points:
                        print(f"{player_two_name} is the winner!")
                    else:
                        print("No one wins its even !")
                        

    