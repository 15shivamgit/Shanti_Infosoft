# :beginner: BASIC LEVEL (10 Questions)
# 1. Write a program that takes a string from the user and prints each character on a new line using a loop.
'''str=input("Enter a string: ")
for i in str:
  print(i)
'''





# 2. Take a string input and count the total number of characters in it without using len().
'''str=input("Enter a string: ")
count=0
for i in str:
  count+=1
print(f"Total charceter: {count}")
'''


# 3. Write a program to print a string in reverse order using a loop.
'''str=input("Enter a string: ")
newstr=''
for i in str:
  newstr=i+newstr
print(f"Reverse string: {newstr}")
'''




# 4. Input a string and print only the uppercase letters from it.
'''str=input("Enter a string: ")
for i in str:
  char=ord(i)
  if char>=65 and char<=90:
    print(i,end="")'''




# 5. Take a string and count how many vowels (a, e, i, o, u) are present in it.
'''str=input("Enter a string: ")
vowel=0
for i in str:
  if i=='a' or i=='e' or i=='i' or i=='0' or i=='u':
    print(i,end="")
    vowel+=1
print(f"\nTotal Vowel in {str}: {vowel}")'''





# 6. Write a program that converts a string into uppercase without using .upper().
'''str=input("Enter a string: ")
newstr=''
for i in str:
  ascii=ord(i)
  if ascii>=97 and ascii<=122:
    newstr+=chr(ascii-32)
  else:
    newstr+=i
print(newstr)'''




# 7. Input a string and count how many digits are present in it.
'''str=input("Enter a string: ")
digit=0
for i in str:
  char=ord(i)
  if char>=48 and char<=57:
    digit+=1
print(f"Total digit in {str}: {digit}")'''
  




# 8. Write a program to check whether a given string starts with the letter ‘A’.
'''str=input("Enter a string: ")
if str[0]=='A':
  print("Yes,Start with 'A'")
else:
  print("Not start with 'A'")'''





# 9. Take a string input and replace all spaces with underscore _ without using .replace().
'''str=input("Enter a string: ")
newstr=''
for char in str:
  if char==" ":
    newstr+="_"
  else:
    newstr+=char
print(f"New string: {newstr}")'''




# 10. Write a program that prints only the alphabets from a mixed string (ignore digits and symbols).
'''str=input("Enter a number: ")
for i in str:
  ch=ord(i)
  if ch>=65 and ch<=90 or ch>=97 and ch<=122:
    print(i,end="")'''





# :gear: INTERMEDIATE LEVEL (10 Questions)
# 11. Write a program to check whether a string is a palindrome or not using a loop.
'''str=input("Enter a string: ")
newstr=''
for ch in str:
  newstr=ch+newstr
if str==newstr:
  print(f"\'{str}\' is a palidrome string")
else:
  print(f"\'{str}\' is a not palidrome string")'''



str='abbaa'
print('Palidrome') if str==str[::-1] else print("Not Palidrome")






# 12. Take a string and find how many times a specific character appears in it.
'''str=input("Enter a string: ")
char=input("Enter a character: ")
count=0
for i in str:
  if i==char[0]:
    count+=1
print(f"'{char}' in {str}: {count} times")'''




# 13. Write a program to remove all vowels from a string and print the result.
'''str=input("Enter a string: ")
for ch in str:
  if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u' or ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U':
    pass
  else:
    print(ch,end='')'''





# 14. Input a string and print only the consonants from it.
'''str=input("Enter a string: ")
for ch in str:
  if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u' or ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U':
    pass
  else:
    print(ch,end='')'''





# 15. Write a program to find the first repeated character in a string.
'''txt='bhnjni'
check=False
for i in range(len(txt)):
  for j in range(len(txt)):
    if txt[i]==txt[j] and i!=j:
      print(txt[i])
      check=True
      break
  if check:
    break'''






'''for i in range(len(txt)):
  if txt[i]==txt[i+1]:
    print(txt[i])
    break'''



# 16. Take a string and swap uppercase letters to lowercase and lowercase to uppercase without using .swapcase().
'''txt=input("Enter a string: ")
swapstr=''
for i in range(len(txt)):
  ascii=ord(txt[i])
  if ascii>=65 and ascii<=90:
    swapstr+=chr(ascii+32)
  elif ascii>=97 and ascii<=122:
    swapstr+=chr(ascii-32)
  else:
    swapstr+=txt[i]
print(swapstr)'''





# 17. Write a program to find the longest word in a sentence without using lists.
'''txt="My name is shivam singh gautam"
result=''
temp=''
for i in range(len(txt)):
  if txt[i]==' ':
    temp=''
  else:
    temp+=txt[i]

  if len(temp)>=len(result):
    result=temp
print(result)'''
  







# 18. Input a string and count how many words are present in it (assume words are separated by spaces).
'''txt=input("Enter a string: ")
count=1
if txt[0]==' ':
  count-=1
for i in range(len(txt)):
  if i<len(txt)-1 and txt[i]==" " and txt[i+1]!=' ':
    count+=1
print(f"Total word: {count}")'''




# 19. Write a program to check whether a string contains only digits.
'''txt=input("Enter a string: ")
digit=False
for i in range(len(txt)):
  ascii=ord(txt[i])
  if ascii>=48 and ascii<=57:
    digit=True
  else:
    digit=False
if digit:
  print(f"'{txt}' contain only digits")
else:
  print(f"'{txt}' not contain only digits")'''





