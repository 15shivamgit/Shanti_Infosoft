'''
def abc():
  print("Hello")

abc()

def syz(a,b):
  print("Product of two number :",a*b)

syz(10,12)  

def pqr(a,b):
  return a*b

print(pqr(11,19))
 '''

def findEven(lst):
  sum=0
  '''for x in  lst:
    if x%2==0:
      sum+=x'''
  
  sum=[x for x in lst if x%2==0]

  return sum      

num=[1,2,3,4,5,6,7,8,9,10]
print(findEven(num))