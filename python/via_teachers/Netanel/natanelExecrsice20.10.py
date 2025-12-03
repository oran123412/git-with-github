#                                           תרגילי מחרוזות -לולאות תנאים ומתודות 20.10.25
#                                             *********************************************

#                                                                                                                                 :תרגילים בסיסיים
#1
# first_name=input("Enter first name: ")    
# last_name=input("Enter last name: ")    
# print(f'my name is {first_name} {last_name}')

#                                                                                                                                        :אורך מילה
#2
# word=input("Enter a word name: ")  
# print(len(word))

#                                                                                                                                        :הדפסה כפולה
#3
# sentence=input("Enter a sentence: ")
# print(sentence+ " "+ sentence)

#                                                                                                                                      :ראשון ואחרון 
#4
# word=input("Enter a word name: ")
# print('first letter', word[0:1])
# print('last letter' ,word[-1:-2:-1])

#                                                                                                                      : השוואת מילים -רגישות למקשים 
#5
# word1=input("Enter a word name: ")
# word2=input("Enter a word name: ")
# if word1==word2:
#     print("True")
# else:
#     print("False")

#                                                                                                                                          : II חלק
#                                                                                                                                           ********
#                                                                                                                          : לולאות ותנאים על תווים 
#                                                                                                                                        :'a'  ספירת 
#6

# word=input("Enter a word: ")
# sum_of_letter=0
# for i in word:
#     if i=='a' or i=='A':
#         sum_of_letter+=1
# print(sum_of_letter)

#                                                                                                                                      :ספירת רווחים
#7
# sentence=input("Enter a sentence: ")
# space_count=sentence.count(' ')
# print(space_count)

#8
# word=input("Enter a word with numbers: ")
# list_numbers=[]
# while len(word)>0:
#     digit=word[-1]
#     if digit.isdigit():
#        list_numbers.append(digit)
#     word=word[:-1]
# print(list_numbers)

#9
# sentence=input("enter a sentence: ")
# for c in sentence:
#     if c.isupper():
#         print(c)

#10
# sentence=input("enter a sentence: ")
# no_gap=sentence.replace(" ","")
# print(no_gap)

#11
# answer=input("Do you have a perfect day? ").lower().strip()
# if answer=="yes":
#     print("Proccedd ")
# else:
#     print("Canceled")

#12
# file=input("Please enter your file's name: ").lower()
# if "png" in file or "jpg" in file:
#     print("image file")
# elif "txt" in file:
#     print("text file ")
# else:
#     print("unknown")

#13
# word=input("Please enter your word: ").lower()
# sentence=input("Please enter your sentence: ").lower().split()
# count=0
# for w in sentence:
#     if w == word:
#         count+=1
# print(count)

#14
# word=input("Please enter your word: ").lower()
# old=input("Please enter the old charcter: ").lower()
# new=input("Please enter the new charcter: ").lower()

# if not old in word:
#     print("char not found")
#     exit()
# word=word.replace(old,new)
# print(word)

#15
# sentence=input("Please enter your sentence: ").lower()
# word="pyhton"
# sentence=sentence.find(word)
# if sentence==-1:
#     print("Not found")
# else:
#     print(sentence)

#16
# word=input("Please enter your word: ").lower()
# word=word[::-1]
# print(word)

#17
# sentence = input("Please enter your sentence: ")

# new_sentence = ""
# for i, char in enumerate(sentence):
#     if i % 2 == 0:
#         new_sentence += char.lower()
#     else:
#         new_sentence += char.upper()
# print(new_sentence)

#18
# sentence=input("Please enter your sentence: ")
# length=len(sentence)
# print(length)

#19
# sentence=input("Please enter your sentence: ").lower().strip().replace(" ","")
# if sentence==sentence[::-1]:
#      print("True")
# else:
#     print("False")

#20
password=input("Please enter your password: ").lower()
signs=["$","&","?","!"]
if len(password)>=8 and "a"<=password<="z" and any (s in signs for s in password):
    print("Strong")
else:
    print("Weak")



