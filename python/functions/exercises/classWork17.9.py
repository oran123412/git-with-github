#1
# number = int(input("Enter a number"))
# if number%2 == 0:
#     print("even")
# else:
#     print("odd")

#2
# number = int(input("Enter a number"))
# if number == 0:
#     print("he is zero")
# elif number>0:
#     print("positive")
# else:
#     print("negative")

#3

# year=int(input("What year are you talking about? "))
# if year%400==0:
#     print("Leap year")
# elif year%100==0:
#     print("not Leap year")
# elif year%4==0:
#     print("Leap year")
# else:
#     print("not Leap year ")

#4
# number1 = int(input("Enter a number"))
# number2 = int(input("Enter another number"))
# if number1>number2:
#     print(number1)
# if number2>number1:
#     print(number2)

#5
# age = int(input("Enter your age"))
# if age>18:
#     print("you are allowed to vote")
# if age<18:
#     print("you are not allowed to vote")
    
#6
# grade = int(input("Enter your grade"))
# if grade>=60:
#     print("pass")
# else:
#     print("falied")

#7
# number = int(input("Enter a number"))
# if number%3 == 0 and number%5==0:
#     print("The number is devided both in 3 and 5 ")
# else:
#     print("not devided")

#8
# letter = input("Enter a letter")
# if letter.islower():
#     print("the letter is small")
# else:
#     print("the letter is big")


#9
# engale1 = int(input("Enter the first engale"))
# engale2= int(input("Enter the second engale"))
# engale3 = int(input("Enter the third engale"))
# if engale1+engale2+engale3==180:
#  print("Its 180")
# else:
#     print("Its not 180")

#10
# number = input("Enter a number")
# if "7" in number:
#     print("lucky number")

#11
# number1 = int(input("Enter the first number"))
# number2 = int(input("Enter the second number"))
# number3 = int(input("Enter the third number"))

# if number1<number2<number3:
#     print("the numbers are growing")
# elif number1>number2>number3:
#     print("the numbers are decreasing")
# else:
#     print("there is no order in the numbers")

# excersice teacher in class
# number = int(input("Enter a number"))
# i = 0
# while i<number:
#     print("*" , end="")
#     i +=1

#12
# days = int(input("Enter the days"))
# month = int(input("Enter the month"))
# year = int(input("Enter the year"))
# if days>31 or days<1 or 12<month or month<1 or 2025<year:
#     print("invalid date")
# else:
#     print("valid date")

#13
side1 = int(input("Enter the first side"))
side2 = int(input("Enter the first side"))
side3 = int(input("Enter the first side"))

if side2+side3>side1 and side3+side1>side2 and side1+side2>side3:
    print("It's a triangle")
    if side1==side2==side3:
        print("All sides are equal")
    elif side1==side2 or side1==side3 or side2==side3:
        print("only two side are equal")
    else:
        print("It's usual triangle only")
else:
    print("its not a triangle")



#14
# numberThreeDigits = int(input("Enter the number"))
# sum = numberThreeDigits//100 + numberThreeDigits//10 + numberThreeDigits%10
# if sum%2==0:
#     print("even")
# else:
#     print("odd")

#15
# number = int(input("Enter a number "))
# if  number%3==0 and number%10==3:
#     print("very special number")
# elif number%3==0 or number%10 ==3:
#     print("special number")
# else:
#     print("not special")

#excrsice 

# count = 20
# while count>=0:
#     if not count%2:
#         print(count,end=" ")
#     count-=1

# number = 0
# while number<=100:
#     if number%3==0 and number%5==0:
#         print(number)
#     number+=1 

#excersice

#2
# num=int(input("please enter a number"))
# num = num if num>0 else -num 
# #יש גם אופציה לעשות במקום שורה למעלה את זה num=abs(num)
# sum=0
# while num != 0:
#     digital=num%10
#     sum+=digital
#     num//=10
# print(sum)
    
