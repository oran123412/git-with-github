#exercise  1 
#כתוב תוכנית שמבקשת מהמשתמש את שמו ומברכת אותו.
#name = input("Please enter your name")
#print("Hello", name , "it's nice to meet you")
#print(ord('C'))
#print(chr(67))
#chr ,ord פעולות הפוכות
#print(ord('A'))
#print(ord('a'))
#print(ord('H'))
#print(ord('K'))
#print(chr(66))
#print(chr(98))
#print(chr(122))

#עצירה קטנה נסו זאת בעצמכם 
#note = "Make a big macrozet as you wish"
#if note.isupper():
#     print("yes")
#else :
#     print("no")

#note = "Make a big macrozet as you wish"
#if note[0].isupper():
#     print("yes")
#else :
#     print("no")

#answer = input("Please fill in a sentence as you wish")
#if "!" in answer:
#    print("yes")
#else: 
#    print("no")

#password = input("please create a password")
#if password[0].isupper() and any(letter in password for letter in ["!","#","&"]):
#    print("Great password")
#else:
#    print("password must containe capital letter at the first letter & must containe &/!/#")

#name = ["ggngkdfjsngldskflkgg"]
#name = name.strip("g")
#print(name)
#name = name.capitalize()
#print(name)
#name = name.replace("g","Q")
#print(name)
#name_str = name[0]  # הוצא את המחרוזת מהרשימה
#name_sorted = ''.join(sorted(name_str))  # מיון האותיות במחרוזת
#print(name_sorted)

#trying = "ello my name is oran"
#trying = trying.strip("Holn")
#print(trying)
#trying = trying.capitalize()
#print(trying)

#תרגילי חזרה
#1.
#string = "How are you doing!?"
#if string[0].isupper():
#    print("valid")
#else:
#    print("invalid")
#2.
#name = input("please enter your first name")
#name = name.capitalize()
#print(name)
#last_name = input("please enter your last name")
#last_name = last_name.capitalize()
#print(last_name)
#3.
#sentence = input("please write a sentence and see the magic !!!!")
#sentence = sentence.replace("a","1").replace("b","2").replace("c","3")    
#print(sentence)
#4.
#phrase = input("Please enter a phrase or coaple of sentences")
#if "!" in phrase and phrase[0].isupper() and phrase[-1].islower:
#    print("valid")
#else:
#    print("invalid") 
#5.
#phrase = input("Please enter a phrase or coaple of sentences")
#if len(phrase)<8 or "#" in phrase or phrase.count("1") < 2:
#    print("invalid")
#else:
#    print("valid")
6.
email = input("lets check your email account if it's valid")
if email.count("@") == 1 and "gmail.com" in email and email[0] != "@":
    print("valid")
else:
    print("invalid") 