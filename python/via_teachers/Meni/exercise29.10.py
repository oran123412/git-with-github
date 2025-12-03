#1
# current_number=int(input("Please enter a number: "))
# prev_num=0
# growing=True
# count=0
# while current_number!=-1:
#     count+=1
#     if current_number>prev_num:
#         prev_num=current_number 
#     elif current_number<=prev_num :
#         growing=False
#     current_number=int(input("Please enter a number: "))
# if count>2:
#     if growing:
#         print("the series is growing")
#     else:
#         print("the series isnt growing")


#2
# n=int(input("Please enter the number of inputs: "))
# max_num=0
# max_second=0
# count=0
# i=0
# while i <n:
#     numbers=int(input("Please enter the number of inputs: "))
#     if numbers >max_num:
#         max_second=max_num
#         max_num=numbers
#     if  numbers >max_second :
#         max_second=numbers
#     count+=1
#     i+=1
# if count>2:
#     print(f'the max number is {max_num} the second is {max_second}')
# if count==1:
#     print(f'the max number is {max_num} the second is {"None"}')
# if count<1:
#     print(f'the max number is {"None"} the second is {"None"}') 
    
    
# def stam(a):
#     a*=2
#     print(a)
#     return
#     print("lala")
#     lala=5
#     return 5
# b=stam(10)
# print(b)


# l1=[]
# l2=[3,5,1,2]
# l3=[2,"lala",3+4j,-7]
# print(l1,l2,l3,sep="\n")
    
# first=l2[0]
# second=l3[-1]
# print(first,second,sep="\n")

# l3[1]="lol"
# print(l3)

# l2.append(150)
# l3.insert(2,"lili")
# print(l2,l3,sep="\n")
4
# l2=[4,2,3,2,10]
# l2.remove(2)
# print(l2)
# del(l3[-1])
# print(l3)
# print(l3.pop()*2+l3.pop(0))

# l=[1,2,3,4,5,6,7]
# for item in l:
#     print(item+5,end="       ")
# print()

#                                                              The question for class 
#                                                           ============================

num=5
sum_of_numbers=0
list_of_numbers=[]
for i in range(num):
    number_of_user=int(input("Enter a number: "))
    sum_of_numbers+=number_of_user
    list_of_numbers.append(number_of_user)
avg=sum_of_numbers/num
print("The numbers which are bigger than average are: ")
for i in list_of_numbers:
    if i >avg:     
        print (i,end=" ")


    


