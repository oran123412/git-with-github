#תרגילים להגשה 
#1
# TOTOSIZE = 15
# d = 0
# for i in range(1, TOTOSIZE + 1) :
#     score = input("Enter score: ")
#     if score == 'X':
#         d += 1
# print(d)


# עליכם לכתוב תכנית מחשב המקבלת כקלט שני מספרים שלמים ) לאו דווקא חיוביים(,
# ומציגה כפלט את סכום כל המספרים השלמים שביניהם .לדוגמא :עבור הקלט 3 , 1 יהיה הפלט: 6
# )כי 6=1+2+3 (
# num1 = int(input("Please enter the first number"))
# num2 = int(input("Please enter the second number"))
# demo_num = 0
# sum_numbers=0
# if num1>num2:
#     demo_num=num1
#     num1=num2
#     num2=demo_num
# for i in range(num1,num2+1):
#     sum_numbers+= i
# print(sum_numbers)
    
#קבוצת תלמידים תיקרא" הומוגנית "אם טווח הגילאים בה אינו עולה על 3 שנים;
#אחרת– קבוצת התלמידים תיקרא" הטרוגנית."

# number_of_students = int(input("How many student there are in the class"))
# list_of_ages_in_class=[]
# max_num=0
# min_num=0

# for i in range(1,number_of_students+1):
#     list_of_ages_in_class.append()
#     if i+1 > i:
#         max_num=i+1
#     if i+1<i:
#         min_num=i+1
# if (max_num - min_num) >3:
#     print("קבוצה הטרוגנית")
# else:
#     print("קבוצה הומוגנית,")


# n_number_students = int(input("How many student there are in the class"))

# for i in range(n_number_students):
#     n_age_student = int(input("What is the age of the student"))
#     if i ==0:
#         min_num=max_num=n_age_student
#     else:
#         if n_age_student > max_num:
#             max_num=n_age_student
#         if n_age_student<min_num:
#             min_num=n_age_student
# if (max_num - min_num) >3:
#     print("קבוצה הטרוגנית")
# else:
#     print("קבוצה הומוגנית,")


#כתבו תכנית מחשב אשר קולטת שני מספרים שלמים M , N הגדולים שניהם מ .1- לאחר
#מכן התכנית תקלוט רשימה של N מספרים שלמים וחיוביים)טבעיים(.
#התכנית תבדוק האם קיימים בקלט זוג מספרים כלשהם )לאו דווקא עוקבים( אשר סכומם גדול
#מ M , ותציג כפלט הודעה מתאימה.

# m =int(input("enter the 'm' number"))
# n_amount=int(input("enter the amount of numbers"))
# n =[]
# flag_bigger = False
# max_num=0


# for i in range(1,n_amount+1,1):
#     n=int(input("Enter a number"))
#     if i > max_num:
#         max_num=i
#     if max_num+i>m:
#         flag_bigger = True
#     else:
#         flag_bigger = False
    
       
# if (flag_bigger):
#     print("the sum of the numbers are bigger than 'n'")
# else:
#     print("the sum of the numbers are smaller than 'n'")



# m = int(input("Enter the 'm' number: "))
# n = int(input("Enter the amount of numbers you will enter: "))
# numbers = []
# flag_bigger = False
# max_num = 0

# for i in range(n):
#     num = int(input(f"Enter number {i+1}: "))
#     numbers.append(num)
#     if num > max_num:
#         max_num = num

# # בדיקה אם יש זוג מספרים שסכומם גדול מ-m
# for number in numbers:
#     if max_num + number > m:
#         flag_bigger = True
#         break

# if flag_bigger:
#     print("The sum of two numbers is bigger than 'm'")
# else:
#     print("The sum of two numbers is not bigger than 'm'")

# m = int(input("Enter M: "))
# n = int(input("Enter the number of numbers you will enter: "))

# numbers = []
# for i in range(n):
#     num = int(input(f"Enter number {i+1}: "))
#     numbers.append(num)

# found = False
# # בדיקה לכל זוג מספרים
# for i in range(n):
#     for j in range(i+1, n):
#         if numbers[i] + numbers[j] > m:
#             found = True
#             break
#     if found:
#         break

# if found:
#     print("The sum of two numbers is bigger than M")
# else:
#     print("No pair has a sum bigger than M")



#כתבו תכנית מחשב אשר מקבלת כקלט מספר שלם וחיובי )טבעי( הקטן מ 86,400 המציין את
#מספר השניות שחלפו מאז תחילת היממה ,ותציג כפלט את השעה הנוכחית.
#לדוגמא :עבור הקלט , 49,635 יוצג הפלט: 13:47:15 .
# whole_number=int(input("please enter a number which is less than 86,400: "))
# hours=whole_number//3600
# minutes=(whole_number%3600)//60
# seconds=(whole_number-hours*3600-minutes*60)
# print(f'{hours}:{minutes}:{seconds}')

#6
# counter1 =0
# counter2 =0
# for i in range(1, 42):
#     vote = int(input("Enter vote: "))
# if vote == 1:
#     counter1 += 1
# else:
#     counter2 += 1
# if counter1 > counter2:
#     print("number 1 won")
# else:
#     print("number 2 won")
    
#b.
# counter1 =0
# for i in range(1, 42):
#     vote = int(input("Enter vote: "))
# if vote == 1:
#     counter1 += 1
#     if counter1>=21:
#             print("number 1 won")
# else:
#     print("number 2 won")
        
counter1 = 0

for i in range(1, 42):
    vote = int(input("Enter vote: "))
    if vote == 1:
        counter1 += 1

# קובע את המנצח בסוף
if counter1 >= 21:
    print("Number 1 won")
else:
    print("Number 2 won")
#7

# seconds_past=int(input("Please enter the number of seconds past of the day "))
# while seconds_past>86400 or seconds_past<0:
#     print("The number of seconds you entered is invalid, put positive number smaller than 86400 ")
#     seconds_past=int(input("Please enter the number of seconds past of the day "))

# hours=seconds_past//3600
# minutes=(seconds_past%3600)//60
# seconds=(seconds_past-(hours*3600)-(minutes*60))
# print(f'{hours}:{minutes}:{seconds}')

#8
# x = int(input("Enter the value of x: "))
# y = int(input("Enter the value of y: "))
# if not (x <= 0 and y >= x):
#     print("A")
# else:
#     print("B")
    
# x = int(input("Enter the value of x: "))
# y = int(input("Enter the value of y: "))
# if not (x < 0 or y > x):
#     print("A")
# else:
#     print("B")

#9
# n=int(input("Please enter the number of digits you want to see "))
# q=int(input("Please enter the distance between the numbers "))
# a1=int(input("Please enter the first digit "))

# for i in range(n):
#     print(a1)
#     a1 *= q


#10
# sum=0
# i=0
# while i<=1000:
#     if i%3 == 0 or i%5 ==0:
#         sum+=i
#     i+=1
# print(sum) 

#11
# a=int(input("Please enter a number"))

# while  a<1 or a>18:
#     print("Please enter a number only between 1 to 18")
#     a=int(input("Please enter a number"))
    
# for i in range(1,100):
#         digit_sum=(i//10) + (i%10)
#         if digit_sum == a:
#             print(i)

#12
# for a in range(10,100,1):
#         for b in range(10,100,1):
#             if b % 10 == 0:
#                 continue  
#             if a%10 == b//10 and a/b == (a//10)/(b%10):
#                 print(f'the numbers are {a} , and {b}')
                
      
            
        
    