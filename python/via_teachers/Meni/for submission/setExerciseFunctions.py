#                                                           סט תרגילים פונקציות
#                                                          =======================

# #1
# def sum_of_numbers(number):
#     sum_of_digits = 0
#     for digit in str(number):  
#         sum_of_digits += int(digit) 
#     return sum_of_digits


# def find_the_number(left, right):
#     if right <= left or left <= 0 or right <= 0:
#         return "invalid digits"

#     max_sum = 0
#     number_with_max_sum = left

#     for i in range(left, right + 1):
#         current_sum = sum_of_numbers(i)
#         if current_sum > max_sum:
#             max_sum = current_sum
#             number_with_max_sum = i

#     return number_with_max_sum


# print(find_the_number(950, 1050))


#2

# def equalize_digits(number):
#     count_even=0
#     count_odd=0
#     for i in str(number):
#         if int(i)%2==0:
#             count_even+=1
#         elif int(i)%2!=0:
#             count_odd+=1
#     if count_even>count_odd:
#         return "big"
#     if count_even<count_odd:
#         return "small"
#     if count_even==count_odd:
#         return "equal"
    
# print(equalize_digits(1068))
# print(equalize_digits(713))
# print(equalize_digits(25))

#3
# def reverse(x:int)->int:
#     return int(str(x)[::-1])
    
# print(reverse(1293))
# print(reverse(34))
# print(reverse(10))
# print(reverse(3))

#4

# def reverse(x:int)->int:
#     return int(str(x)[::-1])


# def merge(a:int,b:int)->int:
#     combaine_of_two=""
#     new_a=reverse(a)
#     new_b=reverse(b)
#     while new_b>0 or new_a>0:
#         if new_a>0:
#             i=new_a%10
#             new_a=new_a//10
#             combaine_of_two+=str(i)
#         if new_b>0:
#             j=new_b%10
#             new_b=new_b//10
#             combaine_of_two+=str(j)
#     return int(combaine_of_two)
        

# print(merge(1293,3456))
# print(merge(415,34))
# print(merge(27,1009))
# print(merge(2742,100))
# print(merge(2742,100))

#5
# def finding_equal(number):
#     number_str = str(number)
#     left = int(number_str[0:2])
#     right = int(number_str[2:4])
    
#     if (left + right) ** 2 == number:
#         print(number)

# x = 1000
# while x < 10000:
#     finding_equal(x)
#     x += 1

#6
#א
# import math
# def area_ring(small_radius,big_radius):
#     if small_radius==big_radius or small_radius<=0 or big_radius<=0:
#         return "invalid data"
#     if small_radius>big_radius:
#         small_radius,big_radius=big_radius,small_radius
#     small_radius=float(small_radius)
#     big_radius=float(big_radius)
#     big_circule_area=(big_radius**2)*math.pi
#     small_circule_area=(small_radius**2)*math.pi
#     result=big_circule_area-small_circule_area
#     return result

# print(area_ring(3,6))

#ב
# import math
# def area_ring(small_radius,big_radius):
#     if small_radius==big_radius or small_radius<=0 or big_radius<=0:
#         return "invalid data"
#     if small_radius>big_radius:
#         small_radius,big_radius=big_radius,small_radius
#     small_radius=float(small_radius)
#     big_radius=float(big_radius)
#     big_circule_size=big_radius*math.pi*2
#     small_circule_size=small_radius*math.pi*2
#     avg=(big_circule_size+small_circule_size)/2
#     result=avg*(big_radius-small_radius)
#     return result

# print(area_ring(3,6))

#7
#א
# def to_ferenait(chelzios):
#     chelzios=float(chelzios)
#     ferenait=(9*chelzios)/5 +32
#     return ferenait
# print(to_ferenait(35))

#ב
# def to_chelzios(ferenait):
#     ferenait=float(ferenait)
#     chelzios=(ferenait-32)*(5/9)
#     return chelzios

# print(to_chelzios(95))

#ג
# print(f"{'Celsius (°C)'} | {'Fahrenheit (°F)'}")
# print("-" * 27)
# for chelzios in range(-273,102,11):
#     chelzios=float(chelzios)
#     ferenait=(9*chelzios)/5 +32
#     print(f'{chelzios:10.2f}|{ferenait:15.2f}')

#8
# def discover_numbers(start,stop,step):
#     results=[]
#     for i in range(100,1000):
#         i=str(i)
#         if int(i[0])**3 + int(i[1])**3+int(i[2])**3==int(i):
#             results.append(i)
#     return results
# print(discover_numbers(100,1001,1))        

#9
# def reverse(x:int)->int:
#     return int(str(x)[::-1])
# for i in range(10000,100000):    
#     if i*4==reverse(i):
#         print(i)

#10
sum_of_digits = 0
id_number = input("enter a 9-digit ID number: ")
id_number = str(id_number)

if len(id_number) != 9 or not id_number.isdigit():
    print("Invalid input! Please enter exactly 9 digits.")
else:
    for i in range(8):  
        if i % 2 == 0:
            digit = int(id_number[i]) * 1 
        else:
            digit = int(id_number[i]) * 2  
            if digit > 9:
                digit = digit // 10 + digit % 10 
        sum_of_digits += digit

    remain = sum_of_digits % 10
    if remain == 0:
        security = 0
    else:
        security = 10 - remain

    if security == int(id_number[-1]):
        print("The ID number is valid!")
    else:
        print("The ID number is invalid!")





