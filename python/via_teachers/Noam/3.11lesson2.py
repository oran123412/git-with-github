#                                                        lesson number 2 - functions
#                                                       =============================

#1 Can you define a function inside a function?
#Answer:
#Yes, you can that is exactly what "nested function" is.

#2 What is a pure function?
#Answer:
#A pure function always returns the same output for the same input and has no side effects (does not change external variables, lists, dicts, or print).


#3 What is "Pure function" and "Higher-order function"?  Define it in one sentence.
# Give 3 examples for each of them.
#Answer:
#"high-order function" or "HOFs" are functions that use other functions as an argument and works with other functions as they are regular data while pure function is a function that given the same input will generate the same outcome.
#examples for pure functions :
#def add(a, b):
#     return a + b

# def square(x):
#     return x * x

#def divide(a,b):
#   return a/b

# Examples for HOFs (fixed)

# def once(func):
#     print("Calling function inside once:")
#     func()  

# def add():
#     print("oran")

# once(add) 


# def once(func):
#     print("Calling function inside once:")
#     func()

# def add():
#     print("osher")

# once(add)  


# def once(func):
#     a = 2 + 5
#     print("Calling function with a computed value inside once:")
#     func(a)  

# def add(value):
#     print(value)

# once(add)  


#4 What will be printed by the following Python code?
# def outer():
#     x = 10
#     def inner():
#         x = 3  
#         return x
#     return inner(), x

# print(outer())

#Answer:
#I assume the result will be : inner() = 3, outer() = (3,10).

#5 What will be printed, and why?
# def outer():
#     x = 5
#     def inner():
#         return x + 2
#     return inner()
# print(outer())

#Answer:
#I believe it will print 7
#                        7
#because the inner function returns 7 and another one of 7 

#6 Modifying a variable from the enclosing scope:
#     The following code raises an error. What is the error and why? Fix it so it prints 1, then 2, then 3.
# def make_counter():
#     count = 0
#     def inc():
#         count += 1
#         return count
#     return inc

# c = make_counter()
# print(c()); print(c()); print(c())

#When you want to call a variable that is possiable eventhough its not in the function itself but to change the value of it you must state gloabl or eclosing in order for it to work .
#the way to fix it :
# def make_counter():
#     count=0
#     def inc():
#         nonlocal count
#         count += 1
#         return count
#     return inc

# c = make_counter()
# print(c()); print(c()); print(c())


#7  What are the criteria that must be met to create closure in Python?
#Answer:
#A closure is an inner function that references variables from its enclosing scope and is used after the outer function finishes. 
#Nonlocal is only needed if you want to modify those variables.


#8 What does the `nonlocal` keyword mean in Python?
#Answer:
#nonlocal allows you to modify variables captured by a closure.

    # - What is the difference between `nonlocal` and `global`? Give a useful example of each.
    #Answer:nonlocal is needed to change an enclosing variable and global in order to change a global vairable which is outside any function .
    #global:
    #x=5
    #def change(double_change):
    #   print("hi")
    #   def double_change(a):
    #       global x
    #       x+=5
    
    #enclosing:
    # def make_counter():
    #     count=0
    #     def inc():
    #         nonlocal count
    #         count += 1
    #         return count
    #     return inc

    # c = make_counter()
    # print(c()); print(c()); print(c())
    
    # - In which scope must the variable referred to by `nonlocal` live?
    #Answer:
    #enclosing scope
    
    # - What happens if you use `nonlocal` for a name that doesn’t exist in any enclosing scope?
    #Answer:It will raise a syntaxError
    
    # - Why can you get an `UnboundLocalError` without `nonlocal` even if a same-named variable exists outside?
    #Because when you use the operator '=' Python assumes that the variable is in the function itself and not outside of the same scope.
    
    # - When is it appropriate to use `nonlocal`, and when is it better to return a value and pass it forward (avoiding state changes)?
    #Answer: When you want to keep the function pure , but if you want to adjuste and save changes in the variable use 'nonlocal'
    
    # - Can `nonlocal` refer to a global variable? Explain.
    #Answer:No nolocal can only refer to variables that are in enclosing scope.
    
    # - Can you use more than one name in a single `nonlocal` statement? What does it mean?
    #Answer:Yes.It means that its a tuple.
    
    # - How is `nonlocal` related to **closures**?
    #Its a tool to use in order to make closures
    
    # - How can you avoid using `nonlocal` by using mutable data structures (like a dict/list)?
    #Answer:By using loops indexes keys and values.
    
