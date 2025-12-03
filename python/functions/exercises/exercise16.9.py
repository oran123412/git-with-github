#exercise16.9

# number = int(input("Plese enter a number"))
# if 10<=number <=99:
#     if number%3 ==0:
#         print("Wow")
#     else:
#         sum = number//10 + number%10
#         print(sum)
# else:
    
#     if number%2 == 0:
#         print("Your number is even")
#     else:
#         print("Your number is odd")

#כתבו קטע קוד שמקבל מספר כקלט אם המספר זוגי ידפיס 2 
# number = int(input("Plese enter a number: "))
# if number%2 == 0:
#     print("2")
# elif number%3==0:
#     print("3")
# elif number%5==0:
#     print("5")
# elif number%7==0:
#     print("7")
# else:
#     print("0")
        
#3 
#קטע קוד שמדפיס כל המספרים שמתחלקים ב3 או 7

# for i in range(100):
#     if i%3 == 0 or i%7 ==0: 
#         print(i)

#4
#קטע קוד מקבל מספר כקלט ומדפיס את סכום הספרות שלו ואת מכפלת הספרות שלו

# number = int(input("Plese enter a number "))
# sum = number//10 + number%10
# multiplication = (number//10) * (number%10)
# print(f'the sum is {sum} the multiplication is  {multiplication}')

#5
#מקבל 10 מספרים ומדפיס ממוצע
# number = 0
# for i in range(10):
#     number += int(input("Plese enter a number "))
# print(f'the average is {number/10}')

#6
#מקבל מספר N מהמשתמש ומקבל אותו מספר ומדפיס ממוצע

# n = int(input("Plese enter a number "))
# sum = 0
# for i in range(n):
#     sum +=int(input("Plese enter a number "))
# print(f'the average is {sum/n}')

#7
#מקבל 5 מספרים ומוריד הפרש בינהם 
# num1=0
# for i in range(5):
#     num2 = int(input("Plese enter a number "))
#     if num2>num1:
#         subtraction = num2 - num1
#         print("the subtraction is ",subtraction)
#     else:
#         subtraction= num1-num2
#         print("the subtraction is ",subtraction)
#     num1 = num2

#8
#מקבל N ואז רץ N פעמים וכו'

n = int(input("Plese enter a number "))
count=0
for i in range(n):
    question = input("How much is {co} squared? ")
    print("how much ")
    if question == i**2:
        print("right")
    else:
        print("wrong")
count+=1

