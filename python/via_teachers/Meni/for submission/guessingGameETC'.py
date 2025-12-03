#                                                       משחק הניחושים ובול פגיעה                                                          
#                                                         ============================

#level 1-
#1
import random

def guess_number(number):
    while True:
        number_user=int(input("What is the number ?"))
        if number_user<number:
            print("Number too small")
        elif number_user>number:
            print("Number too large")
        elif number_user ==number:
            return ("Congratulations, you guessed correctly!")
        
print(guess_number(random.randint(0,100)))

#2
import random
lst=[]

def guess_number(number):
    count=0
    while True:
        number_user=int(input("What is the number ?"))
        if number_user<number:
            print("Number too small")
            lst.append(number_user)
            count+=1
        elif number_user>number:
            print("Number too large")
            count+=1
            lst.append(number_user)
        elif number_user ==number:
            print ("Congratulations, you guessed correctly!")
            print(f"Your guesses were: {lst}")
            return(f'the number of attemps is {count}')
        
print(guess_number(random.randint(0,100)))

#3
import random
lst=[]

def guess_number(number):
    count=0
    while True:
        number_user=int(input("What is the number ?"))
        if number_user in lst:
            print("You already guessed that number... :-(")
            count+=1
        elif number_user<number:
            print("Number too small")
            lst.append(number_user)
            count+=1
        elif number_user>number:
            print("Number too large")
            count+=1
            lst.append(number_user)
        elif number_user ==number:
            print ("Congratulations, you guessed correctly!")
            return(f'the number of attemps is {count}')
        
print(guess_number(random.randint(0,100)))


#level 2

#1
import random

def guess_number(number):
    lst=[]
    count=0
    while count<10:
        number_user=int(input("What is the number ?"))
        if number_user in lst:
            print("You already guessed that number... :-(")
            count+=1
        elif number_user<number:
            print("Number too small")
            lst.append(number_user)
            count+=1
        elif number_user>number:
            print("Number too large")
            count+=1
            lst.append(number_user)
        elif number_user ==number:
            print ("Congratulations, you guessed correctly!")
            return(f'the number of attemps is {count}')
    if count==10 :
        return("game over")
        
print(guess_number(random.randint(0,100)))

#2
import random
lst=[]

def guess_number(number):
    count=0
    while count<10:
        number_user=int(input("What is the number ?"))
        if number_user in lst:
            print("You already guessed that number... :-(")
            count+=1
        elif number_user<number:
            print("Number too small")
            lst.append(number_user)
            count+=1
            print(f'📌 Guesses: {",".join(map(str,lst))}')
        elif number_user>number:
            print("Number too large")
            count+=1
            lst.append(number_user)
            print(f'📌 Guesses: {",".join(map(str,lst))}')
        elif number_user ==number:
            print ("Congratulations, you guessed correctly!")
            print(f'📌 Guesses: {",".join(map(str,lst))}')
            return(f'the number of attemps is {count}')
    if count==10 :
        return("game over")
        
print(guess_number(random.randint(0,100)))

#level 3 

#1
import random

def hit_or_bullseye(list_of_numbers:list):

    users_guess = list(map(int, input("Enter 4 numbers: ").replace(","," ").split()))
    while users_guess!=list_of_numbers:
        correct_numbers_and_index=0
        correct_numbers_only=0
        for i in range(4):
            if users_guess[i]==list_of_numbers[i]:
                print(f"Your {users_guess[i]} is correct and is in the right place ")
                correct_numbers_and_index+=1
            elif users_guess[i] != list_of_numbers[i] and users_guess[i] in list_of_numbers:
                print(f"Your {users_guess[i]} is correct but is not in the right place ")
                correct_numbers_only+=1
        print (f"The number of correct answers in numbers and index are {correct_numbers_and_index},\n correct number of correct numbers only are {correct_numbers_only}")
        users_guess = list(map(int, input("Enter 4 numbers: ").replace(","," ").split()))
    
        
print(hit_or_bullseye([random.randint(0,9) for _ in range(4)]))

#2
import random

