# def greet(fname,lname):
#     print(f"Hello, {fname} {lname}!")
    
# o="Oran"
# k=6
# greet(o,k)
#פונקציה שמחזירה מינימלי ומקסימלי של ספרות ממספר שקיבלת 

# def sum_digtis(num):
#     negative=num<0
#     num=abs(num)
#     sum_of_digits=0
#     while num>0:
#         sum_of_digits+=num%10
#         num=num//10
#     if negative:
#         return -sum_of_digits
#     return sum_of_digits 
# print(sum_digtis(-19157))

def min_max_digits(num): 
    max_num=min_num=num%10
    while num>0:
        current_number=num%10
        if current_number>max_num:
            max_num=current_number
        if current_number<min_num:
            min_num=current_number
        num=num//10
    return (f"The max number is {max_num} ,the lowest number is {min_num}")

print(min_max_digits(526987441))



