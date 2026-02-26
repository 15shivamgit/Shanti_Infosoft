# :white_check_mark: EASY LEVEL (Basics)
# If-Else (Easy)
# 1. Write a program to check whether a number is positive or negative.
'''num=float(input("Enter a number: "))
if num>0:
  print(f"{num} is a Pogetive number")
elif num<0:
  print(f"{num} is a Negative number")
else:
  print(f"{num} is a Zero")'''




# 2. Check if a number is even or odd.
'''num=int(input("Enter a number: "))
if num%2==0:
  print(f"{num} is a Even number")
else:
  print(f"{num} is a Odd number")'''





# 3. Find the greater number between two inputs.
'''n1=float(input("Enter first number: "))
n2=float(input("Enter second number: "))
if n1>n2:
  print(f"{n1} is greater then {n2}")
elif n1<n2:
  print(f"{n1} is greater then {n2}")
else:
  print(f"{n1} and {n2} are same")'''





# 4. Check whether a person is eligible to vote (age ≥ 18).
'''age = float(input("Enter your age: "))

if age<=0:
  print("Enter valid age!")
elif age>0 and age<18:
  print("Your are not eligible for vote")
else:
  print("Your are eligible for vote")'''




# 5. Check if a number is divisible by 5.
'''num=float(input("Enter a number: "))
if num==0:
  print("You're entered 0")
elif num%5==0:
  print(f"Yes, {num} is divisible by 5")
else:
  print(f"No, {num} is not divisible by 5")'''





# While Loop (Easy)
# 6. Print numbers from 1 to 10 using while.




# 7. Print numbers from 10 to 1 using while.
# 8. Print all even numbers from 1 to 50.
# 9. Find the sum of first 10 natural numbers.
# 10. Print the multiplication table of 5.

# Numeric (Easy)
# 11. Find the sum of digits of a number.
# 12. Reverse a number.
# 13. Count the number of digits.
# 14. Check if a number is multiple of 10.
# 15. Convert Celsius to Fahrenheit.

# :zap: MEDIUM LEVEL (Logic Building)
# If-Else (Medium)
# 16. Check whether a year is a leap year.
# 17. Find the largest among three numbers.
# 18. Calculate grade:
 
#  90+ → A
#  80+ → B
#  70+ → C
#  Else → Fail
# 19. Check if a number is 3-digit.
# 20. Find whether a character is vowel or consonant.

# While Loop (Medium)
# 21. Print all numbers between 100 to 200 divisible by 7.
# 22. Find factorial of a number using while.
# 23. Print Fibonacci series up to n terms.
# 24. Find the sum of even digits in a number.
# 25. Print all prime numbers between 1 and 50.

# Numeric (Medium)
# 26. Check if a number is palindrome.
# 27. Check if a number is Armstrong number.
'''num=int(input("Enter a number: "))
n=num
power=0
while num!=0:
  power+=1
  num//=10
print(power)'''




# 28. Find HCF (GCD) of two numbers.
'''n1=int(input("Enter first number: "))
n2=int(input("Enter second number: "))
HCF=None
while True:
  if n2%n1==0:
    HCF=n1
    break
  rem=n2%n1
  n2=n1
  n1=rem
print(f"HCF: {HCF}")'''
  





# 29. Find LCM of two numbers.
'''n1=int(input("Enter first number: "))
n2=int(input("Enter second number: "))
LCM=1
i=2
while i<=n1 and i<=n2:
  if n1%i==0 and n2%i==0:
    n1//=i
    n2//=i
    LCM*=i
  else:
    i+=1
print(f"LCM: {LCM*n1*n2}")'''




# 30. Find the product of digits.
'''num=int(input("Enter a number: "))
product=1
while num!=0:
  digit=num%10
  product*=digit
  num//=10
print(f"Producr of digit: {product}")'''





