#                                                                  תרגול למבחן מחרוזות
#                                                               ==========================

#1
#א
# count_a=0
# count=0

# chr=input("Enter a charcter to finish press '.' : ")
# if chr=='a':
#     count_a+=1
# while chr!= '.' :
#     chr=input("Enter a charcter to finish press '.' : ")  
#     if 'a'<=chr<='z':
#         if chr=='a':
#             count_a+=1
#         if chr=='b' and count_a>0:
#             count+=count_a
#     else:
#         print("Enter only english letters ") 
# print(count)
#    acbsabcba

#ב
# count_a=0
# count=0

# chr=input("Enter a charcter to finish press '.' : ")
# if chr=='a':
#     count_a+=1
# while chr!= '.' :
#     chr=input("Enter a charcter to finish press '.' : ")  
#     if 'a'<=chr<='z':
#         if chr=='a':
#             count_a+=1
#         if chr=='b' and count_a>0:
#             count+=count_a
#         if chr=='c':
#             count_a=0
#     else:
#         print("Enter only english letters ") 
# print(count)

#    acbsabcba

#ג
# count_a=0
# count_c=0
# count=0

# chr=input("Enter a charcter to finish press '.' : ")
# if chr=='a':
#     count_a+=1
# while chr!= '.' :
#     chr=input("Enter a charcter to finish press '.' : ")  
#     if 'a'<=chr<='z':
#         if chr=='a':
#             count_a+=1
#         if chr=='c':
#             count_c+=1
#         if count_c>1:
#             count_a=0
#             count_c=0
#         if chr=='b' and count_a>0 and count_c==1:
#             count+=count_a
#             count_c=0
#     else:
#         print("Enter only english letters ") 
# print(count)

# dsacbsabcbxxa

#2
# strings_under_condition=""
# for i in range(15):
#     string=input("enter a string: ")
#     if string[0]==string[-1]:
#         strings_under_condition+=string+","
# print(strings_under_condition[:-1])

#3
# long_string=input("Enter a long string: ")
# short_string=input("Enter a short string: ")
# if len(long_string)>=2*len(short_string):
#     print(long_string)
# else:
#     print(short_string)

#4
# count=0
# s1=input("Enter a long string: ")
# s2=input("Enter a short  string: ")
# for i in range(len(s1)-len(s2)+1):
#     if s1[i:i+len(s2)]==s2:
#         count+=1
# print(count)
#ababaabbbaba

#5

# def sum_numbers_in_string(string):
#     total = 0
#     num_str = ""  
   
#     for char in string:
#         if char.isdigit():
#             num_str += char    
#         else:
#             if num_str != "":
#                 total += int(num_str)
#                 num_str = ""          
                             
#     if num_str != "":
#         total += int(num_str)      
#     return total
# print(sum_numbers_in_string("600cw580d12ab"))

#6
# def delete_char(st,ch):
#     st=st.replace(ch,"")
#     return st
# print(delete_char("e-r-e-t-z-n-e-h-e-d-e-r-e-t","-"))

#7
# def chiper(string,key):
#     new_string=""
#     for ch in string:
#         if 'a'<=ch<='z':
#                 ch=(ord(ch)-ord('a')+key)%26
#                 ch=chr(ch+ord('a'))
#                 new_string+=ch
#         if 'A'<=ch<='Z':
#                 ch=(ord(ch)-ord('A')+key)%26
#                 ch=chr(ch+ord('A'))
#                 new_string+=ch
#     return(new_string)
        

# print(chiper("baby",3))

# def opposite(string,key):
#     new_string=""
#     for ch in string:
#         if 'a'<=ch<='z':
#             ch=(ord(ch)-ord('a')-key)%26
#             ch=chr(ch+ord('a'))
#             new_string+=ch
#         if 'A'<=ch<='Z':
#             ch=(ord(ch)-ord('A')-key)%26
#             ch=chr(ch+ord('A'))
#             new_string+=ch
#     return(new_string)

# print(opposite('edeb',3))




#                                                                 תרגול למבחן פונקציות
#                                                               ==========================


#1

# def from_number_to_sum_digits(number):
#     sum_of_digits=0
#     for digit in str(number):
#         digit=int(digit)
#         sum_of_digits+=digit
#     return sum_of_digits
    