# 20. Take two strings as input and check whether they are exactly equal without using ==.
'''txt1=input("Enter first string: ")
txt2=input("Enter second string: ")
same=False
if len(txt1) is len(txt2):
  for i in range(len(txt1)):
    if txt1[i] is txt2[i]:
      print(txt1[i],"-",txt2[i])
      same=True
    else:
      same=False
      break
  if same:
    print(f"'{txt1}' and '{txt2}' are equal")
  else:
    print(f"'{txt1}' and '{txt2}' are not equal")
else:
  print(f"'{txt1}' and '{txt2}' are not equal")'''

# print(' ' is ' ')
# print(' ' in ' ')
'''if txt1 is txt2:
  print("Equal")
else:
  print("Not Equal")'''


# print(txt1 is txt2)
# print(id(txt1))
# print(id(txt2))






# :rocket: ADVANCED LEVEL (8 Questions)
#? 21. Write a program to compress a string by counting consecutive characters.
#  Example:
#  Input: aaabbc
#  Output: a3b2c1

'''txt = 'aaabbc'
result = ''
count = 1
ch = txt[0]
for i in range(1, len(txt)):
    if txt[i] == ch:
      count += 1
    else:
      result += ch + str(count)
      ch = txt[i]
      count = 1
result += ch + str(count)
print(result)'''




'''txt='aaabbcabcc'
result=''
count=1
for i in range(1,len(txt)):
    if txt[i]==txt[i-1]:
        count+=1
    else:
        result+=txt[i-1]+str(count)
        count=1
result+=txt[len(txt)-1]+str(count)
print(result)'''


#? 22. Write a program to find the most frequently occurring character in a string (without using list or dictionary).
'''txt='bbbananaccccca'
freq=''
temp=0
for i in range(len(txt)):
  count=0
  ch=txt[i]
  for j in range(len(txt)):
    if txt[i]==txt[j]:
      count+=1
  check=False
  for j in range(i):
    if ch==txt[j]:
      check=True
  if check==False and count>temp:
    temp=count
    freq=ch
print(f"Most frequently occurring character : {freq}")'''



#? 23. Take a string and remove all duplicate characters while keeping the first occurrence.
'''txt='my name'
for i in range(len(txt)):
  ch=txt[i]
  count=0

  for j in range(len(txt)):
    if txt[i]==txt[j]:
      count+=1

  check=False
  for j in range(i):
    if ch==txt[j]:
      check=True
  
  if check==False:
    print(ch,end='')'''




#? 24. Write a program to check whether two strings are anagrams without using sorting, lists, or tuples.
s1='aab'
s2='aba'
'''
if len(s1)==len(s2):
  for i in range(len(s1)):
    temp=''
    check=False
    for j in range(len(s2)):
      if s1[i]==s2[j] and check==False:
        check=True
      else:
        temp+=s2[j]
    s2=temp
    print(temp)
  
  if s2=='':
    print("Yes, anagrams")
  else:
    print("Not anagrams")
else:
  print("Not anagrams")
'''


# if len(s1)!=len(s2):
#   print("Not anagrams")

# print("Yes, anagrams") if sorted(s1)==sorted(s2) else print("Not anagrams")



#? 25. Input a string and find the second most frequent character.
'''text='bananabn'
max_freq=0
max_ch=''
sec_freq=0
sec_ch=''
for i  in range(len(text)):
  ch=text[i]
  count=0
  for j in range(len(text)):
    if text[i]==text[j]:
      count+=1
  
  check=False
  for j in range(i):
    if ch==text[j]:
      check=True
  
  if check==False:
    if count>max_freq:
      sec_freq=max_freq
      sec_ch=max_ch

      max_freq=count
      max_ch=ch
    elif count > sec_freq and count < max_freq:
      sec_freq=count
      sec_ch=ch

print(f"Most frequent character in '{text}' : {max_ch}")
print(f"Second most frequent character in '{text}' : {sec_ch}")
'''





#? 26. Write a program to reverse each word of a sentence without changing their order.
#?  Example:
#  Input: hello world
#  Output: olleh dlrow
'''text='15    kumar hello world shivam 123'
newtext=''
result=''
for i in range(len(text)):
  if text[i]!=' ':
    newtext+=text[i]
  else:
    for j in range(len(newtext)-1,-1,-1):
      result+=newtext[j]
    newtext=''
    result+=' '

for j in range(len(newtext)-1,-1,-1):
  result+=newtext[j]
print(result)'''




#? 27. Write a program to check whether a string is a valid identifier name in Python (only letters, digits, underscore and not starting with digit).
'''var=' p_thOn123'
valid=False
for i in range(len(var)):
  ascii=ord(var[i])
  if var[0]!=' ':
    if ascii>=48 and ascii<=57 or ascii>=65 and ascii<=90 or ascii>=97 and ascii<=122 or ascii==95:
      valid=True
    else:
      valid=False
      break
  else:
    valid=False

if valid:
  print(f"'{var}' is valid identifier in python")
else:
  print(f"'{var}' is not valid identifier in python")'''


#? 28. Write a program that finds the longest substring that contains no repeated characters.
'''text = input("Enter a string: ")
longest = ""
current = ""
for i in range(len(text)):
    ch = text[i]
    for j in range(len(current)):
      if current[j] == ch:
        current = current[j+1:]
        break
    current += ch
    if len(current) > len(longest):
      longest = current

print(f"Longest substring: '{longest}'")
'''



#? 29. Take a string and find how many times a all character appears in it.
'''txt='banana--'
for i in range(len(txt)):
  count=0
  ch=txt[i]
  for j in range(len(txt)):
    if txt[i]==txt[j]:
      count+=1
  check=False
  for j in range(i):
    if ch==txt[j]:
      check=True
  if check==False:
    print(ch,"=",count)'''

      