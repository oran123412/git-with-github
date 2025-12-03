#                                                           סט תרגילים מחרוזות
#                                                            =================

#1
#א
letters = input("Enter your string to end write '.': ")
count = 0

for i in range(len(letters)):
    if letters[i] == 'a':
        for j in range(i+1, len(letters)):
            if letters[j] == 'b':
                count += 1

print(" Number of words that start with 'a' and end with 'b':", count)


#ב
count_no_c = 0
in_a = False
c_found = False


letters = input("Enter your string to end write '.': ")
for ch in letters:
    if ch == 'a':
        in_a = True
        c_found = False
    elif ch == 'c' and in_a:
        c_found = True
    elif ch == 'b' and in_a and not c_found:
        count_no_c += 1
print(" Number of words without c:", count_no_c)



#ג
count_only_one_c = 0
in_a = False
c_count = 0

letters=input("Enter your string again to end write '.': ")
for ch in letters:
    if ch == 'a':
        in_a = True
        c_count = 0
    elif ch == 'c' and in_a:
        c_count += 1
    elif ch == 'b' and in_a and c_count == 1:
        count_only_one_c += 1

print(" Number of words with one c:", count_only_one_c)

#2
output = ""

for i in range(15):
    string = input("Enter your string: ")
    if len(string) > 1 and string[0] == string[-1]:
        output += string + "\n"

print(f'The strings that were under the condition:\n{output}')


#3
long_string=input("Enter a long string: ")
short_string=input("Enter a short string: ")
if len(long_string)>=2*(len(short_string)):
    print(long_string)
else:
    print(short_string)


#4
s1 = input("Enter a long string: ")
s2 = input("Enter a short string: ")

count = 0
i = 0

while i < len(s1):
    if s1[i:i+len(s2)] == s2:
        count += 1
        i += 1 
    else:
        i += 1

print(f"The word '{s2}' appears {count} times .")


#5
def sum_numbers_in_string(string):
    total = 0
    num_str = ""  
    
    for char in string:
        if char.isdigit():
            num_str += char    
        else:
            if num_str != "":
                total += int(num_str) 
                num_str = ""           
                             
    if num_str != "":
        total += int(num_str)      
    return total
print(sum_numbers_in_string("600cw580d12ab")) 

#6
def delete_char(st, ch):
    new_sentence = ""
    for i in range(len(st)):
        if st[i] != ch:
            new_sentence += st[i]
    return new_sentence

print(delete_char("hello,, world", ",")) 

#7
def chipher(key, text):
    new_string = ""
    for char in text:
        if 'A' <= char <= 'Z':  
            new_string += chr((ord(char) - ord('A') + key) % 26 + ord('A'))
        elif 'a' <= char <= 'z':
            new_string += chr((ord(char) - ord('a') + key) % 26 + ord('a'))
        else:
            new_string += char  
    print("Encrypted:", new_string)

def opposite_chipher(key, text):
    new_string = ""
    for char in text:
        if 'A' <= char <= 'Z':
            new_string += chr((ord(char) - ord('A') - key) % 26 + ord('A'))
        elif 'a' <= char <= 'z':
            new_string += chr((ord(char) - ord('a') - key) % 26 + ord('a'))
        else:
            new_string += char
    print("Decrypted:", new_string)











                