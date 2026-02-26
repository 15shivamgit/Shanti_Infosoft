'''name=['shivamk','aditi','pranaw','smrati','yukti','yukti']
for i in  range(len(name)):
  if  len(name[i])%2==1:
    print(name[i],'-',name[i][len(name[i])//2])
'''



#! access a list item 
'''friends=['shivam kumar','aditi singh','pranaw gautam','smrati nigam','yukti singh']
newfd=[]
for fd in friends:
  temp=fd.split(' ')
  newfd.append((temp[0][0]+temp[1][0]).upper())

print(newfd)'''

#? reverse a list of item and store diffrent list
'''friends=['shivam kumar','aditi singh','pranaw gautam','smrati nigam','yukti singh']
newfd=[]
for fd in friends:
  n=''
  for i  in range(len(fd)):
    n=fd[i]+n
  newfd.append(n)

print(newfd)'''



#? reverse a list of item and store same list
'''friends=['shivam kumar','aditi singh','pranaw gautam','smrati nigam','yukti singh']
for i in range(len(friends)):
  name=''
  for j  in range(len(friends[i])):
    name=friends[i][j]+name
  friends[i]=name

print(friends)
'''

'''friends=['shivam kumar','aditi singh','pranaw gautam','smrati nigam','yukti singh']
for i in range(len(friends)):
  name=friends[i][::-1]
  friends[i]=name

print(friends)'''





#? reverse character  word of list  items and store same list
'''friends=['shivam kumar','aditi singh','pranaw gautam','smrati nigam','yukti singh']
for i in range(len(friends)):
  name=friends[i].split(' ')
  rev=name[0][::-1]+" "+name[1][::-1]
  friends[i]=rev

print(friends)'''

#? reverse character  word of list  items and store same list
friends=['shivam kumar','aditi singh','pranaw gautam','smrati nigam','yukti singh']
'''for i in range(len(friends)):
  name=friends[i].split(' ')
  rev=[]
  for j in range(len(name)): 
    rev.append(name[j][::-1])

  friends[i]=" ".join(rev)

print(friends)'''


#! Find second largest item in list
'''num=[21,4,35,65,76,34,3,12,43,67,100]
max=num[0]
sec_max=0
for i in range(len(num)):
  if num[i]>max:
    sec_max=max
    max=num[i]
  if num[i]<max and num[i]>sec_max:
    sec_max=num[i]
print(sec_max)'''

#! find how many palidrome string in a list and also find longest palidrome string
name=['shivam','naman','121','pranm','jahaj','1234321']
count=0
length=0
max_str=''
for i in range(len(name)):
  temp=name[i][::-1]
  if name[i]==temp:
    count+=1
    if len(temp)>length:
      length=len(temp)
      max_str=temp
print(f"Number of palidrome string : {count}")
print(f"Longest palidrome string : {max_str}")