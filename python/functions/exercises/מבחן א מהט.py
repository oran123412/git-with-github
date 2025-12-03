#כתוב קטע קוד שקולט מספרים שלמים עד שיקלט מספר תלת ספרתי.
#יש להדפיס את מספר הגדול ביותר שנקלט ואת מספר קטן ביותר שנקלט 
#max_num = None
#min_num = None 
#x = (input("give a number"))
#while x < 100 :
#        print("try agian")
#else  :
#    print("great choice give another one") 
 

#x = int(input("give a number: "))
#max_num = x
#min_num = x
#
#while x <= 100 or x >= 999:
#    print("try again")
#    x = int(input("give a number: "))
#    if x > max_num:
#        max_num = x
#    if x < min_num:
#        min_num = x
#
#print("The largest number entered:", max_num)
#print("The smallest number entered:", min_num)



#כתבו פעולה המקבלת מחרוזת ובודקת אם היא מחרוזת "תקינה"

#is_valid = input("write a string here: ")
#
#if len(is_valid) %2 ==1:
#    middle_index =  len(is_valid) // 2 
#    if is_valid[0] == is_valid[-1] == is_valid[middle_index] :
#        print ("True")
#    else:
#        print("False")
#else:
#    print("False")

#ב'

#good_string=[]
#bad_string=[]
#
#for i in range(3):
#    is_valid = input("write a string here: ")
#    if len(is_valid) %2 ==1:
#        middle_index =  len(is_valid) // 2 
#        if is_valid[0] == is_valid[-1] == is_valid[middle_index] :
#             good_string.append(is_valid)
#        else:
#            bad_string.append(is_valid) 
#    else:
#        bad_string.append(is_valid)
#
#print(good_string,"great string")
#print(bad_string,"bad string")

#3 
#num_list = []
#num_list = input("put your list of numbers here please")
#pos = sum(1 for x in num_list if x > 0 )
#neg = sum(1 for x in num_list if x < 0 )
#if 0 in int(num_list) or pos == neg :
#        print (num_list)
#else : 
#        num_list_not_balanced = [num_list.reverse()]
#        print (num_list_not_balanced)

#def print_balanced(num_list):
#    if 0 in num_list:
#        print(num_list[::-1])
#        return
#
#    pos_count = sum(1 for x in num_list if x > 0)
#    neg_count = sum(1 for x in num_list if x < 0)
#
#    if pos_count == neg_count:
#        print(num_list)
#    else:
#        print(num_list[::-1])

#user_input = input("הכנס מספרים מופרדים ברווח: ")
#num_list = [int(x) for x in user_input.split()]
#print_balanced(num_list)

#4
#flower_type = input ("enter the type of flower")
#price = int(input ("enter the price"))
#class FlowerPackage:
#    def __init__(self,flower_type,price):
#        self.type = flower_type
#        self.price = price
#        self.time = 12
#        self.num = 2000
#
#    def order (self):
#            return f"{self.type},{self.price }$, {self.time} ,{self.num}" 
#    
#my_order = FlowerPackage(flower_type,price)
#print(my_order.order())

