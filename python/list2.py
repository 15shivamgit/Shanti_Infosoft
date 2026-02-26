# :large_green_circle: BASIC (7 Questions)
#! 1. Print all elements of a list using a loop (without using len()).
'''name=['guddi','chhoti','tannu','mannu','dhannu']
print(name[0:])
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
'''

#! 2. Count how many elements are in a list (without using len()).
'''names=['guddi','chhoti','tannu','mannu','dhannu']
elements=0
for i in names:
  elements+=1
print(f"Total element: {elements}")
'''


#! 3. Find the sum of all numbers in a list (without using sum()).
'''nums=[1,2,3,4,5,6,7,8,9,10]
sum=0
for n in nums:
  sum+=n
print(f"Sum : {sum}")
'''



#! 4. Count how many even numbers are in a list.
'''nums=[1,2,3,4,5,6,7,8,9,10]
even=0
for n in nums:
  if n%2==0:
    print(n,end=' ')
    even+=1
print(f"\nEven number: {even}")
'''


#! 5. Count how many odd numbers are in a list.
'''nums=[1,2,3,4,5,6,7,8,9,10]
odd=0
for n in nums:
  if n%2==0:
    print(n,end=' ')
    odd+=1
print(f"\nOdd number: {odd}")
'''

#! 6. Print all negative numbers from a list.
'''nums=[1,-5,2,-9,3,4,5,-101,-1,6,7,-5,8,9,10]
for n in nums:
  if n<0:
    print(n,end=' ')
'''



#! 7. Given a list of strings, count how many strings start with the letter "a".
'''names=['Shivam','Aditi','Smarti','Yukti','Pranaw']
count=0
for name in names:
  if name[0]=='A' or name[0]=='a':
    count+=1
print(f"Number of string start with 'a/A' : {count}")
'''


# :large_yellow_circle: INTERMEDIATE (7 Questions)
#! 8. Find the largest number in a list (without using max()).
'''nums=[2,45,34,56,4,5,61,4,30]
max=nums[0]
for n in nums:
  if n>max:
    max=n
print(f"Largest elemets of list : {max}")
'''



#! 9. Find the smallest number in a list (without using min()).
'''nums=[2,45,34,56,0,4,5,61,4,30,1]
small=nums[0]
for n in nums:
  if n<small:
    small=n
print(f"Smallest number of list : {small}")
'''



#! 10. Reverse a list manually (without using reverse() or slicing).
'''names=['guddi','chhoti','tannu','mannu','dhannu']
for i in range(len(names)//2):
  temp=names[i]
  names[i]=names[len(names)-1-i]
  names[len(names)-1-i]=temp
print(names)
'''


#! 11. Check if a number exists in a list (without using in keyword).
'''nums=['abc','xyz','pqr']
exists=0
for num in nums:
  if isinstance(num,int) or isinstance(num,float):
    print(num)
    exists+=1

if exists!=0:
  print(f"Number exists in list")
else:
  print(f"Number not exists in list")
'''


'''nums=['abc',4,45,'xyz',6,'pqr',9.0]
for num in nums:
  if type(num)==int or type(num)==float:
    print("Number exists in list")
    break
'''


'''nums=[2,45,90,34,17,63,6,91,58,29]
n=int(input("Enter a number: "))
for num in nums:
  if n==num:
    print("Number exists in list")
    break
'''





#! 12. Remove duplicate numbers from a list (without using set()).
'''nums=[2,3,1,2,3,5]
for n in nums:
  if nums.count(n)>1:
    nums.remove(n)
print(nums)
'''

# nums=[2,3,1,2,3,5,3,2]
# newlist=[]
# for x in nums:
#   if x not in newlist:
#     newlist.append(x)

# print(newlist)




#! 13. Count how many times a specific number appears (without using count()).
'''nums=[2,3,1,4,2,3,5,8,76,6,6,]
n=int(input("Enter a number: "))
count=0
for num in nums:
  if n==num:
    count+=1
print(f"{n} appears time : {count}")
'''


#! 14. Separate even and odd numbers into two different lists.
'''nums=[1,2,3,4,5,6,7,8,9,10]
even=[]
odd=[]
for num in nums:
  if num%2==0:
    even.append(num)
  else:
    odd.append(num)
print(f"Even number: {even}")
print(f"Odd number: {odd}")
'''



'''nums=[1,2,3,4,5,6,7,8,9,10]
even=[]
odd=[]
for num in nums:
  if num%2==0:
    even+=[num]
  else:
    odd+=[num]
print(f"Even number: {even}")
print(f"Odd number: {odd}")
'''




# :large_orange_circle: MEDIUM (7 Questions)
#? 15. Sort a list in ascending order manually (without using sort()).
'''nums=[21,45,90,34,17,63,6,91,58,29]
for i in range(len(nums)):
  for j in range(len(nums)-i-1):
    if nums[j]>nums[j+1]:
      temp=nums[j]
      nums[j]=nums[j+1]
      nums[j+1]=temp
print("Ascending order: ",nums)
'''


