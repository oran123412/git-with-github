#1
# previous=None
# for i in range(10):
#     number=int(input("Plese enter a number: "))
#     if previous is not None:
#         if number >previous:
#             print(f" {number} is bigger")
#         elif number <previous:
#             print(f" {number} is smaller")
#         else:
#             print(f"{number} is equal to {previous}")
#     previous=number

#2
# number=int(input("Please enter a number: "))
# numbers_sum=number
# i = 1
# while number !=(numbers_sum/i) :
#     number=int(input("Please enter a number: "))
#     numbers_sum+=number
#     i += 1
# print(i)
        
#3
# sum_numbers=0
# duplication_numbers=0
# numbers=[]
# num = int(input("Please enter a number: "))
# while num !=0:
#     numbers.append(num)
#     num = int(input("Please enter a number: "))
# calc=input("Do you want to duplicate or to sum the numbers, +/*:  ")
# while calc != "+" or calc != "*":
#     calc=input("Do you want to duplicate or to sum the numbers, +/*:  ")
# if calc == "+":
#     for i in numbers:
#         sum_numbers+=i
# if calc == "*":
#     for i in numbers:
#         sum_numbers*=i
# print(sum_numbers)
    
# def even(num1,num2):
#     if (num1%2==0 and num2%2!=0) or (num1%2!=0 and num2==0) :
#         return False
#     else:+-

#         return True
# def sum_of_two(num1,num2,num3):
#     if num1<num2 and num1<num3:
#         sum_numbers=num2+num3
#         return sum_numbers
#     elif num2<num3 and num2<num1:
#         sum_numbers=num1+num3
#         return sum_numbers
#     elif num3<num1 and num3<num2:
#         sum_numbers=num1+num2
#         return sum_numbers

# def middle_of_numbers(num1,num2,num3):
#     if num1<num2<num3 or num3<num2<num1:
#         return num2
#     elif num2<num1<num3 or num3<num1<num2:
#         return num1
#     elif num2<num3<num1 or num1<num3<num2:
#         return num3        

#6
def sum_of_non_even(arr):
    sum=0
    for i in arr:
        if i%2!=0:
            sum+=i
    return sum

#7
# def divided_by_n(n,arr):
#     for i in arr:
#         if i%n!=0:
#             return False
#     return True

#8
# def duplication(arr):
#     count=0
#     for i in range(len(arr)-1):
#         if arr[i]==arr[i+1]:
#             count+=1
#     return count
        

        