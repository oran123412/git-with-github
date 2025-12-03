# count_a=0
# count=0
# ch=input("Enter a charcter from the abc")
# if ch=='a':
#             count_a+=1
# while ch !='.':
#     ch=input("Enter a charcter from the abc")
#     if ch =='.':
#         break
#     if 'a'<=ch<='z':
#         if ch=='a':
#             count_a+=1   
#         if count_a and ch =='b':
#             print("operated b")
#             count+=count_a
#             print(count)
#     else:
#         print("only in English")
# print(count)

#ababaabbbaba
# count=0
# i=0
# s1=input("enter long ")
# s2=input("enter short ")

# while i<len(s1):
#     if s1[i:i+len(s2)]==s2:
#         count+=1
#         i+=1
#     else:
#         i+=1
# print(count)


# 600cw580d12ab

# string=input("enter a string: ")
# total=0
# num_str=""

# for chr in string:
#     if chr.isdigit():
#         num_str+=chr
#     else:
#         if num_str!="":
#             total+=int(num_str)
#             num_str=""
# if num_str!="":
#     total+=int(num_str)
# print(total)


# string=input("enter a string: ")
# total=0
# num_str=""
# for chr in string:
#     if chr.isdigit():
#         num_str+=chr
#     else:
#         if num_str!="":
#             num_str=int(num_str)
#             total+=num_str
#             num_str=""
# if num_str!="":
#     num_str=int(num_str)
#     total+=num_str
# print(total)

# def delete_char(st, ch):
#     new_sentence = ""
#     for i in st:
#         if i != ch:
#             new_sentence += i
#     return new_sentence

# print(delete_char("hello,, world", ","))
# def chiper(word,key):
#     new_word=""
#     for i in word:
#         new_word+=chr((ord(i)+key-ord('a'))%26+ord('a'))
#     return new_word
# print(chiper("baby",3))

# def chiper(word,key):
#     new_word=""
#     for i in word:
#         new_word+=chr((ord(i)-key-ord('a'))%26+ord('a'))
#     return new_word
# print(chiper("edeb",3))

#                                                                                             פונקציות                                                                     
#                                                                  ============

# def sum_digits(number):
#     total=0
#     number=str(number)
#     for i in number:
#         total+=int(i)
#     return total


# right=int(input("big number"))
# left=int(input("small number"))
# max_sum=0
# best_num=0
# if left>right:
#     left,right=right,left
# for i in range(left,right+1):
#     s=sum_digits(i)
#     if s>max_sum:
#         max_sum=s
#         best_num=i
# print(best_num,max_sum)


# def reverse(x:int)->int:
#     return int(str(x)[::-1])


# def merge(a:int,b:int)->int:
#     reversed_a=reverse(a)
#     reversed_b=reverse(b)
#     digit_a=0
#     digit_b=0
#     combo=""
#     while reversed_a>0 or reversed_b>0:
#         if reversed_a>0:
#             digit_a=reversed_a%10
#             combo+=str(digit_a)
#             reversed_a//=10
#         if reversed_b>0:
#             digit_b=reversed_b%10
#             combo+=str(digit_b)
#             reversed_b//=10
#     return int(combo)
# merge(1234,5678)        


id_number=input("enter id: ")
sum_digits=0
count=1
for i in id_number:
    if count %2==0:
        i=int(i)*2
        sum_digits+=i
    else:
        sum_digits+=int(i)
last_digit=10-(sum_digits%10)
if str(id_number)[-1]==last_digit:
    print("ok")
else:
    print("no good")