def hit_or_bullseye(list_of_numbers:list):

    users_guess = list(map(int, input("Enter 4 numbers: ").replace(","," ").split()))
    if users_guess==list_of_numbers:
            return("You won!")
    while users_guess!=list_of_numbers:
        correct_numbers_and_index=0
        correct_numbers_only=0
        for i in range(4):
            if users_guess[i]==list_of_numbers[i]:
                print(f"Your {users_guess[i]} is correct and is in the right place ")
                correct_numbers_and_index+=1
            elif users_guess[i] in list_of_numbers:
                print(f"Your {users_guess[i]} is correct but is not in the right place ")
                correct_numbers_only+=1
        print (f"The number of correct answers in numbers and index are {correct_numbers_and_index},\n correct number of correct numbers only are {correct_numbers_only}")
        users_guess = list(map(int, input("Enter 4 numbers: ").replace(","," ").split()))
    return "You won!"
        
print(hit_or_bullseye([random.randint(0,9) for _ in range(4)]))

#3
import random

def hit_or_bullseye(list_of_numbers:list):

    list_of_guess=[]
    while True:
        users_guess = list(map(int, input("Enter 4 numbers: ").replace(","," ").split()))
        if users_guess in list_of_guess:
            print("You already guessed that number... :-(")
            continue
        list_of_guess.append(users_guess)
        if users_guess==list_of_numbers:
            return("You won!")
        correct_numbers_and_index=0
        correct_numbers_only=0
        for i in range(4):
            if users_guess[i]==list_of_numbers[i]:
                print(f"Your {users_guess[i]} is correct and is in the right place ")
                correct_numbers_and_index+=1
            elif users_guess[i] in list_of_numbers:
                print(f"Your {users_guess[i]} is correct but is not in the right place ")
                correct_numbers_only+=1
        print (f"The number of correct answers in numbers and index are {correct_numbers_and_index},\n correct number of correct numbers only are {correct_numbers_only}")
        
print(hit_or_bullseye([random.randint(0,9) for _ in range(4)]))

#4
import random

def hit_or_bullseye(list_of_numbers:list):
    guesses_history=[]
    while True:
        users_guess = list(map(int, input("Enter 4 numbers: ").replace(","," ").split()))
        if users_guess in guesses_history:
            print("You already guessed that number... :-(")
            continue
        guesses_history.append(users_guess)
        if users_guess==list_of_numbers:
            return f"You won!\nThe number of attempts to find the right answer are: {len(guesses_history)}" 
        correct_numbers_and_index=0
        correct_numbers_only=0
        for i in range(4):
            if users_guess[i]==list_of_numbers[i]:
                print(f"Your {users_guess[i]} is correct and is in the right place ")
                correct_numbers_and_index+=1
            elif users_guess[i] in list_of_numbers:
                print(f"Your {users_guess[i]} is correct but is not in the right place ")
                correct_numbers_only+=1
        print (f"The number of correct answers in numbers and index are {correct_numbers_and_index},\n correct number of correct numbers only are {correct_numbers_only}")
        
print(hit_or_bullseye([random.randint(0,9) for _ in range(4)]))

#level 4 

#1
import random

def hit_or_bullseye(list_of_numbers:list):

    list_of_guess=[]
    while True:
        users_guess = list(map(int, input("Enter 4 numbers: ").replace(","," ").split()))
        if users_guess in list_of_guess:
            print("You already guessed that number... :-(")
            continue
        list_of_guess.append(users_guess)
        if users_guess==list_of_numbers:
            return f"You won!\nThe number of attempts to find the right answer is: {len(list_of_guess)}" 
        correct_numbers_and_index=0
        correct_numbers_only=0
        for i in range(4):
            if users_guess[i]==list_of_numbers[i]:
                print(f"Your {users_guess[i]} is correct and is in the right place ")
                correct_numbers_and_index+=1
            elif users_guess[i] in list_of_numbers:
                print(f"Your {users_guess[i]} is correct but is not in the right place ")
                correct_numbers_only+=1
        print (f"The number of correct answers in numbers and index are {correct_numbers_and_index},\n correct number of correct numbers only are {correct_numbers_only}")
        
print(hit_or_bullseye([random.randint(0,9) for _ in range(4)]))

#2
import random

def hit_or_bullseye(list_of_numbers:list):
    list_of_guess=[]
    while True:
        users_guess = list(map(int, input("Enter 4 numbers: ").replace(","," ").split()))
        if users_guess in list_of_guess:
            print("You already guessed that number... :-(")
            continue
        list_of_guess.append(users_guess)
        if users_guess==list_of_numbers:
            return f"You won!\nThe number of attempts to find the right answer is: {len(list_of_guess)}" 
        correct_numbers_and_index=0
        correct_numbers_only=0
        for i in range(4):
            if users_guess[i]==list_of_numbers[i]:
                print(f"Your {users_guess[i]} is correct and is in the right place ")
                correct_numbers_and_index+=1
            elif users_guess[i] in list_of_numbers:
                print(f"Your {users_guess[i]} is correct but is not in the right place ")
                correct_numbers_only+=1
        print (f"The number of correct answers in numbers and index are {correct_numbers_and_index},\n correct number of correct numbers only are {correct_numbers_only}")
        