# right=int(input("Enter a big number: "))
# left=int(input("Enter a small number: "))
# if right<left:
#     right,left=left,right
# elif right==left:
#     right=int(input("Enter a big number: "))
#     left=int(input("Enter a small number: "))

# max_digit_number=0
# for i in range(left,right+1):
#     sum_digits=from_number_to_sum_digits(i)
#     if sum_digits>max_digit_number:
#         max_digit_number=sum_digits
# print(max_digit_number)
    
    
#2
# count_even=0
# count_odd=0
# number=int(input("Enter a number: "))
# while number<=0:
#     number=int(input("Enter a number which is positive: "))
    
# for i in str(number):
#     if int(i)%2==0:
#         count_even+=1
#     else:
#         count_odd+=1
# if count_even>count_odd:
#     print("big")
# elif count_even<count_odd:
#     print("small")
# elif count_even==count_odd:
#     print(" equal")

#3
# def reverse(x:int)->int:
#     x=str(x)
#     x=x[::-1]
#     return int(x)
    
# print(reverse(1293))
# print(reverse(10))
# print(reverse(43))

#4
# def merge(a:int,b:int)->int:
#     new_number=""
#     digit=0
#     while a<0 or b <0:
#         a=int(input("Enter only positive numbers"))
#         b=int(input("Enter only positive numbers"))
#     a=reverse(a)
#     b=reverse(b)
#     while a>0:
#         digit=a%10
#         new_number+=str(digit)
#         a=a//10
#         if b>0:
#             digit=b%10
#             new_number+=str(digit)
#             b=b//10
#     while b>0:
#         digit=b%10
#         new_number+=str(digit)
#         b=b//10
#     return int(new_number)
         
    
# print(merge(1293,3456))
# print(merge(415,34))
# print(merge(27,1009))

#5
# for i in range(1000,9900):
#     i=str(i)
#     left=int(i[0:2])
#     right=int(i[2:4])
#     if (left+right)**2 == int(i):
#         print("the condition has operated")
#         print(i)
        
        
#6
# #א
# small_radius=int(input("Enter small radius: "))
# big_radius=int(input("Enter big radius: "))
# if small_radius>big_radius:
#     small_radius,big_radius=big_radius,small_radius
# while small_radius==big_radius:
#     small_radius=float(input("Enter small radius: "))
#     big_radius=float(input("Enter big radius: "))
# small_circule_area=(small_radius**2)*3.14
# big_circule_area=(big_radius**2)*3.14
# ring_area=big_circule_area-small_circule_area
# print(ring_area)

# #ב
# width_of_ring=big_radius-small_radius
# big_c=2*3.14*big_radius
# small_c=2*3.14*small_radius
# ring_area=((big_c+small_c)/2)*width_of_ring
# print(ring_area)

#7
#א
# def to_phernait(chelzios_degree):
#     new_degree=(chelzios_degree*9)/5+32
#     return new_degree
    
# print(to_phernait(35))
# #ב
# def to_chelzios(phernait_degree):
#     new_degree=(phernait_degree-32)*(5/9)
#     return new_degree
# print(to_chelzios(95.0))

# #ג
# print(f"{'Chelzios':^12}|{'fernahit':>15}")
# print("-"*30)
# for i in range(-273,101,11):
#     print(f'{i:^12}|{to_phernait(i):>15.2f}')

#8
# for i in range(100,1000):
#     i=str(i)
#     first_digit= int(i[0])
#     second_digit=int(i[1])
#     third_digit= int(i[2])
#     if first_digit**3 + second_digit**3 + third_digit**3 == int(i):
#         print(i)

#9
# for i in range(10000,100000):
#     if i*4==reverse(i):
#         print(i)

#10
# sum_of_digits=0
# idfiction=input("enter your i.d.: ")
# for i in range(len(idfiction)-1):
#     if i%2!=0:
#         new_duplicated_number=int(idfiction[i])*2
#         if new_duplicated_number>9:
#             new_duplicated_number=str(new_duplicated_number)
#             new_duplicated_number=int(new_duplicated_number[0])+int(new_duplicated_number[1])
#             sum_of_digits+=new_duplicated_number
#         else:
#             sum_of_digits+=new_duplicated_number
#     else:
#         sum_of_digits+=int(idfiction[i])
# print(sum_of_digits)
# safety_digit=10-(sum_of_digits%10)
# print(safety_digit)
# if int(idfiction[8])==safety_digit:
#     print("correct i.d.")
# else:
#     print("incorrect i.d")