# for i in range(123):
#   print(i," - ",chr(i))

# print(ord(" "))

# list=['abc','4','6','xyz','1','pqr']
# for x in list:
#   if x.isdigit():
#     print(x)

#print(type(list[2]))

# n=10
# if type(n)==int:
#   print("yes")
# else:
#   print("no")


# print(2.5%1)
# print("Hello" and "Word")
# print(1 and "Word")
# print("" or "Word")

# n=[1,2,3]
# n.insert(-1,7)
# print(n)
# long=n[0]
# for x in n:
#   if x>long:
#     long=x
# print(x)


#! 14. Separate even and odd numbers into two different lists.
'''nums=[1,2,3,4,5,6,7,8,9,10]
even=[]
odd=[]
for num in nums:
  if num%2==0:
    even+=[num]
  else:
    odd+=[num]
print(f"Even number: {even}")
print(f"Odd number: {odd}")'''

# Input: arr[] = [1, 4, 11, 51, 15], low = 50, high = 55
# Output: [50, 52, 53, 54, 55]
# Explaination: Numbers 50, 52, 53, 54 and 55 lie in the range [50, 55] but are not present in the array.


# n=[10,20,30,40,50]
# print(n)
# n+=[n[0]]
# print(n)
# n=[n[x] for x in range(len(n)) if x!=0]
# print(n)




'''class Solution:
    def findDuplicates(self, arr):
        # code here
        result=[]
        for num in arr:
            if arr.count(num)>1 and num not in result:
                result.append(num)
                
        return result
    '''    


'''class Solution:
    def missingRange(self, arr, low, high):
        #code here
        rangeList=list(range(low,high+1))
        result=[]
        
        for x in rangeList:
            if x not in arr:
                result.append(x)
                
        return result'''

# arr = [2, 3, 1, 2, 3]
# temp=list(set(arr))  
# print(temp)
# arr=[x for x in arr if x not in temp]
# print(arr) 


'''str=['A','Z','a','z','1','9','@',' ','_',',','+']
print(sorted(str))'''

# lst=[5,4,4,5,1,2,3,6,2,]
# lst=[x  for x   in  lst if  lst.count(x)>1]

# print(lst)


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


# Sliding Window concept:

# Ek window start karo

# Elements add karte jao

# Agar sum target se bada ho jaaye:

# Left side se elements hatao

# Jaise hi sum == target:

# Indices return karo

# End tak pahunch gaye aur nahi mila → [-1]


'''arr=[10,10]
res=[]
for x in arr:
  if arr.count(x)>1 and x not in res:
    res.append(x)
print(res)'''


'''arr=[1,2,2,3]
sum=8
f='False'
for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j]==sum:
                f='True'
                break

print(f)'''


# str='Shivam'
# newstr=sorted(str)
# print(newstr)
# print(list(str))


'''a = ["Texas", "California", "Florida"] # states
b = ["Austin", "Sacramento", "Tallahassee"] # capital
print(list(zip(a,b)))
res = {state: capital for state, capital in zip(a, b)}
print(res)'''

'''std={
  'name':"Shivam",
  'age':24,
  'cgpa':8.9
}
for _,y  in std.items():
    print(_,y)'''
'''
lst=[1,2,3,4,5,6,7,8,9,10,'s']
lst=[x if x%2==0 elif x=='s' "Shivam"  else 0 for x in lst]
print(lst)'''

lst=[(i,j) for i in range(2) for j in range(2)]  
print(lst)