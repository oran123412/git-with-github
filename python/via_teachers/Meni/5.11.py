#                                                                    lists
#                                                              ==================


#1
# list=[]
# max_number=0
# x=1
# length=int(input("Enter the length: "))
# for i in range(length):
#     list.append(x)
#     x=int(input("enter a number: "))


# print("Before: ")
# for i in range(len(list)):
#     print(list[i],end=" ")
    
# for i in range(len(list)):
#     list[i]*=i+1

# print(" ")
# print("After: ")
# for i in range(len(list)):
#     print(list[i],end=" ")
    
    
# max_index=0
# for i in range(1,len(list)):
#         if list[i]>list[max_index]:
#             max_index=i
# print(f'the max number is: {list[max_index]}')
# print(f'the max number index is: {max_index}')


#כתבו פונקציה שמקבלת רשימה ומשתנה נוסף .הפונקציה תבדוק אם המשתנה נמצא ברשימה ואם כן תחזיר את האינדקס שלו 

#2
# def find_the_index(lst,var):
#     for i in range(len(lst)):
#         if lst[i]==var:
#             return i
            
#     return -1
  
# if find_the_index([77,8,66,7,82],82) == 0 :
#     print("lala")     
# print(find_the_index([77,8,66,7,82],82))


#                                                                    חיפוש בינארי
#                                                                  =================


# from random import randint
# lst=[]
# for i in range(100000):
#     lst.append(randint(-10000,10000))
# lst.sort()



# def target (number,lst):
#     low=0
#     high=len(lst)-1
#     while low<=high:
#         mid=(low+high)//2
#         if lst[mid] <number:
#             low=mid+1
#         elif lst[mid] > number:
#             high=mid-1
#         elif lst[mid] == number:
#             print("found number")
#             return
#     print("not found")

# target(10,lst)
# print(lin_search(lst,572))
# print(bin_search(lst,572))

#                                                                        פונקציה סידורית
#                                                                       ==================

#pesudo code :
#מוצאת את המספר המקסימלי ברשימה    
#מחליפה אותו במיקום של האיבר האחרון   
#סורקת את הרשימה פחות איבר אחד   
#מוצאת את המספר המקסימלי ברשימה הנוכחית   
#מחליפה אותו במיקום של האיבר האחרון    
#סורקת את הרשימה פחות איבר אחד    
#ממשיכה ככה עד שהמספר המקסימלי הוא היחיד או שאיןעוד איברים   
   