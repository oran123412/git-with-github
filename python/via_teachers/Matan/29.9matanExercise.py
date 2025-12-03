
#1
div=int(input("Please enter a number of the div: "))
while div ==0:
    div = int(input("Div cannot be equal to zero, enter a diffrent number please: "))
num=int(input("Please enter a number of the num: "))
while num<=0:
    num=int(input("Num cannot be smaller or equal to 0,please enter a diffrent number: "))
for i in range (1,num+1):
    if i%div ==0:
        print(i)

#2
count=0
numbers=int(input("Please enter the numbers you want to count their digits,when finished write -1: "))
while numbers!=-1:
    count+=1
    numbers=int(input("Please enter the numbers you want to count their digits,when finished write -1: "))
print(count)

#3
#א
is_growing = True
prev_number = 0
current_number = int(input("Please enter the numbers, when finished write -1: "))

if current_number == -1:
    is_growing = False
    print("סדרה לא עולה")
else:
    prev_number = current_number
    current_number = int(input("Please enter the numbers you want to count their digits, when finished write -1: "))
    
    while current_number != -1:
        if current_number <= prev_number:
            is_growing = False
            print("סדרה לא עולה")
            break
        prev_number = current_number   
        current_number = int(input("Please enter the numbers you want to count their digits, when finished write -1: "))

if is_growing:
    print("סדרה עולה")
else:
    print("לא סדרה עולה")


#ב
is_growing = True
prev_number = 0
current_number = int(input("Please enter the numbers, when finished write -1: "))

if current_number == -1:
    is_growing = False
else:
    prev_number = current_number
    current_number = int(input("Please enter the numbers you want to count their digits, when finished write -1: "))
    
    while current_number != -1:
        if current_number <= prev_number:
            is_growing = False
        prev_number = current_number   
        current_number = int(input("Please enter the numbers you want to count their digits, when finished write -1: "))

if is_growing:
    print("סדרה עולה")
else:
    print("לא סדרה עולה")
    
#4
#א
num=int(input("Please enter a number: "))
current_num=0
for i in range(num):
    current_num=int(input("Please enter a number: "))
    if current_num<=prev_num:
        print("The series isnt growing")
        break
    prev_num=current_num
else:
     print("The series is growing")
     
#ב
num=int(input("Please enter a number: "))
prev_num=0
growing=True
for i in range(num):
    current_num=int(input("Please enter a number: "))
    if current_num<=prev_num:
        growing=False
    prev_num=current_num
if growing:
    print("The series is growing")
else:
    print("The series isn't growing")


#5
#א
max_num = 0
number = int(input("Enter a number (-1 to stop): "))

while number != -1:
    if number > max_num:   
        max_num = number
    number = int(input("Enter a number (-1 to stop): "))

print("המספר הגדול ביותר הוא:", max_num)

#ב
max_num1 = 0
max_num2 = 0
number = int(input("Enter a number (-1 to stop): "))

while number != -1:
    if number > max_num1:
        max_num2 = max_num1
        max_num1 = number
    elif number > max_num2:
        max_num2 = number
    number = int(input("Enter a number (-1 to stop): "))

print(f"The biggest number is {max_num1}\nthe second after that is {max_num2}" )


#6
number=int(input("Please enter a number: "))
digit=0
high_digit=0
index_right_side=0
index_left_side=0
save_right=0
save_left=0
index=0
while number>0:
    digit=number%10
    if digit>high_digit:
        high_digit=digit
        save_right=index
        save_left=index
    if digit==high_digit:
        save_left=index
    number=number//10
    index+=1
print(f"Your number is {high_digit} and your index is {save_right} from the right side, and {save_left} from the left side")
        
#7
#א
#מימין לשמאל
binary_number=int(input("Please enter your number: "))
full_numer_base_10=0
power=0
while binary_number>0:
    digit_base_10=binary_number%10*(2**power)
    power+=1
    binary_number=binary_number//10
    full_numer_base_10+=digit_base_10
print(full_numer_base_10)

#ב
#משמאל לימין
binary_number=int(input("Please enter your number: "))
number_of_digits=binary_number
full_numer_base_10=0
power=0
while number_of_digits>0:
    number_of_digits=number_of_digits//10 
    power+=1
while binary_number>0:
    digit_base_10=binary_number%10*(2**(power-1))
    power-=1
    binary_number=binary_number//10
    full_numer_base_10+=digit_base_10
print(full_numer_base_10)    

#8
num1=int(input("Please enter a number: "))
while num1<=0:
    num1=int(input("Please enter a number which is above 0: "))
num2=int(input("Please enter a number: "))
while num2<=0:
    num2=int(input("Please enter a number which is above 0: "))

if num1>=num2:
    sum_numbers=0
    for i in range (num2):
        sum_numbers+=num1
    print(f"The multipaction is {sum_numbers}")
else:
    sum_numbers=0
    for i in range (num1):
        sum_numbers+=num2
    print(f"The multipaction is {sum_numbers}")
    