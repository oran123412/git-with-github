# mishiaim=[10,20,35,155,55,60,78,88,90,101,125,155]
# months=["January","February","March","April","May","June","July","August","September","October","November","December"]


# max_mishiaim=max(mishiaim)
# min_mishiaim=min(mishiaim)
# min_months=""
# max_months=""
# max_index=[]
# min_index=[]
# print(max_mishiaim)
# print(min_mishiaim)

# for i in range(len(mishiaim)):
#     if mishiaim[i] == max_mishiaim:
#         max_index.append(i)
#     elif mishiaim[i]==min_mishiaim:
#         min_index.append(i)

# for i in max_index: 
#     print(f'the max month is  {months[i]}')
# for i in min_index: 
#     print(f'the min month is  {months[i]}')



# def reverse(number):
#     number=str(number)
#     number=number[::-1]
#     return number    

# def merge(num1,num2):
#     num1=(reverse(num1))
#     num2=(reverse(num2))
#     new_number=""
#     new_digit=0
#     new_digit2=0
#     while num1!="" or num2!="":
#         if num1!="":
#             new_digit=num1[-1]
#             num1=num1[:-1]
#             new_number=new_number + new_digit
#         if num2!="":
#             new_digit2=num2[-1]
#             num2=num2[:-1]
#             new_number=new_number + new_digit2
#     print(new_number)
# merge(1000,5432)

def merge(num1, num2):
    new_number = 0

    # מוצאים את החזקה הכי גדולה של 10 בכל מספר (למשל 1000 עבור 1000)
    pow1 = 1
    if num1 > 0:
        while pow1 * 10 <= num1:
            pow1 *= 10
    else:
        pow1 = 0

    pow2 = 1
    if num2 > 0:
        while pow2 * 10 <= num2:
            pow2 *= 10
    else:
        pow2 = 0

    # כל עוד יש ספרות באחד המספרים
    while pow1 > 0 or pow2 > 0:
        if pow1 > 0:
            digit1 = num1 // pow1   # הספרה הכי שמאלית
            num1 = num1 % pow1
            pow1 //= 10
            new_number = new_number * 10 + digit1

        if pow2 > 0:
            digit2 = num2 // pow2   # הספרה הכי שמאלית
            num2 = num2 % pow2
            pow2 //= 10
            new_number = new_number * 10 + digit2

    print(new_number)


merge(1000, 5432)  # ידפיס 15040302



# matriza=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
# for i in range(len(matriza)):
#     for j in range(len(matriza[i])):
#         print(j,end=" ")
        
#אלכסון ראשי
# sum_of_diagonal=0
# for i in range(len(matriza)):
#     sum_of_diagonal+=matriza[i][i]
# print(sum_of_diagonal)

#אלכסון משני
# sum_of_opposite_diagonal=0
# for i in range(len(matriza)):
#     sum_of_opposite_diagonal+=matriza[i][-i-1]
# print(sum_of_opposite_diagonal)

# numbers=[]
# for i in range(37):
#     numbers.append(i)
# print(numbers)
numbers=[]
# i=1
# while i<37:
#         numbers.append(i)
#         i+=1    
# print(numbers)

# rows = 6
# cols = 6
# lst = []
# k = 1

# for i in range(rows):
#     row = [0] * cols
#     for j in range(cols):
#         if i % 2 == 0:      
#             col_index = j
#         else:                
#             col_index = cols - 1 - j

#         row[col_index] = k
#         k += 1

#     lst.append(row)

# for row in lst:
#     print(*row)



