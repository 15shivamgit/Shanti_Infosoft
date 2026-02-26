#------------------------String------------------------------

# a='Shivam'
# print(a[0])
# print(a[len(a)-1])
# print(a[len(a)//2])
# print(a[(len(a)-1)//2])


'''str="Shanti infosoft"
consonent=0
vowel=0
for i in range(len(str)):
  if str[i]!= 'a' and str[i]!= 'e' and str[i]!= 'i' and str[i]!= 'o' and str[i]!= 'u':
    print(str[i])
    consonent+=1
  else:
    vowel+=1
print(f"Consonent: {consonent}")
print(f"Vowel: {vowel}")'''



# first character convert into capital
'''str="my name is shivam"
for i in range(len(str)):
  if i==0:
    print(str[i].upper(),end="")
  elif str[i-1] ==" ":
      print(str[i].upper(),end="")
  else:
    print(str[i],end="")'''


# Reverse string
'''s='Shivam'
for i in  range(-1,-len(s)-1,-1):
  print(s[i],end="")

for i in  range(len(s)-1,-1,-1):
  print(s[i],end="") '''



#  --------Slicing  String-------
'''str='shani'
print(str[:])
print(str[2:3])
print(str[0:5:2])
print(str[-5:-1:2])
print(str[-1:-5:-1])'''


#--------modifying  string------
'''str="   shanti    infosoft"
print(str)
print(str.strip())
print(str.replace('s','z'))'''


#-------F-String-------
'''name="Shivam"
age=24
print()'''


#WAP to convert lower  to  upper  and upper-lower
str='a'
print(ord(str))