#? 16. Sort a list in descending order manually.
'''nums=[21,45,90,34,17,63,6,91,58,29]
for i in range(len(nums)):
  for j in range(len(nums)-i-1):
    if nums[j]<nums[j+1]:
      temp=nums[j]
      nums[j]=nums[j+1]
      nums[j+1]=temp
print("Descending order: ",nums)
'''



#? 17. Find the second largest number in a list.
nums=[10,60,20,23,25,60]
max=nums[0]
sac_max=0
for num in nums:
  if num>max:
    sac_max=max
    max=num

  if num>sac_max and num<max:
    sac_max=num

print("Largest number: ",max)
print("Second largest number: ",sac_max)


#? 18. Merge two lists without using extend().
'''names=['Shivam','Pranaw','Smarti','Aditi','Yukti']
ages=[23,25,19,20,22]
names+=ages
print(names)
'''


#? 19. Find common elements between two lists (without using set()).
'''n1=[True,12,34,1,23,45,2,109,87,'Shivam']
n2=[11,34,98,'Shivam',29,56,2,78,True]
count=0
for x in n1:
  for y in n2:
    if x==y:
      count+=1
      print(x)
print(f"Number of commen element: {count}")
'''


#? 20. Check if a list is a palindrome (without using slicing).
'''myList=[1,2,3,4,2,1]
pald=True
for i in range(len(myList)):
  #print(i,len(myList)-1-i)
  if myList[i]!=myList[len(myList)-1-i]:
    pald=False


if pald:
  print("List is a palidrome")
else:
  print("List is a not palidrome")
'''



#? 21. Move all zeros in a list to the end while keeping order of other elements.
'''nums=[12,0,3,45,9,67,0,2,0,11]
for i in range(len(nums)):
  for j in range(len(nums)-1-i):
    if nums[j]==0:
      nums[j],nums[j+1]=nums[j+1],nums[j]

print(nums)
'''


'''nums=[12,0,3,45,9,67,0,2,0,11]
for i in  range(len(nums)):
  if nums[i]==0:
    nums.pop(i)
    nums.append(0)

print(nums)    
'''




# :red_circle: ADVANCED (7 Questions)
# 22. Find the frequency of each element in a list (without using dictionary built-in counting functions).
'''nums=[12,0,3,11,9,67,0,21,3,0,11]
for i in range(len(nums)):
  n=nums[i]
  count=0
  for j in range(len(nums)):
    if nums[i]==nums[j]:
      count+=1

  check=False
  for j in range(i):
    if n==nums[j]:
      check=True

  if check==False:
    print(n," - ",count)
'''


#? 23. Rotate a list to the right by k positions (without slicing).
'''num=[1,2,3,4,5]
k=2
for i in range(k):
  num.insert(0,num.pop())
print(num)
'''

'''num=[1,2,5,4,8,6,3]
k=5
for i in range(k):
  num+=[num[0]]
  num=[num[x] for x in range(len(num)) if x!=0]

print(num)'''








#! 24. Rotate a list to the left by k positions.
'''num=[1,2,3,4,5]
k=2
for i in range(k):
  #num.insert(len(num),num.pop(0))
  num.append(num.pop(0))
  # temp=num[0]
  # num.pop(0)
  # num.append(temp)
print(num)
'''



'''
num=[1,2,5,4,8,6,3]
k=5
for i in range(k):
  num=[num[len(num)-1]]+num
  num=[num[x] for x in range(len(num)) if x!=len(num)-1]
print(num)'''



#? 25. Find the longest string in a list (without using max()).
'''name=['12345','a','ab','abc','aaac']
long=len(name[0])
long_str=name[0]
for x in name:
  if len(x)>long:
    long_str=x
    long=len(x)

print(f"Longest string : {long_str}")
'''


#? 26. Check if two lists are equal without using ==.
'''list1=[1,True,'sk',2.3]
list2=[1,True,'sk',2.3]

if len(list1)==len(list2):
  equal=True
  for i in range(len(list2)):
    if list1[i]!=list2[i]:
      equal=False
      break

  if equal:
    print("Both list are equal")
  else:
    print("Both list are not equal")
else:
  print("Both list are not equal")
'''




#? 27. Find all pairs in a list whose sum equals a given number.
'''nums=[0,1,2,3,2,3,4,5,6,7]
sum=7
for i in range(len(nums)):
  for j in range(i+1,len(nums)):
    if sum==nums[i]+nums[j]:
      print(f"({nums[i]},{nums[j]})")
'''
      


#? 28. Remove all occurrences of a specific value from a list (without using remove()).
'''nums=[16,78,2,56,2,5,9,0,2]
n=2
nums=[x for x in nums if x!=n]
print(nums)
'''