# :fire: HARD LEVEL (Advanced Logic)
# If-Else + While (Hard)
# 31. Create a menu-driven program:
#  1 → Add
#  2 → Subtract
#  3 → Multiply
#  4 → Divide
'''def add():
  n1=float(input("Enter first number: "))
  n2=float(input("Enter second number: "))
  print(f"Addition : {n1+n2}")

def sub():
  n1=float(input("Enter first number: "))
  n2=float(input("Enter second number: "))
  print(f"Substraction : {n1-n2}")

def multi():
  n1=float(input("Enter first number: "))
  n2=float(input("Enter second number: "))
  print(f"Multiplication : {n1*n2}")

def div():
  n1=float(input("Enter first number: "))
  n2=float(input("Enter second number: "))
  if n2==0:
    print("Not divisble by zero!")
  else:
    print(f"Division : {n1/n2}")

print("-----Menu-----")
print("1 Addition(+)")
print("2 Substraction(-)")
print("3 Multiplication(*)")
print("4 Division(/)")
print("5 Exit")
while True:
  choice=int(input("Enter your choice: "))
  match choice:
    case 1:
      add()
    case 2:
      sub()
    case 3:
      multi()
    case 4:
      div()
    case 5:
      print("Thank you!")
      break
    case _:
      print("Please enter valid choice: ")'''

  



# 32. ATM system:
#  Check balance
#  Withdraw
#  Deposit
#  Exit
'''def check_balance(bal):
  print(f"Balance {bal}")

def withdraw(bal):
  amt=float(input("Enter amount: "))
  if amt>0 and amt<=bal:
    bal-=amt
    print("Amount withdraw successfully")
  else:
    print("Invalid amount!")
  return bal
  
def deposit(bal):
  amt=float(input("Enter amount: "))
  if amt>0:
    bal+=amt
    print("Amount deposit successfully")
  else:
    print("Invalid amount!")
  return bal
pin=int(input("Enter your pin:  "))
if  pin==1234:
  bal=57000
  print("-----Option-----")
  print("1-Check Balance")
  print("2-Withdraw")
  print("3-Deposit")
  print("4-Exit")
  while True:
    choice=int(input("Enter your choice: "))
    match choice:
      case 1: 
        check_balance(bal)
      case 2: 
        bal=withdraw(bal)   
      case 3: 
        bal=deposit(bal)
      case 4: 
        print("Thank  you!")
        break
      case _: print("Please enter valid choice!")
else:
  print("Wrong pin! ") '''     








# 33. Validate password:
#  At least 8 chars
#  One number
#  One uppercase
'''password=input("Enter password: ")
upper_case=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
up=True
lower_case=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
lo=True
digit=['0','1','2','3','4','5','6','7','8','9']
dt=True
if len(password)>=8:
  for i in range(len(password)-1):
    if password[i] in upper_case:
      up=False
    if password[i] in lower_case:
      lo=False
    if password[i] in digit:
      dt=False

  if up:
    print("Your password must contain at least one uppercase letter.")
  elif lo:
    print("Your password must contain at least one lowercase letter.")
  elif dt:
    print("Your password must contain at least one number.")
  else:
    print("Password successfully genereated!")
else:
  print("Your password must be at least 8 characters long.")'''






# 34. Electricity bill calculator with slabs.
# 1-100=5
# 100-250=8
# 250++ = 10
# discount below 1000=no discount
# 1000-2500=5%
# 2500++=10%

'''unit = float(input("Enter Electric unit: "))
amt,total=0,0
if unit>=0 and unit<=100:
  amt = unit*5
elif unit>100 and unit<=250:
  amt = unit*8
elif unit>250:
  amt = unit*10
else:
  print("Please enter valid unit")
#Discount calculate
if amt<=1000:
  total = amt
elif amt<=2500:
  total = amt-(amt*0.05)
else:
  total = amt-(amt*0.10)
print(f"Your total electric bill : {total}")'''





# 35. Salary calculator with:
#  HRA(House rent allowance)
#  DA(Dearness allowance)
#  Tax
'''basic_salary=90500
HRA=8700
DA=6100
TAX=12/100
gross_salary=basic_salary+HRA+DA
print(f"Gross Salary: {gross_salary}")
net_salary=gross_salary-(gross_salary*TAX)
print(f"Net Salary: {net_salary}")'''






