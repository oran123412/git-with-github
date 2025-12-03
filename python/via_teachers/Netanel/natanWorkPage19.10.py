#1
# def welcome():
#     print("Welcome to functions in Python!")
# welcome()
# welcome()

#2
# def greet(name):
#     print("hello" ,name)
# greet("Oran")
# greet("Moshe")
# greet("Yakov")

#3
# def full_name(first,last):
#     if type(first) != str or type(last) != str:
#         return print(("invalid name "))
#     print(first,last)
# full_name("Ana","Cohen")
# full_name("Or","Levy")
# full_name("Bob","Moshe")


#4
# def rectangle_area(length,width):
#     if  length<=0 or width <= 0:
#         return("the width and length must be positive")
#     return(length*width)
# print(f'The rectangle area is {rectangle_area(7,3)}')
# print(f'The rectangle area is {rectangle_area(-7,3)}')
# print(f'The rectangle area is {rectangle_area(7,0)}')

#5
# def avg(a,b):
#     return((a+b)/2)
# print(avg(3,6))

#6
# def max2(a,b):
#     if a>b:
#         return a
#     if b>a:
#         return b
# print(max2(5,3))
# print(max2(-4,1))
# print(max2(0,5))

#7
# def is_even(n):
#     if n%2==0:
#         return True
#     else:
#         return False
    
# print(is_even(3))
# print(is_even(0))
# print(is_even(-3))
# print(is_even(4))

#8
# def with_vat(price,vat_percent):
#     if price<=0 or vat_percent>100 or vat_percent<0:
#         return "invalid input"
#     return (price + (price*vat_percent/100))
# print(with_vat(30,18))
# print(with_vat(0,18))

#9
# def grade_status(grade):
#     if type(grade) != int or grade<0 or grade>100  :
#         return "invalid input"
#     if grade>=90:
#         return("Excellent")
#     elif grade>=60:
#         return("Passed")
#     else:
#         return("Failed")
    
# print(grade_status(90))
# print(grade_status(63))
# print(grade_status(20))
# print(grade_status(-20))
# print(grade_status(0))
# print(grade_status(200))
# print(grade_status("gcf"))

#10

# def pow_int(base,power):
#     result=1
#     if power>0:
#         for _ in range(power):
#             result*=base
#     elif power <0:
#         for _ in range(-power):
#             result*=base
#         result=1/result
#     return result
# print(pow_int(2,3))
# print(pow_int(2,-3))
# print(pow_int(-2,-3))
# print(pow_int(22,3))
# print(pow_int(0,3))
# print(pow_int(-2,3))

#11
# def product_range(a,b):
#     if not isinstance(a,(int)) or not isinstance(b,(int)):
#         return "invalid input"
#     result=1
#     step=1
#     stop=b+1
#     if b<=a:
#         step=-1
#         stop=b-1
#     for i in range(a,stop,step):
#         result*=i
#     return result
# print(product_range(2,5))
# print(product_range(-2,-5))
# print(product_range("d","A"))


#12
# def rectangle_area(length,width):
#     return(length*width)


# def compare_rectangle(l1,w1,l2,w2):
#     area1=rectangle_area(l1,w1)
#     area2=rectangle_area(l2,w2)
#     if area1>area2:
#         return("Rectangle 1 is bigger")
#     elif area2>area1:
#         return("Rectangle 2 is bigger")
#     else:
#         return("Equal areas")
# print(compare_rectangle(3,9,9,3))

#13
# def square(x):
#     result=x
#     result*=x
#     return result


# def sum_of_squares(n):
#     if n<0 or type(n)==float:
#         return "enter a positive int number"
#     result=0
#     for i in range(1,n+1):
#         result+=square(i)
#     return result

# print(sum_of_squares(7))
# print(sum_of_squares(-7))
# print(sum_of_squares(3.5))


#14
# def is_divisable(a,b):
#     if a%b==0:
#         return True
#     else:
#         return False

# def is_prime(n):
#     if n<2:
#         return False
#     for i in range(2,n):
#         if is_divisable(n,i):
#             return False
#     return True
    
# print(is_prime(5))
# print(is_prime(-5))
# print(is_prime(0))
    
#15
# def grade_status(grade):
#     if grade>=90:
#         return("Excellent")
#     elif grade>=60:
#         return("Passed")
#     else:
#         return("Failed")

# def grade_summary(g1,g2,g3):
#     grades=[g1,g2,g3]
#     for grade in grades:   
#         print(grade,grade_status(grade))
# grade_summary(97, 63, 22)

