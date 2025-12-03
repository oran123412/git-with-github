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

def correct_word(letters_used):
    letter_guess_player_one=input(f"choose a letter: ").lower()
    while len(letter_guess_player_one)>1 or letter_guess_player_one in letters_used or not "a"<=letter_guess_player_one<="z":
            letter_guess_player_one=input(f"enter one character only which is not used and make sure its only in English: ")
    letters_used.append(letter_guess_player_one)

    return letter_guess_player_one

while not stop:
    word = choice(words)
    hidden_word = "_" * len(word)
    letters_used = []
    print("\n", word)
    print(hidden_word)
    
    while "_" in hidden_word:
    #player one
        letter_guess_player_one = correct_word(letters_used)
        found=False
        for i in range(len(word)):
            if word[i]==letter_guess_player_one:
                hidden_word = hidden_word[:i] + letter_guess_player_one + hidden_word[i+1:]
                found =True
        if found==False:
            print("Letter not in the word")
        print(*letters_used)
        print(hidden_word)
        if "_" in hidden_word:

            if not "_" in hidden_word:
                print(f"You have finished the word:\n {word}\n")
                num_turns+=1
                if num_turns>=10:
                    stop=True
                        

    