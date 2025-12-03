# #5
# #כתוב תוכנית שקולטת 3 מספרים ומדזפיסה את הגדול ביותר

# num1=int(input("Please enter the first number "))
# num2=int(input("Please enter the second number "))
# num3=int(input("Please enter the third number "))
# if num1>=num2 and num1>=num3:
#     print(f"{num1} is the biggest number")
# elif num2>=num1 and num2>=num3:
#     print(f"{num2} is the biggest number")
# else:
#     print(f"{num3} is the biggest number")

#9
#חישוב שטח מעגל
# pi=3.14
# radius=float(input("Plese enter the radius number "))
# surface = pi*(radius**2)
# print(f"The surface of the circle is {surface}")
# if surface>100:
#     print("Big circle")
# else:
#     print("Small circle")
    
#Exercise with Aviv 9.9.25:
#1.
#A man wants to buy a motorcycle he has expenses and income . calculate the number of monthes till he buys it.
# income = int(input("Please enter you income"))
# expenses = int(input("Please enter you expenses"))
# cost = int(input("Please enter the cost of the motorcycle"))
# dis = income - expenses
# if dis<=0:
#     print("You cant buy the motorcycle")
# else:
#     print(f"You can buy the motorcycle in {cost/dis :.2f} monthes")
    
#2
#Program a plan that solves the equation Ax+B=0,receive the parameters A,B . Show value of X no resolve or endless soultions
# parameterA=int(input("Please enter the A parameter"))
# parameterB=int(input("Please enter the B parameter"))
# if parameterA==0:
#     if parameterB==0:
#         print("infinity")
#     else:
#         print("no x")
# else:
#     print(f"x = {-parameterB/parameterA}")

#3
#program that calculates the amount of money needed to pay for wadding 

# family = input("Are you family member ? (True/False) ")
# if family == "True":
#     print("As a faimily member you need to pay 1000 for the wedding ")
# else:
#     friend = input("Are you close friend ? (True/False) ")
#     know_for_3_years = input("Do you know them for more than 3 years ? (True/False) ")
#     distance = input("Is the wedding located  more than 1 hour of driving ? (True/False) ")

#     if friend == "True":
#         if know_for_3_years == "True" and distance == "True":
#             print("you need to pay 600 for the wedding ")
#         if know_for_3_years == "False" and distance == "True":
#             print("you need to pay 550 for the wedding ")
#         if know_for_3_years == "False" and distance == "False":
#             print("you need to pay 500 for the wedding ")
#         if know_for_3_years == "True" and distance == "False":
#             print("you need to pay 550 for the wedding ")
#     else:
#         if know_for_3_years == "True" and distance == "True":
#             print(" you need to pay 350 for the wedding ")
#         if know_for_3_years == "False" and distance == "True":
#             print(" you need to pay 300 for the wedding ")
#         if know_for_3_years == "False" and distance == "False":
#             print(" you need to pay 250 for the wedding ")
#         if know_for_3_years == "True" and distance == "False":
#             print(" you need to pay 300 for the wedding ")

#4
#program a library subscription program 
time_of_barrowing = int(input("If you have book at home how many days you are barrowing  it till this day ? "))
if time_of_barrowing >30:
    print("You cant barrow any more books")
    exit()
books_at_home = int(input("How many books do you currently have at home? "))
age = int(input("What is your age? "))
if age<18:
    if books_at_home>=3:
        print("You cant barrow any more books")
    else:
        print("Enjoy your new book!")
       
else:
    if books_at_home>=5:
         print("You can't borrow any more books (adults' limit is 5).")
    else:
        print("Enjoy your new book!")   



#The teacher's way of solving this question
#adult = 5
#kid = 3 
# age = int(input("What is your age ? "))
# book = int(input("How many books do you have ? "))
# if age >=18:
#     temp = 5 - book
# else:
#     temp = 3 - book

# ask = int (input("how many time (days?): "))

# if ask >= 30 or temp <= 0:
#     print("sorry you cant barrow")
# else:
#     print(f"you can take {temp} books home")
     
#5
#If a student can be aceepted for studies at college "Liliput"
# bagrut_avg = float(input("What is the average of your Bagrut ? "))

# if bagrut_avg>=102:
#     print("You can start learning in our college")
#     exit()
# else:
#     psychometric_avg = int(input("What is the grade of your psychometric ? "))
#     english_part = int(input("What is the grade of your English-part ? "))
#     count_part = int(input("What is the grade of your count-part ? "))
#     total_sum_grades = (bagrut_avg*1.2)/0.8 + psychometric_avg 
#     if  psychometric_avg >=700 and english_part>=120 and count_part>=145:
#         print("You can start learning in our college")
#     elif total_sum_grades > 600:
#         print("You can start learning in our college")
#     else:
#         print("You grades aren't enougth for learning in our college")
        
    
    
    
