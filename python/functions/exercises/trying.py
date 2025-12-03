#1
# def count_char(string,char):
#    amount_of_chars=0
#    for c in string:
#       if c==char:
#          amount_of_chars+=1
#    return amount_of_chars
# user_string = input("Enter a string: ")
# user_char = input("Enter a character to search: ")
# print(count_char(user_string,user_char))

2
# def reverse_number(number):
#    opposite_number = 0
#    is_negative=number<0
#    if is_negative:
#       number=-number
#    while number!=0:
#       digit_number=number%10
#       opposite_number=opposite_number*10+digit_number
#       number=number//10
#    if is_negative:
#       opposite_number=-opposite_number
#    return opposite_number
# user_number = int(input("Enter a number: "))
# print(reverse_number(user_number))

#מחרוזת כולל עשרוני 
def reverse_number(number):
    number = str(number)
    
    is_negative = False
    if number[0] == "-":
        is_negative = True
        number = number[1:]  
    
    if "." in number:
        whole, frac = number.split(".") 
        reversed_number = whole[::-1] + "." + frac[::-1]  
    else:
        reversed_number = number[::-1]  
    
    if is_negative:
        reversed_number = "-" + reversed_number
    
    return reversed_number
user_number = input("Enter a number (integer or float): ")
print(reverse_number(user_number))


# #3
# def is_leap_year(year):
#    if year%400 == 0 :
#       return "שנה מעוברת"
#    elif year%100 == 0:
#       return "שנה לא מעוברת"
#    elif year%4==0:
#       return "שנה מעוברת"
#    else:
#       return "שנה לא מעוברת"
# user_year = int(input("Enter a year: "))
# print(is_leap_year(user_year))

# #מתקדמים   
# def is_leap_year(year):
#    if year%400 == 0  or  (year%4==0 and year%100!=0)  :
#       return"שנה מעוברת"
#    else:
#       return"שנה לא מעוברת"
# user_year = int(input("Enter a year: "))
# print(is_leap_year(user_year))

# #4

# def char_in_password(password):
#    number = False
#    symbols = False
#    lower_letter = False
#    capital_letter = False
#    symbols_bank = ["@", "#", "%", "&"]
#    for char in password:
#       if "0"<=char<="9":
#          number = True
#       elif "a"<=char<="z":
#             lower_letter = True 
#       elif "A"<=char<="Z":
#                capital_letter = True 
#       elif char in symbols_bank:
#                   symbols = True
#    if len(password)>=8 and number and lower_letter and capital_letter and symbols :
#       return "Good password"
#    else:
#       return "try again"
# user_password = input("Enter your password: ")
# print(char_in_password(user_password))

#5
# def sum_of_dividers(number):
#    deviders_sum=0
#    for i in range(1,number+1):
#       if number%i ==0:
#          deviders_sum+=i
#    return(deviders_sum)
# user_number=int(input("Enter your number: "))
# print(sum_of_dividers(user_number))

# #6
# def is_prime_number(number):
#    is_prime=True
#    if number<2:
#       is_prime=False
#    for i in range(2,number):
#       if number%i==0:
#          is_prime=False
#          break
#    if not is_prime:
#       return "The number is not prime"
#    else:
#       return "The number is prime"
# user_number=int(input("Please enter your number: "))
# print(is_prime_number(user_number))