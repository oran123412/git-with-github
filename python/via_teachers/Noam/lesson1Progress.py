#                                                          Data Structures-Noam  
#                                                        ========================



#Questions:
#=========

#1 List mutable and immutable objects in Python.
#2 What happens when you increment an int? Investigate with ID.
#3 How do you switch two variables in one line of code?
#    - Can you do it for more than two variables?
#    - How does it work?
#4 How can you loop over all the elements in a data structure?
#5 What is the difference between == and is ?
#6 Can you delete an element inside a data structure?
#7 Explain slicing in Python. How many arguments does slicing need? 
# How many arguments can it receive?
#8 Can you mix all types of elements in all data structures?
#9 List the ordered and the unordered data structures.



#Answers:

#1 mutable is a list,set and dict for instance.Immutable are tuple,int,float,string and bool

#2 Since 'int' is immutable his id() will be diffrent :
#n=5 
#print(id(n))
#n=n+1
#print(id(n))

#3 a=9
# b=7
# a,b=b,a
# print(a)
# print(b)

# Yes

#The reason is that in the left side is created a temporary   varibales and in the right side temporary tuple . The program takes the tuple and dived it into two and make application by order 

#4 Loops.

#5 The operator of'==' is a boolean operator to cheack if the right side is equal to the left side and it returns true or false.
#  'is' checks if the variables refer to the same object in memory

#6 It dependes on the elment if it is mmutable or not . If its is muutable you can if not , not .

#7 Slicing is a method to change the data using index . There are two ways to do it one way is you can  create a slice object with slice(start, stop, step) and apply it to a sequence, like lst[s]. or in a short way of [start:stop:step] . it needs at least one argument and at most can recieve 3  

#8 No,it dependes on the container , in list ,tuple,dict and set you can , on string,int,float,bool you can't since they posess only one element.

#9 Ordered-dict,list,tuple. Not oredered-set.



## **What will the following programs print? Explain why.**

# ```python
# >>> a = 1
# >>> b = 1
# >>> print(a == b, a is b)
# ```

#answer:(True,True)

# ```python
# >>> a = 55555

# >>> b = 55555

# >>> print(a == b, a is b)
# ```
#answer:(True,False)

# ```python
# >>> a = ()

# >>> b = ()

# >>> print(a == b, a is b)
# ```
#answer:(True,True)

# ```python
# >>> a = (1, 2, 3)

# >>> b = (1, 2, 3)

# >>> print(a == b, a is b)
# ```
#answer:(True,False)

# ```python
# >>> a = [1, 2, 3]

# >>> b = a[:]

# >>> print(a == b, a is b)
# ```

#answer:(True,False) 

# ```python
# >>> x = [1, 2, 3]

# >>> y = x

# >>> y[0] = 8

# >>> print(x)
# ```
#answer:x = [8, 2, 3]

# ```python
# >>> x = (1, 2, 3)

# >>> y = x

# >>> y[0] = 8

# >>> print (x)
# ```
#answer:Type error

# ```python
# >>> x = 1

# >>> y = x

# >>> y = 2

# >>> print (x)
# ```
#answer:x = 1

# ```python
# >>> a = None

# >>> b = None

# >>> print(id(a) == id(b))
# ```
#answer:True

# ```python
# x = 'DevOpsMeGo'

# print(x[-1:-2])
#answer:''

# print(x[3:-1])
#answer:OpsMeG

# print(x[:1])
#answer:D

# print(x[:3])
#answer:Dev

# print(x[::-1])
#answer:oGeMspOveD
# print(x[1::-1])
#answer:eD
## 


# 1. Write a function that receives a string and returns a dictionary in which each character maps to the number of its occurrences.

#Answer:
# my_dict={
# }
# def location_letters(name):
#     for char in name:
#         value=name.count(char)
#         my_dict[char]=value
               
#     return my_dict
# location_letters("Oran")

# 2. Write a function that receives a list and removes from it all objects that are not strings.

#Answer:
# def only_string(lst):
#  lst[:] = [i for i in lst if isinstance(i, str)]
#  print (lst)
# only_string([11,"hi",9,5.5,"like",True])

# 3. Write a function that receives two lists and returns a list containing only the elements that appear in both lists.

#Answer:

# def two_becomes_one(list1,list2):
#     list3=[]
#     for i in list1:
#         for j in list2:
#             if j==i:
#                 list3.append(i)
#     return(list3)
# print(two_becomes_one([1,2,3,4,5],[78,5,6,1,22,3,42,5]))

# 4. Write a function that receives a dictionary and returns a list of all the unique values in the given dictionary.

#Answer:
# my_dict={"a":1,"b":1,"c":"t","d":"r","e":"d","f":"e","g":44,"h":32,"i":13,"j":"&","k":"e"}
# def unique_only(v):
#     new_list=[]
#     for value in v.values():
#         if value not in new_list:
#             new_list.append(value)
#     return new_list
# print(unique_only(my_dict))



# 5. Write a function that receives a list and performs a left rotation using slicing.

#Answer:
# def rotate_left(lst):
#     if len(lst) == 0:
#         return lst
#     return lst[1:] + lst[:1] 


