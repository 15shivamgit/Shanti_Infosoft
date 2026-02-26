#? Ladder 
'''arr = [16, 17, 4, 3, 5, 2] #! output-[17, 5, 2],
res=[]
last=arr[-1]
for i in range(len(arr)-1,-1,-1):
  if arr[i]>=last:
    res.append(arr[i])
    last=arr[i]
  
res.reverse()  
print(res)'''


#?  Jumping through While - Python
'''n=100
i=1
while i**2<=n:
  print(i**2)
  # if i**2>n:
  #   break
  i+=1'''

'''N=5
for x in range(1,11):
    print(x*N,end=' ')'''


#?  The FizzBuzz Program
'''arr = tuple(map(int, input().split()))
if len(arr)==len(set(arr)):
  print(False)
else:
  print(True)
print(arr)'''



# s="Shivam"
# print(s[::-1])


#? Slicing in String - Python
'''bound_by = '[[]]'
tag_name = 'tag'
# bound_by = '<>'
# tag_name = 'body'
print(bound_by[:len(bound_by)//2] + tag_name + bound_by[len(bound_by)//2:])'''



#?  Day before N days
'''
0 - Sunday
1 - Monday
2 - Tuesday
3 - Wednesday
4 - Thursday
5 - Friday
6 - Saturday
'''
# d=2
# n=19
# n=n%7

'''arr=[1, 2, 3, 3,8,0]
sum = 8
flag=False
for i in range(len(arr)):
  for j in range(len(arr)):
    if i!=j and arr[i]+arr[j]==sum:
      flag=True
      break
if flag:
  print("True")
else:
  print("False")
'''


#? count digit
'''
n=2442
num=n
count=0
check=[]
while n!=0:
  digit=n%10
  if num%digit==0 and digit not in check:
    count+=1
    check.append(digit)
  n//=10
print(count)
'''


# Palidrome
# s1="geeks"
# s2="kseeg"
# print(sorted(s1)==sorted(s2))
# print(sorted(s2))


# Anagram
# s1="geeks"
# s2="kseeg"
# temp=list(s2)
# for x in s1:
#   if x in temp:
#     temp.remove(x)

# if len(temp)==0 and len(s1)==len(s2):
#   print(True)
# else:
#   print(False)


# Power of 2
# n=1
# i=0
# check=False
# while pow(2,i)<=n:
#   if pow(2,i)==n:
#     check=True
#     break
#   i+=1

# print(check)




# Reverse word
# s = "i.like.this.program.very.much"
# # "much.very.program.this.like.i"
# s2='..geeks..for.geeks.'
# # geeks.for.geeks
# print(s2.split('.'))
# print(s2.split(".")[::-1])
# temp=s2.split(".")[::-1]
# temp=[x for x in temp if x!='']
# print('.'.join(temp))




# Smallest Positive Missing
arr=[1,2,3,5]
# small=arr[0]
# for x in arr:
#   if x>0 and x<small:
#     small=x
# print(small)

'''n=max(arr)
small=0
for i in range(1,n):
  if i not in arr:
    small=i
    break
print(n)
'''

# Rotate array
arr=[1,2,3,4,5]
d=2
# for i in range(d):
#   arr+=[arr[0]]
#   arr=arr[1:]
  # arr.pop(0)

  # arr.append(arr.pop(0))

print(arr)
'''class hello:
  def rotateArr(self,arr, d):
    #Your code here
    for i in range(d):
      arr+=[arr[0]]
      arr=arr[1:]      
    return arr
s1=hello()
print(s1.rotateArr(arr,d))'''


for i in range(d):
  arr+=[arr[0]]
  arr=arr[1:]  
print(arr)