#9 Predict the Output:
# Question: What will be printed?
# x = 10

# def outer():
#     x = 5
#     def inner():
#         # Try to predict what happens here
#         x += 1
#         print(x)
#     inner()

# outer()
#Answer:UnboundLocalError, because inner tries to modify x without nonlocal.


# ​
# 	def make_counter():
#     count = 0
#     def inc():
#         nonlocal count
#         count += 2
#         return count

#     print(inc(), inc(), count)

# make_counter()
#Answer:# Output: 2 4 4 

#10
# Explain in one sentence what *args collects and what **kwargs collects inside a function.
#Answer:They collect arguments inside a function.
# What data types do *args and **kwargs become inside the function body?
#Answer:*args changes it to tuple and **kwargs to dictionary.

#12 Predict the output:

# def f(a, *args, **kwargs):
#     print(a, args, kwargs)

# f(1, 2, 3, x=10, y=20)
#Answer:In my opinion the result will be 1
#(2,3)
#{x:10,y:20}

#13
# What will be printed and why?
# def total(*nums):
#     return sum(nums)

# print(total())        # ?
# print(total(4))       # ?
# print(total(1,2,3))   # ?
#Answer:0,4,6
# ​
#14 Identify the bug and correct it:
# def f( *args,a=1, **kwargs):
#     return a
#The problem is the order of the parameters.

#lambada 24.11                                                                                     ==============                             

#1                              

# lst=["hi","hello","wow","momtaz"]
# remove=filter(lambda x:x !="hi" , lst)
# print(list(remove))

#2
# numbers = ["12", "3", "100", "25", "8", "50"]
# organize=sorted(numbers,key=lambda x:(int)(x))
# print(list(organize))

#3
# numbers=[5, -3, 12, -1, -4, 7]
# sum_positive=sum(filter(lambda x:x >0 ,numbers))
# sum_negative=sum(filter(lambda x:x <0 ,numbers))
# print(f'the positive is {sum_positive} the negative is {sum_negative}')

#4
# numbers=[5, -3, 12, -1, -4, 7,8]
# new_numbers=[ x**2 for x in numbers if x%2 ==0]
# print(new_numbers)

#5
# products = {
#     "Milk": 5.90,
#     "Bread": 6.50,
#     "Chocolate": 12.00,
#     "Pasta": 8.40,
#     "Rice": 9.90
# }

# def apply_sale(d):
#     return dict(map(lambda item: (item[0], round(item[1] * 0.9, 2)), d.items()))

# updated_products = apply_sale(products)
# print(updated_products)

#6
# card_number=list(input("Enter your credit number: "))
# sum_numbers=0
# for i in range(len(card_number)-1,-1,-1):
#     card_number[i]=int(card_number[i])
#     if (len(card_number)-i)%2==0:
#         card_number[i]=card_number[i]*2
#         if card_number[i]>9:
#             card_number[i]=card_number[i]-9
#     sum_numbers+=card_number[i]
# if sum_numbers%10==0:
#     print("Valid")
# else:
#     print("not valid")

#Lambda Functions – Exercises 
# 1.12

#1
# words = (
#     "apple",
#     "sun",
#     "banana",
#     "tree",
#     "light",
#     "sky",
#     "python",
#     "car",
#     "window",
#     "door",
#     "notebook",
#     "pen",
#     "mouse",
#     "code",
#     "energy"
# )
# result=tuple(filter(lambda x:len(x)%2==0 ,words ))
# print(result)

#2
# words = (
#     "apple",
#     "sun",
#     "banana",
#     "tree",
#     "light",
#     "sky",
#     "python",
#     "car",
#     "window",
#     "door",
#     "mouse",
#     "energy"
# )
# result=sorted(words,key=lambda x:x[-1])
# print(result)
        