# lst = [10, 20, 30, 40]
# new_lst = rotate_left(lst)
# print(new_lst)  


# 6. Write a function that removes and prints every second number from a list of numbers, until the list is empty.

#Answer:
# def empty_the_list(lst):
#     while lst:  
#         dem_list = lst[:] 
#         for i in range(0, len(dem_list), 2):
#             print(dem_list[i])  
#             lst.remove(dem_list[i]) 


# 7. Write a function that converts a given dictionary into a list of pairs (tuples).

#Answer:
# def dict_to_tuple(d):
#     new_tuple=list(d.items())
#     return new_tuple
  
# print(dict_to_tuple({'a': 10, 'b': 20, 'c': 30}))

# 8. Write a function that finds the maximum and minimum values in a dictionary and prints their keys.

#Answer:

# def max_min_dict(d):
#     v=d.values()
#     maximum=(max(v))
#     minimum=(min(v))
#     for keys,value in d.items():
#         if value == maximum:
#             print(f'the key of maximum {keys}')
#         elif value == minimum:
#             print(f'the key of minimum {keys}')
# max_min_dict({'a': 10, 'b': 20, 'c': 30})

# 9. Write a function that receives a string and returns a dictionary where each character is a key and the value is the number of times that character appears.

#Answer:

# def from_str_to_dict(string):
#     dict_of_char={}
#     for ch in string:
#        if ch in dict_of_char:
#            dict_of_char[ch]+=1
#        else:
#            dict_of_char[ch]=1
#     return dict_of_char

# print(from_str_to_dict("my name is oran! how are you"))



# 10. Write a function that receives two lists and returns a list of all values that are in exactly one of them (exclude the intersection).

#Answer:

# def unique(list1,list2):
#     unique_list=[]
#     for ch in list1:
#         if ch not in unique_list and ch not in list2:
#             unique_list.append(ch)
#     for ch in list2:
#         if ch not in unique_list and ch not in list1:
#             unique_list.append(ch)
#     return unique_list
# print(unique([1,2,3,4,5,7,8],[9,8,7,6,5]))

# 11. Write a function that receives a list of numbers and returns the same numbers sorted from smallest to largest, without using sort() or sorted().

#Answer:

# def organized(list):
#     sorted_list=[]
#     while list:
#         sorted_list.append(min(list))
#         list.remove(min(list))        
#     return sorted_list
# print(organized([10,50,20,70,30,100]))

# 12. Write a function that receives a list of numbers and returns the two largest numbers.

#Answer:
# def two_biggest_numbers(list):
#     max_number=second_max=0
#     max_number=max(list)
#     list.remove(max_number)
#     second_max=max(list)
#     return f'the first max is {max_number} the second is {second_max}'

# print(two_biggest_numbers([10,15,88,97,54,56,65,11,23,65,45,47,48]))

# 13. Write a function that receives a dictionary of grades and returns the name of the student with the highest grade.

#Answer:

# def name_of_best_student(d):
#     best_student = None
#     highest_grade = -1
#     for student, grade in d.items():
#         if grade>highest_grade:
#             highest_grade=grade
#             best_student=student
#     return best_student
    
    
# print(name_of_best_student({'Alice': 85, 'Bob': 92, 'Charlie': 78}))

# 14. Write a function that receives a list of numbers and returns a list containing only the numbers that occur more than once.

#Answer:
# def more_than_once(lst):
#     new_list=[]
#     for i in lst:
#         if lst.count(i) >=2 and i not in new_list:
#             new_list.append(i)
#     return(new_list)

# print(more_than_once([10,11,12,10,15,14,15,98,89,98,74,55,61]))

# 15. Write a function that receives a dictionary of {name: age} and returns a list of the names of all people over the age of 18.

#Answer:
# def from_dict_to_list(d):
#     for people,age in d.items():
#         if age>18:
#             print(people)
    

# from_dict_to_list({
#     "Alice": 25,
#     "Bob": 32,
#     "Charlie": 9,
#     "Diana": 41,
#     "Ethan": 7
# })

 # 16. Write a function that receives a list and returns a list in which each element appears only once, while preserving the original order.

 #Answer:
# def only_once(lst):
#     new_list=[]
#     for i in lst:
#         if i not in new_list:
#             new_list.append(i)
#     return new_list
       
# print(only_once([11,54,69,87,452,32,14,56,98,4,56,32,54,23,65,47,89,65,55,22,11,44,22,36]))


# 17. Write a function that receives a string and returns a new string where each letter is replaced by the next letter in the alphabet (wrap around: z → a).

#Answer:

# def tzofen(str):
#     new_str=""
#     for i in str:
#        if i =='z':
#            i='a'
#            new_str+=i
#        else:
#             i= chr(ord(i)+1)
#             new_str+=i
#     return new_str

# print(tzofen("hello"))
# 18. Write a function that receives a list of strings and returns the longest string.

#Answer:
# def longest_string(list):
#     max_length_string=""
#     for i in list:
#         if len(i)>len(max_length_string):
#             max_length_string=i
#     return max_length_string
        

# print(longest_string(["aba","wwwwwww","lhlh","mbkmfk"]))

