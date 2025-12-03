#1
# div= int(input("Please enter a number: "))
# while div ==0:
#     div= int(input("Please enter a number which is not zero: "))
# num= int(input("Please enter a number: "))
# while num<=0:
#     num= int(input("Please enter a number which is positive: "))
# for i in range(1,num+1):
#     if i%div==0:
#         print(i)
        
#2
# numbers=int(input("Please enter a number (when finish please enter -1): "))
# num_digits_in_series = 0
# while numbers !=(-1):
#     numbers=int(input("Please enter a number (when finish please enter -1): "))
#     num_digits_in_series+=1
# print(f"The number of digits is: {num_digits_in_series}")

#3
#א)
# growing = True
# prev_number=0
# current_number=int(input("Please enter a number (when finish please enter -1): "))
# while current_number<=0:
#     current_number=int(input("Please enter a number bigger than 0 (when finish please enter -1): "))
# while current_number!=-1:
#     prev_number=current_number
#     current_number=int(input("Please enter a number (when finish please enter -1): "))
#     if current_number<prev_number and current_number!=-1:
#         growing=False
#         print("The series isn't growing")
#         break
# if growing:
#     print("The series is growing")
    
#ב)
# growing = True
# prev_number=0
# current_number=int(input("Please enter a number (when finish please enter -1): "))
# while current_number<=0:
#     current_number=int(input("Please enter a number bigger than 0 (when finish please enter -1): "))
# while current_number!=-1:
#     prev_number=current_number
#     current_number=int(input("Please enter a number (when finish please enter -1): "))
#     if current_number<prev_number and current_number!=-1:
#         growing=False
# if growing:
#     print("The series is growing")
# else:
#     print("The series is  not growing")


#4
#א)
# n=int(input("Please enter a number*: "))
# current_number=0
# prev_number=0
# for i in range(n):
#     number_from_series=int(input("Please enter a number*2*: "))
#     current_number=number_from_series
#     if current_number <=prev_number:
#         print("The series isn't growing")
#         break
#     prev_number=current_number
# else:
#     print("The series is growing")
    
#ב)
# growing=True
# n=int(input("Please enter a number*: "))
# current_number=0
# prev_number=0
# for i in range(n):
#     number_from_series=int(input("Please enter a number*2*: "))
#     current_number=number_from_series
#     if current_number <=prev_number:
#         growing=False
#     prev_number=current_number
# if growing:
#     print("The seires is growing")
# else:
#     print("The seires is not growing")

    
#5
#א)
# number=int(input("Please enter a number: "))
# max_number=number
# while number!=-1:
#    number=int(input("Please enter a number: "))
#    if number >max_number:
#       max_number=number
# print(max_number)

#ב)
# number=int(input("Please enter a number: "))
# max_number=0
# second_max=0
# while number!=-1:
#     if number >max_number:
#         second_max=max_number
#         max_number=number
#     elif number>second_max:
#         second_max=number
#     number=int(input("Please enter a number: "))
# print(max_number,second_max)

#6
# number=int(input("Please enter a number: "))
# max_digit=0
# max_left=0
# max_right=0
# index=0
# while number>0:
#     digit=number%10
#     if digit>max_digit:
#         max_digit=digit
#         max_right=index
#     if digit==max_digit:
#         max_left=index
#     number=number//10
#     index+=1
# print(f" The max digit is :{max_digit} the index in the right is {max_right} and the left is {max_left}")

#7
#א)
# binary_number=int(input("Please enter a binary number: "))
# index=0
# decimal_number=0
# while binary_number>0:
#     digit=binary_number%10
#     binary_number=binary_number//10
#     decimal_number+=digit*(2**index)
#     index+=1
# print(decimal_number)

#ב)
# binary_number = int(input("Enter a binary number: "))
# decimal_number = 0

# # קודם מוצאים את מספר הספרות
# num_digits = 0
# temp = binary_number
# while temp > 0:
#     temp //= 10
#     num_digits += 1

# # עכשיו סורקים מימין לשמאל ומחשבים את הערך בעשרוני
# temp = binary_number
# for i in range(num_digits):
#     digit = temp // (10**(num_digits-i-1)) % 10  # בודדים את הספרה השמאלית ביותר שנותרה
#     decimal_number += digit * (2**(num_digits-i-1))

# print(decimal_number)

#8
# small_number=int(input("Please enter a number: "))
# big_number=int(input("Please enter a number: "))
# dem_number=0
# sum_numbers=0

# if small_number>big_number:
#     dem_number=small_number
#     small_number=big_number
#     big_number=dem_number

# for i in range(small_number):
#     sum_numbers+=big_number
# print(sum_numbers)

#7ב)

# binary_number = input("Enter binary number (left to right): ")

# decimal_number = 0
# length = len(binary_number)

# for i in range(length):
#     digit = int(binary_number[i])      # המרה מ־str ל־int
#     power = length - 1 - i             # החזקה של הספרה (מMSB לLSB)
#     decimal_number += digit * (2 ** power)

# print(decimal_number)




