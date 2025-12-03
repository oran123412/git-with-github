#שאלות על לולאות 15.9 
#עליכם לכתוב תכנית מחשב המקבלת כקלט שני מספרים שלמים ) לאו דווקא חיוביים(,
#ומציגה כפלט את סכום כל המספרים השלמים שביניהם .לדוגמא :עבור הקלט 3 , 1 יהיה הפלט: 6
#)כי 6=1+2+3 (
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

#כתבו תכנית מחשב אשר קולטת שני מספרים שלמים M , N הגדולים שניהם מ .1- לאחר
#מכן התכנית תקלוט רשימה של N מספרים שלמים וחיוביים)טבעיים(.
#התכנית תבדוק האם קיימים בקלט זוג מספרים כלשהם )לאו דווקא עוקבים( אשר סכומם גדול
#מ M , ותציג כפלט הודעה מתאימה.

# m =int(input("enter the 'm' number"))
# n =int(input("enter the 'n' number"))
# flag_bigger = False
# max_num=0


# for i in range(1,n+1,1):
#     input("Enter a number")
#     if max_num+i>m:
#         flag_bigger = True
#     else:
#         flag_bigger = False
#     if i > max_num:
#         max_num=i
       
# if (flag_bigger):
#     print("the sum of the numbers are bigger than 'n'")
# else:
#     print("the sum of the numbers are smaller than 'n'")

#כתבו תכנית מחשב אשר מקבלת כקלט מספר שלם וחיובי )טבעי( הקטן מ 86,400 המציין את
#מספר השניות שחלפו מאז תחילת היממה ,ותציג כפלט את השעה הנוכחית.
#לדוגמא :עבור הקלט , 49,635 יוצג הפלט: 13:47:15 .
# whole_number=int(input("please enter a number which is less than 86,400: "))
# hours=whole_number//3600
# minutes=(whole_number%3600)//60
# seconds=(whole_number-hours*3600-minutes*60)
# print(f'{hours}:{minutes}:{seconds}')