print(hit_or_bullseye([random.randint(0,9) for _ in range(4)]))

#3
import random

def hit_or_bullseye(list_of_numbers:list):
    print(list_of_numbers)
    list_of_guess=[]
    while True:
        users_guess = list(map(int, input("Enter 4 numbers: ").replace(","," ").split()))
        if users_guess in list_of_guess:
            print("You already guessed that number... :-(")
            continue
        list_of_guess.append(users_guess)
        if users_guess==list_of_numbers:
            return f"You won!\nThe number of attempts to find the right answer is: {len(list_of_guess)}" 
        correct_numbers_and_index=0
        correct_numbers_only=0
        for i in range(4):
            if users_guess[i]==list_of_numbers[i]:
                print(f"Your {users_guess[i]} is correct and is in the right place ")
                correct_numbers_and_index+=1
            elif users_guess[i] in list_of_numbers:
                print(f"Your {users_guess[i]} is correct but is not in the right place ")
                correct_numbers_only+=1
        print (f"The number of correct answers in numbers and index are {correct_numbers_and_index},\n correct number of correct numbers only are {correct_numbers_only}")
        
print(hit_or_bullseye(random.sample(range(10),4)))

#4
import random

def hit_or_bullseye(list_of_numbers:list):
    list_of_guess=[]
    while True:
        users_guess = list(map(int, input("Enter 4 numbers: ").replace(","," ").split()))
        if users_guess in list_of_guess:
            print("You already guessed that number... :-(")
            continue
        list_of_guess.append(users_guess)
        if users_guess==list_of_numbers:
            print (f"You won!\nThe number of attempts to find the right answer is: {len(list_of_guess)}") 
            ask=input("Would you like another round?\n to confirm press 'y' or 'yes' ").lower()
            if ask in("y","yes"):
                list_of_numbers=random.sample(range(10),4)
                list_of_guess = []
                print(list_of_numbers)
                continue
            else: 
                return "game over"
        correct_numbers_and_index=0
        correct_numbers_only=0
        for i in range(4):
            if users_guess[i]==list_of_numbers[i]:
                print(f"Your {users_guess[i]} is correct and is in the right place ")
                correct_numbers_and_index+=1
            elif users_guess[i] in list_of_numbers:
                print(f"Your {users_guess[i]} is correct but is not in the right place ")
                correct_numbers_only+=1
        print (f"The number of correct answers in numbers and index are {correct_numbers_and_index},\n correct number of correct numbers only are {correct_numbers_only}")
        
print(hit_or_bullseye(random.sample(range(10),4)))

#5
import random
BLUE="\033[34m"
RESET = "\033[0m"

def hit_or_bullseye(list_of_numbers:list):
    print(list_of_numbers)
    list_of_guess=[]
    while True:
        users_guess = list(map(int, input("Enter 4 numbers: ").replace(","," ").split()))
        if users_guess in list_of_guess:
            print("You already guessed that number... :-(")
            continue
        list_of_guess.append(users_guess)
        if users_guess==list_of_numbers:
            print (f"You won!\nThe number of attempts to find the right answer is: {len(list_of_guess)}") 
            ask=input("Would you like another round?\n to confirm press 'y' or 'yes' ").lower()
            if ask == 'y' or ask=='yes':
                list_of_numbers=random.sample(range(10),4)
                list_of_guess = []
                print(list_of_numbers)
                continue
            else:
                return "game over"
        correct_numbers_and_index=0
        correct_numbers_only=0
        for i in range(4):
            if users_guess[i]==list_of_numbers[i]:
                print(f"Your {users_guess[i]} is correct and is in the right place ")
                correct_numbers_and_index+=1
            elif users_guess[i] in list_of_numbers:
                print(f"Your {users_guess[i]} is correct but is not in the right place ")
                correct_numbers_only+=1
        print (f"The number of correct answers in numbers and index are {correct_numbers_and_index},\n correct number of correct numbers only are {correct_numbers_only}")
        print (f"{BLUE}Guess #{len(list_of_guess)}: {users_guess}{RESET}" ) 
        
        
print(hit_or_bullseye(random.sample(range(10),4)))