# While Loop (Hard)
# 36. Print this pattern using while:
#  1
#  12
#  123
#  1234
'''n=9
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()'''






# 37. Find all perfect numbers up to 1000.==perfect=sum of divisible (excluding it's self)
'''perfect=[]
for n in range(1,1000+1):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum+=i
    if sum==n:
        perfect.append(n)
print(perfect)'''



# 38. Check if a number is strong number.==sum of all digit fectorial
'''num=int(input("Enter a number: "))
n=num
sum=0
while num!=0:
  fect=1
  digit=num%10
  for i in range(1,digit+1):
    fect*=i
  sum+=fect
  num//=10
if n==sum:
  print(f"{n} is a strong number")
else:
  print(f"{n} is a not strong number")'''




# 39. Convert decimal to binary using while.
'''num=int(input("Enter a number: "))
rem=None
binary=''
while num!=0:
  rem=num%2
  binary=str(rem)+binary
  num//=2
print(binary)'''





# 40. Find square root using loop (no inbuilt function).
#num=int(input("Enter a number: "))







# Numeric + Logic (Hard)
# 41. Find the second largest digit in a number.
'''num=int(input("Enter a number: "))
large=0
n=num
while num!=0:
  digit=num%10
  if digit>large:
    large=digit
  num//=10
print(f"Large digit:  {large}")
sl=0
while n!=0:
  digit=n%10
  if digit<large and digit>sl:
    sl=digit
  n//=10
print(f" Second Large digit:  {sl}")'''





# 42. Check if two numbers are co-prime.
'''n1=int(input("Enter first number: "))
n2=int(input("Enter second number: "))
hcf=None
while True:
  hcf=n1%n2
  if n2!=1 and hcf!=0:
    n1=n2
    n2=hcf
    hcf=n1%n2
  if hcf==0:
    break
print(f"HCF : {n2}")
if hcf==1:
  print(f"{n1} and {n2} is co-prime number!")
else:
  print(f"{n1} and {n2} is not co-prime number!")'''




# 43. Generate random OTP of 6 digits.
'''import random
num=random.randint(111111,999999)
print(f"OTP : {num}")'''



# 44. Find missing number in array 1–n.






# 45. Check if a number is Harshad number.(num%sum_of_digit==0)
'''num=int(input("Enter a number: "))
sum,n=0,num
while num>0:
  digit=num%10
  sum+=digit
  num//=10

if n%sum==0:
  print(f"{n} is a Harshed number")
else:
  print(f"{n} is a not Harshed number")'''




# :rocket: 2025 Placement-Oriented Mixed Questions
# 46. Count how many numbers between 1–100 are divisible by both 3 and 5.
'''count=0
for i in range(1,101):
  if i%3==0 and i%5==0:
    count+=1

print(f"Total numbers between 1–100 are divisible by both 3 and 5: {count}")'''




# 47. Reverse only even digits in a number.
'''num=int(input("Enter a number: "))
rev=0
while num>0:
  digit=num%10
  if digit%2==0:
    rev = rev*10+digit
  num//=10

print("Reverse number: ",rev)'''






# 48. Check if a number is Spy Number (sum of digit= product of digits).
'''num=int(input("Enter a number: "))
sum,product,n=0,1,num
while num>0:
  digit=num%10
  sum+=digit
  product*=digit
  num//=10

if sum==product:
  print(f"{n} is a SPY number")
else:
  print(f"{n} is a not SPY number")'''




# 49. Create login system (3 attempts using while).
'''data={"ID":[],"PWD":[]}
i=0
while i<3:
  id=input("User id : ")
  passwd=input("Passward : ")
  data["ID"].append(id)
  data["PWD"].append(passwd)
  i+=1

print(data.items())'''





# 50. Find first 10 prime numbers using while.
'''count=0
prime=[]
n=1
while n<100:
  is_prime=True
  i=2
  while i<n:
    if n%i==0:
      is_prime=False
    i+=1

  if is_prime:
    prime.append(n)
    count+=1

  if count==10:
    break
  n+=1

print(f"First 10 prime number: {prime}")'''



