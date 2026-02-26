#1 WAP to check user is eligible or not for voting- 1) if user age is above 18 and below 40 and gender is male, 2) if user age is above 18 and below 30 and gender is female.

'''gen=input("Enter your gender: ").lower()
age=float(input("Enter your age: "))

if gen == "male":
  if age>=18 and age<=40:
    print("You are eligible for voting")
  elif age>0 and age<100:
    print("You are not eligible for voting")
  else:
    print("Please enter valid age")
elif gen == "female":
  if age>=18 and age<=30:
    print("You are eligible for voting")
  elif age>0 and age<100:
    print("You are not eligible for voting")
  else:
    print("Please enter valid age")
else:
  print("Enter valid gender")'''





#2 WAP to calculate electricity bill, the conditions given below
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





#3  Print sum of digit in the number.

'''num = int(input("Enter a numbere: "))
sum = 0
while num>0:
  digit = num%10
  sum += digit
  num //= 10

print(f"Sum of digit : {sum}")'''





#4 WAP to check the given number prime number or not

'''num = int(input("Entr a number: "))
is_prime = True
for i in range(2,num):
  if num%i==0:
    is_prime=False
    break

if is_prime:
  print(f"{num} is a prime number")
else:
  print(f"{num} is a not prime number")'''





#4  WAP to print all prime number 1-100 and also count total prime number.

'''count=0
prime=[]
for n in range(1,101):
  is_prime=True
  for i in range(2,n):
    if n%i==0:
      is_prime=False

  if is_prime:
    count += 1
    prime.append(n)

print(f"Total prime number between 1-100: {count}")
print(f"Prime number: {prime}")'''







