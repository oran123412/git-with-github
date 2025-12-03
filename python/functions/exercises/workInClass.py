#1 
# תוכנית שקולטת מספר ובודקת אם חיובי/שלילי
num = int(input("please enter a number to check if he is positive/negative/zero"))
if num>0:
    print("Positive")
elif num == 0:
    print("Zero")
else:
    print("Negative")

#2
#כתוב תוכנית שקולטת מספר ובודקת אם הוא זוגי או אי זוגי 
number = int(input("please enter a number to check if he is even/odd"))
if number%2 == 0:
    print("The number is even")
else:
    print("The number is odd")

#3
#תוכנית שקולטת את שם המשתמש 
age_number = int(input("please enter your age"))
if age_number>=16:
    print("You can enter")
else:
    print("You are too young")

#4
#תוכנית שקולטת 2 מספרים מחשבת ממוצע ומדפיסה
avg_number1 = float(input("please enter a number "))
avg_number2 = float(input("please enter another number "))
avg_total = (avg_number1 + avg_number2)/2
if avg_total>50:
    print("Good average")
else:
    print("Low average")

#6
#תוכנית שקולטת ציון 
grade = int(input("please enter a grade "))
if grade>=90:
    print("Excellent")
elif 60<=grade <=89:
    print("Passed")
else:
    print("Failed")
    
#8
#תוכנית שממירה דקות לשעות ודקות ומדפיסה הערה
minutes = float(input("please enter the minutes "))
hours = minutes//60
if minutes>60:
    print(f"{int(hours)}:{int(minutes%60)} more than an hour")
else:
    print("Less than a hour")
    
#9
#הרשמה של משתמש חדש
email = input("please enter your email: ")
password = input("please enter your password: ")
confirm_password =  input("please enter your password agian: ")
if password == confirm_password:
    print("You have registered successfully")
else:
    print("You have failed to register")