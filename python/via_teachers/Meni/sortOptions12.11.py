# arr=[3,1,6,5,4]
# def bubbles_sort(arr:list[int])->None:
#     for  i in range(len(arr)-1):
#             is_sorted=True
#             for j in range(0,len(arr)-1-i):
#                 if arr[j]>arr[j+1]:       
#                     arr[j],arr[j+1]=arr[j+1],arr[j]
#                     is_sorted=False
#             if is_sorted:
#                 return
# bubbles_sort()
# print(arr)

# def insertion_sort(arr:list[int])-> None:
#     for i in range(1,len(arr)):
#         key = arr[i]
#         j=i
#         while j>0 and arr[j]>key:
#             arr[j+1]=arr[j]
#             j-=1
#         arr[j] = key
# l1=[2,5,1,3,9,10,7]
# print(l1)
# insertion_sort(l1)
# print(l1)

#כתוב פונקציה המקבלת 2 רשימות ממוינות ותחזיר רשימה merge בינהם

# lst1 = [2, 3, 5, 9]
# lst2 = [1, 5, 6, 12]

# def merge(lst1, lst2):
#     i = 0
#     j = 0
#     merged = []

#     while i < len(lst1) and j < len(lst2):
#         if lst1[i] < lst2[j]:
#             merged.append(lst1[i])
#             i += 1
#         else:
#             merged.append(lst2[j])
#             j += 1

#     merged.extend(lst1[i:])
#     merged.extend(lst2[j:])

#     return merged

# print(merge(lst1, lst2))

#כתוב תוכנית שתקבל מספר ותדפיס את מספר ההופעות של כל ספרה במספר לפי הסדר מהקטן לגדול 

# number='3005'

# def num_of_numbers(number):
#     lst_of_digits=[]
#     for i in range(len(number)):
#         lst_of_digits.append(number[i])
#         lst_of_digits.append(number.count(number[i]))
#     return lst_of_digits

# print(num_of_numbers(number))


# number=3005
# digit=0
# lst=[]
# while number>0:
#     digit=number%10
#     lst.append(digit)
#     lst.append(number.count(digit))
#     number=number//10
# print(lst)

# number=12223415

# def bubbles_sort(arr:list[int])->None:
#   for i in range(len(arr)-1):
#       is_sorted=True
#       for j in range(0,len(arr)-1-i):
#           if arr[j]>arr[j+1]:
#               arr[j],arr[j+1]=arr[j+1],arr[j]
#               is_sorted=False
#       if is_sorted:
#           return
# l1=[2,5,1,3,9,10,7]
# print(l1)
# bubbles_sort(l1)
# print(l1)

# def insertion_sort(arr:list[int]) -> None:
#   for i in range(1, len(arr)):
#     key = arr[i]
#     j = i
#     while j > 0 and arr[j -1] > key:
#       arr[j] = arr[j - 1]
#       j -= 1
#     arr[j] = key
# l1=[2,5,1,3,9,10,7]
# print(l1)
# insertion_sort(l1)
# print(l1)

# def merge(arr1:list[int],arr2:list[int]):
#   ret=[0]*(len(arr1)+len(arr2))
#   i=j=k=0
#   while k<len(ret):
#     if i<len(arr1) and j<len(arr2):
#       if arr1[i]<arr2[j]:
#         ret[k]=arr1[i]
#         i+=1
#       else:
#         ret[k]=arr2[j]
#         j+=1
#     elif i<len(arr1):
#       ret[k]=arr1[i]
#       i+=1
#     else:
#       ret[k]=arr2[j]
#       j+=1
#     k+=1
#   return ret


# arr1=[5,3,8,6,9,12,6,7]
# arr2=[5,9,2,5,4,11,12,6,12,13,25,4]
# arr1.sort()
# arr2.sort()
# arr3=merge(arr1,arr2)
# print(arr1,arr2)
# print(arr3)


# def print_digits_occurrences_ver1(num:int)->None:
#   if num<0:
#     num-=num
#   for digit in range(10):
#     temp=num
#     times=0
#     while(temp):
#       if temp%10==digit:
#         times+=1
#       temp//=10
#     if times:
#       print(f"{digit}:{times}",end="   ")
      
# print_digits_occurrences_ver1(2005)



# def print_digits_occurrences_ver2(num:int)->None:
#   if num<0:
#     num-=num
#   arr=[0]*10
#   while num:
#     arr[num%10]+=1
#     num//=10
#   for i in range(len(arr)):
#     if arr[i]:
#       print(f"{i}:{arr[i]}",end="   ")

# number=12223415
# print_digits_occurrences_ver1(number)
# print()
# print_digits_occurrences_ver2(number)



