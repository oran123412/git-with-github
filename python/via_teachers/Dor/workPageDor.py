#1
def even(numbers):
    for i in numbers:
        if i%2==0:
            continue
        else:
            return("Not totally even")
    return("Totally even")

print(even([11,24,25,27]))

#2
def most_common(numbers):
    count0=0
    count1=0
    count2=0
    for i in numbers:
        if i%3==0:
            count0+=1
        elif i%3==1:
            count1+=1
        elif i%3==2:
            count2+=1
    if count0>count1 and count0>count2:
        return ('the most common is 0')
    elif count1>count0 and count1>count2:
        return ('the most common is 1')
    elif count2>count1 and count2>count0:
        return ('the most common is 2')
    else:
        return("tie between some groups")
print(most_common([3,17,18,27,29,5,22,33]))

#3
def length(growing):
    prev_string=""
    for i in growing:
        current_string=i
        if len(current_string)>len(prev_string):
            prev_string=current_string
            continue
        else:
            return ("Not always increasing")
    return("Always increasing")   
print(length(["a","aa","dffa"]))

#4
def changing_string_by_number(number,string):
    new_word=""
    string=string.lower()
    for i in string:
        if 'a'<=i<='z':
            new_letter=ord(i) + number 
            if new_letter>122:
                new_letter-=26 
            new_word+=(chr(new_letter))
    return new_word
        
print(changing_string_by_number(3,("fox")))

#5
def list_numbers(numbers,n):
    list_of_smaller=[]
    list_of_bigger=[]
    for i in numbers:
        if i<n:
            list_of_smaller.append(i)
        elif i >n:
            list_of_bigger.append(i)
    if len(list_of_bigger)>len(list_of_smaller):
        return (f"the list of 'bigger numbers' is bigger {list_of_bigger}\n the number of 'small numbers' is {len(list_of_smaller)}\n the number of 'bigger numbers' is {len(list_of_bigger)}")
    elif len(list_of_bigger)<len(list_of_smaller):
        return (f"The list of the 'smaller numbers' is bigger {list_of_smaller}\n the number of 'small numbers' is {len(list_of_smaller)}\n the number of 'bigger numbers' is {len(list_of_bigger)}")

print(list_numbers([1,17,55,98,74,55,61,21,0,35,12,94,55],55))
