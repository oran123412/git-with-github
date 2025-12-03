#סט תרגילים רשימות                                               
#                                              =====================

#1
#a
n = int(input("Enter the number of numbers you want to write: "))
while n<=0:
    n = int(input("Enter positive number: "))
    
first_number = int(input("Enter the first number:")) 

sum_small = 0
count_small = 0

for i in range(n - 1):
    num = int(input("Enter a number: "))
    if num < first_number:
        sum_small += num
        count_small += 1

if count_small > 0:
    print(sum_small / count_small)
else:
    print(0)

   
#b
n = int(input("Enter the number of numbers you want to write: "))

s = ""  

for i in range(n):
    num = input("Enter a number: ")
    s += num + " "   

parts = s.split() 

last = int(parts[-1])

sum_small = 0
count_small = 0


for p in parts[:-1]:
    num = int(p)
    if num < last:
        sum_small += num
        count_small += 1

if count_small > 0:
    print(sum_small / count_small)
else:
    print(0)


#2
number=int(input("Enter a number: "))
while number<0:
    number=int(input("Enter a number: "))
number=str(number)
already=""
for i in number: 
    if i not in already:
        print(f'the digit {i} apppears:', number.count(i))
        already+=i

#3
def findMissing(a: list[int], n: int) -> int:
    for num in range(1, n+1):
        if num not in a:
            return num


#4
binary_list=[]
count_1=0
series_of_one=[]
digit=input("Enter a number: ")
while digit not in ("0","1"):
    digit=input("Enter a number of 0 or 1 only!: ")
binary_list.append(digit)
i=1
while i<12:
    digit=input("Enter a number: ")
    while digit not in ("0","1"):
        digit = input("Enter a number of 0 or 1 only! ")
    binary_list.append(digit)
    i+=1
for i in binary_list:
    if i =="1":
        count_1+=1
    elif i =="0":
        if count_1>0:
            series_of_one.append(count_1)
        count_1=0
if count_1>0:
      series_of_one.append(count_1)
print(f'the number of 111  apperns in series is  {series_of_one.count(3)} time')
print(f'the number of 11  apperns in series is {series_of_one.count(2)} time')
print(f'the number of 1 apperns in series is {series_of_one.count(1)} time')
    
#5
#a
midMax(3,7,5)

#b
midMax(7,3,5)

#c
def midMax(a:float, b:float, c:float) -> int:
    if b > a and b > c:
        return 1
    return 0

#d

def midMax(a:float, b:float, c:float) -> int:
    if b > a and b > c:
        return 1
    return 0


def countPeaks(heights:list[int])->int:
    count_hights=0
    for i in range(1,len(heights)-1):
        if midMax(heights[i-1],heights[i],heights[i+1])==1:
            count_hights+=1
    return(count_hights)
    
print(countPeaks([206,350,300,167,406,310,328,250,200,120,400,380,435,200,337,200]))

#6
#a
def arithmeticMean(a:list[int])->float:
    sum_of_numbers=0
    for i in range(len(a)):
        sum_of_numbers+=a[i]
    result=sum_of_numbers/len(a)
    return result

#b
def geomrtricMean(a:list[int])->float:
     duplication_of_numbers=1
     for i in range(len(a)):
         duplication_of_numbers*=a[i]
     result=duplication_of_numbers**(1/len(a))
     return result

#c
def harmonicMean(a:list[int])->float:
    sum_of_numbers=0
    new_number=0
    for i in range(len(a)):
        new_number=1/a[i]
        sum_of_numbers+=new_number
    result=len(a)/sum_of_numbers
    return result


#d
def arithmeticMean(a:list[int])->float:
    sum_of_numbers=0
    for i in range(len(a)):
        sum_of_numbers+=a[i]
    result=sum_of_numbers/len(a)
    return result

def geomrtricMean(a:list[int])->float:
     duplication_of_numbers=1
     for i in range(len(a)):
         duplication_of_numbers*=a[i]
     result=duplication_of_numbers**(1/len(a))
     return result

def harmonicMean(a:list[int])->float:
    sum_of_numbers=0
    new_number=0
    for i in range(len(a)):
        new_number=1/a[i]
        sum_of_numbers+=new_number
    result=len(a)/sum_of_numbers
    return result

a = [2, 4, 8, 16]
harmonic=harmonicMean(a)
geomrtric=geomrtricMean(a)
arithmetic=arithmeticMean(a)

print("Harmonic:", harmonic)
print("Geometric:", geomrtric)
print("Arithmetic:", arithmetic)

if  arithmetic>=geomrtric>=harmonic:
    print("Proven")
else:
    print("Not proven")


#7
#a
def reverse(a:list[int]):
    n=len(a)
    for i in range(n//2):
        a[i] , a[n-1-i] = a[n-1-i] , a[i]
        
#b
def flip(a:list[int],m:int,n:int):
    for i in range(m):
        temp=a[ m+i ]

        for j in range( m+i-1 ,0,-1):
            a[j]=a[ j-1 ]
        a[ 0 ]=temp