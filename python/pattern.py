# 1 Ractangle + Square
'''for i in range(5):
  for j in range(5):
    if j==0 or j==4 or j==2 or i==0 or i==4 or i==2:
      print("* ",end="")
    else:
      print("  ",end="")
  print()'''


# Triangle
'''n=5
for i in range(n):
  for j in range(i+1):
    if j==0 or i==n-1 or j==i:
      print("* ",end="")
    else:
      print("  ",end="")
  print()'''

# for i in range(5):
#   for j in range(5,i):
#     print("  ",end="")
#   for k in range(i):
#     print("* ",end="")
#   print()



# X-X
'''n=6
for i in range(n):
  for j in range(n):
    if j==0 or i==n-1 or i==0 or j==n-1 or i==j or i==n//j:
      print("* ",end="")
    else:
      print("  ",end="")
  print()'''



# V-V
'''n=15
for i in range(n):
    for j in range(i):
        print(" ",end="")
    for k in range(n-i):
        if k==0 or k==n-1-i:
            print("* ",end="")
        else:
            print("  ",end="")
    print()'''

n=15
for i in range(n):
  for j in range(i+1):
    print("* ",end="")
  print()
for i in range(n-1):
  for j in range(n-1-i):
    print("* ",end="")
  print()