# לחשב את סכום ספרות של מספר שנקבל ממשתמש
# sum_of_digits=0
# number=int(input("Please enter a number: "))
# while number>0:
#     digit=number%10
#     sum_of_digits+=digit
#     number//=10
# print(sum_of_digits)

#הדפס כל מספרים מ1 עד 10 
# #1
# for i in range(1,11):
#     print (i)

# #2
# for i in range(10,0,-1):
#     print(i)

# #3
# for i in range (2,22,2):
#     print(i)

# #4
# for i in range (11):
#     print(i*i)

# #5
# for i in range(5,51,5):
#     print(i)

# #6
# sum_of_numbers=0
# for i in range(1,101):
#     sum_of_numbers+=i
# print(sum_of_numbers)

# #7
# sum_of_numbers=0
# count = 0
# for i in range(1,11):
#     sum_of_numbers+=i
#     count = i
# avg=sum_of_numbers/count
# print(avg)

# #8
# sum_numbers=0
# for i in range(2,101,2):
#     sum_numbers+=i
# print(sum_numbers)

# #9
# count=0
# for i in range(1,101):
#     if i%3==0 or i%5==0:
#         count+=1
# print(count)

# #10
# result=1
# number=int(input("Please enter a number: "))
# for i in range(1,number+1):
#     result*=i
# print(result)

# #11
# result=1
# base=int(input("Please enter a base: "))
# power=int(input("Please enter a power: "))
# for i in range(1,power+1):
#     result*=base
# print(result)

# #12
# firstly=True
# number=int(input("Please enter a number: "))
# if number <= 1:
#     firstly = False
# for i in range(2,number):
#     if number%i==0 :
#         firstly=False
# if firstly:
#     print("its reshony")
# else:
#     print("its not reshony")

# #13
# sum_of_dividers=0
# n=int(input("Please enter a number: "))
# for i in range(1,n):
#     if n%i==0 :
#         sum_of_dividers+=i
# print(sum_of_dividers)
# if sum_of_dividers>n:
#     print("bigger")
# elif sum_of_dividers<n:
#     print("smaller")
# else:
#     print("equal")

# #14
# start=int(input("Please enter a start: "))
# end=int(input("Please enter a end: "))
# sum_of_numbers=0
# step=1 
# if start>end:
#     step=-1
# for i in range(start,end+1,step):
#     sum_of_numbers+=i
# print(sum_of_numbers)
        
