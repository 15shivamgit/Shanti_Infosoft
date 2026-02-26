#   Left triangle
'''n=6
for i in range(n):
    for j in range(i+1):
        if j==0 or i==n-1 or i==j:
            print("* ",end="")
        else:
            print("  ",end="")
    print()'''


# Right Triangle
'''n=6
for i in range(n):
    for j in range(n-1-i):
        print(". ",end="")
    for k in range(i+1):
        if k==0 or i==n-1 or i==k:
            print("* ",end="")
        else:
            print("  ",end="")
    print()'''


# Cross-X
'''n=6
for i in range(n):
    for j in range(n):
        if i==j or i==n-1-j:
            print("* ",end="")
        else:
            print("  ",end="")
    print()'''

# T-T
'''n=5
for i in range(n):
    for j in range(n):
        if i==0 or j==2:
            print("* ",end="")
        else:
            print("  ",end="")
    print()'''

#   A-A
'''n=5
for i in range(n):
    for j in range(n-1-i):
        print(" ",end="")
    for k in range(i+1):
        if k==0 or i==n-n//2 or i==k:
            print("* ",end="")
        else:
            print("  ",end="")
    print()'''


#
n=6
for i in range(n):
    for j in range(i):
        print("  ",end="")
    for k in range(i+1):
        print("* ",end="")
    print()