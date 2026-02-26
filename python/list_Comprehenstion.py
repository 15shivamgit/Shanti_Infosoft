# lst=[1,2,3,4,5,6,7,8,9]
# #lst=[x for x in lst if x%2==0]
# lst=[x for x in lst if x%2!=0]
# print(lst)


# lst=['Shivam Kumar','Aditi Singh','Smarti Nigam','Yukti Singh','Pranaw Gautam']
# lst=[x[0] for x in lst]
# print(lst)


# lst=[1,2,3,4,5,6,7,8,9]
# mylstr=[x for x in lst if x!=2]
# print(lst)
# print(mylstr)

# lst=[x for x in range(10,0,-1) if x>5]
# print(lst)


# lst=['Shivam Kumar','Aditi Singh','Smarti Nigam','Yukti Singh','Pranaw Gautam']
# lst=[x.upper() for x in lst]
# print(lst)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = ['hello' for x in fruits]
# print(fruits)
# print(newlist)
# newlist = [x if x != "banana" else "orange" for x in fruits]
# print(newlist)


# lst=[x if x%2==0 else 0 for x in range(1,11)]
# print(lst)



# lst=[1,2,3,4,2,3,5]
# lst=[x if lst.count(x)!=1 else lst.remove(x) for x in lst]
# print(lst)