# def factorial(n:int)->int:
#     if n==0 or n==1:
#         return 1
#     else:
#         return n* factorial(n-1)
        
# print(factorial(5))



def fib(n: int) -> int:
    if n <= 1:
        return 1
    
    a, b = 1, 1
    for _ in range(2, n):
        a, b = b, a + b
    
    return b

print(fib(5))
print(fib(10))


# a=[1,3,5,7]
# b=[2,4,6,8]
# c=[]
# a=[11,33,44,77]
# b=[22,55,66,88]
# c=[]


# def Merge(a:list[int],b:list[int],c:list[int]):
#     c.clear
#     while len(a)>0 and len(b)>0:
#         if a[0]<=b[0]:
#             c.append(a.pop(0))
#         else:
#             c.append(b.pop(0))
#     if len(a)>0:
#         c.append(a.pop(0))
#     else:
#         c.append(b.pop(0))
    
# Merge(a,b,c)
# print(a,b,c)


#כתוב פונקציה שמקבלת מחרוזת ומחזירה לנו את המחרוזת הפוכה ברקורסיה

# def reverse_string(s:str)->str:
#     if len(s) ==0:
#         return s
#     else:
#         return s[-1]+ reverse_string(s[:-1])

# print(reverse_string("hello"))
    

#כתוב פונקציה שמקבלת מחרוזת ותבדוק אם היא פולנידרום בצורה רקרוסיבית
# def polindrom(s):
    
#     if len(s) ==0 or len(s) == 1 :
#         return True
#     else:
#         return s[-1]==s[0] and polindrom(s[1:-1])
    
# print(polindrom("abcda"))
