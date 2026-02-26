# :large_yellow_circle: INTERMEDIATE LEVEL
#? 1. Dictionary – Student Marks
# Create a dictionary of 5 students with marks.
#  Print the student name who got highest marks.
# Example:
# students = {
#     "Rahul": 85,
#     "Amit": 90,
#     "Neha": 78,
#     "Priya": 92,
#     "Karan": 88
# }
# Output: Priya

'''
std={
  'Shivam':89,
  'Aditi':90,
  'Yukti':91,
  'Smrati':86,
  'Pranaw':88
}
high=0
name=''
for key in std:
  if std[key]>high:
    high=std[key]
    name=key
print(f'Highest marks of student : {name}')
'''


#? 2. Dictionary – Employee Salary
# Store employee salary and increase salary by 10% for each employee.
# Example:
# employees = {
#     "Rahul": 25000,
#     "Amit": 30000,
#     "Neha": 28000
# }
# Output:
# Rahul 27500
# Amit 33000
# Neha 30800
'''
emp={
  'Shivam':89000,
  'Aditi':90000,
  'Yukti':91000,
  'Smrati':86000,
  'Pranaw':88000
}
for key in emp:
  sal=emp[key]+(emp[key]*0.10)
  print(key,"\t",sal)
'''


#? 3. Tuple – Store Coordinates
# Store GPS coordinates in tuple and print latitude and longitude separately.
# Example:
# location = (22.7196, 75.8577)
# Output:
# Latitude: 22.7196
# Longitude: 75.8577
'''
location = (22.7196, 75.8577)
Latitude,Longitude=location
print(f'Latitude: {Latitude}')
print(f'Longitude: {Longitude}')
'''

# 4. Set – Unique Visitors
# You have website visitors list. Remove duplicates using set.
# Example:
# visitors = ["Rahul", "Amit", "Rahul", "Neha", "Amit"]
# Output:
# {'Rahul', 'Amit', 'Neha'}
'''
visitors = ["Rahul", "Amit", "Rahul", "Neha", "Amit"]
visitors=set(visitors)
print(visitors)
'''

# :large_orange_circle: MEDIUM LEVEL
#? 5. Dictionary – Product Inventory
# Store product and quantity. Print products with quantity less than 10.
# Example:
# products = {
#     "Laptop": 5,
#     "Mouse": 25,
#     "Keyboard": 8,
#     "Monitor": 12
# }
# Output:
# Laptop
# Keyboard
'''
products = {
    "Laptop": 5,
    "Mouse": 25,
    "Keyboard": 8,
    "Monitor": 12
}
for key in products:
  if products[key]<10:
    print(key,'-',products[key])
'''



#? 6. Dictionary – Student Subject Marks
# student = {
#     "Math": 85,
#     "Science": 78,
#     "English": 92,
#     "Computer": 88
# }
# Task:
# Calculate total marks
# Calculate average marks
# Output:
# Total: 343
# Average: 85.75
'''
student = {
    "Math": 85,
    "Science": 78,
    "English": 92,
    "Computer": 88
}
total_marks=0
for key in student:
  total_marks+=student[key]

average=total_marks/len(student)
print(f'Total marks : {total_marks}')
print(f'Average : {average}')
'''


#? 7. Tuple – Employee Records
# Store employee data in tuple:
# (id, name, salary)
# Print employee name and salary.
# Example:
# emp = (101, "Rahul", 35000)
# Output:
# Rahul 35000
'''
emp=(101,'Shivam',110000)
print(emp[1],emp[2])
'''

#? 8. Set – Common Students in two classes
# classA = {"Rahul", "Amit", "Neha"}
# classB = {"Neha", "Priya", "Amit"}
# Output:
# {'Neha', 'Amit'}
'''
classA = {"Rahul", "Amit", "Neha"}
classB = {"Neha", "Priya", "Amit"}
print(classA.intersection(classB))
'''


# :red_circle: ADVANCED LEVEL
#? 9. Dictionary – Student Database (Nested)
# students = {
#     "Rahul": {"Math": 85, "Science": 90},
#     "Amit": {"Math": 78, "Science": 82},
#     "Neha": {"Math": 92, "Science": 88}
# }
# Task:
#  Print student name with average marks.
# Output:
# Rahul 87.5
# Amit 80.0
# Neha 90.0
'''
students = {
    "Rahul": {"Math": 85, "Science": 90},
    "Amit": {"Math": 78, "Science": 82},
    "Neha": {"Math": 92, "Science": 88}
}

for key in students:
  marks=0
  for x in students[key]:
    marks+=students[key][x]
  print(key,marks/len(students[key]))
'''



#? 10. Dictionary – Online Shopping Cart
# cart = {
#     "Laptop": {"price": 50000, "qty": 1},
#     "Mouse": {"price": 500, "qty": 2},
#     "Keyboard": {"price": 1500, "qty": 1}
# }
# Task:
#  Calculate total bill.
# Output: 52500
'''
cart = {
    "Laptop": {"price": 50000, "qty": 1},
    "Mouse": {"price": 500, "qty": 2},
    "Keyboard": {"price": 1500, "qty": 1}
}
bill=0
for key in cart:
  bill+=cart[key]['price']*cart[key]['qty']
print(f'Total bill : {bill}')
'''


#? 11. Tuple – Student Records System
# students = (
#     (101, "Rahul", 85),
#     (102, "Amit", 90),
#     (103, "Neha", 78)
# )
# Task:
#  Print student with marks > 80
# Output:
# Rahul
# Amit
'''
students = (
    (101, "Rahul", 85),
    (102, "Amit", 90),
    (103, "Neha", 78)
)
for i in students:
  if i[-1]>80:
    print(i[1])
'''



#? 12. Set – Find Missing Numbers
# all_students = {"Rahul", "Amit", "Neha", "Priya", "Karan"}
# present_students = {"Rahul", "Neha"}
# Output:
# {'Amit', 'Priya', 'Karan'}
'''
all_students = {"Rahul", "Amit", "Neha", "Priya", "Karan"}
present_students = {"Rahul", "Neha"}
# print(all_students-present_students)
print(all_students.difference(present_students))
'''



# :fire: ADVANCED REAL-WORLD CHALLENGE (IMPORTANT)
#? 13. Employee Database
# employees = {
#     "E101": {
#         "name": "Rahul",
#         "department": "IT",
#         "salary": 50000
#     },
#     "E102": {
#         "name": "Amit",
#         "department": "HR",
#         "salary": 40000
#     },
#     "E103": {
#         "name": "Neha",
#         "department": "IT",
#         "salary": 55000
#     }
# }
# Tasks:
# Print all IT employees
# Print highest salary employee
# Increase salary by 5000
'''
employees = {
    "E101": {
        "name": "Rahul",
        "department": "IT",
        "salary": 50000
    },
    "E102": {
        "name": "Amit",
        "department": "HR",
        "salary": 40000
    },
    "E103": {
        "name": "Neha",
        "department": "IT",
        "salary": 55000
    }
}
high=0
name=''
for key in employees:

  #Print all IT employees
  print(employees[key]['name'],end=' ')

  #Calculate highest salary employee
  if employees[key]['salary']>high:
    name=employees[key]['name']
    high=employees[key]['salary']

  #Increase salary by 5000
  employees[key]['salary']+=5000

print(f'\nHighest salary employee {name}: {high}')
'''


# :brain: VERY ADVANCED INTERVIEW LEVEL
#? 14. E-commerce Orders
# orders = {
#     101: {"product": "Laptop", "price": 50000},
#     102: {"product": "Mouse", "price": 500},
#     103: {"product": "Keyboard", "price": 1500}
# }
# Tasks:
# Find total revenue
# Find most expensive product
'''
orders = {
    101: {"product": "Laptop", "price": 50000},
    102: {"product": "Mouse", "price": 500},
    103: {"product": "Keyboard", "price": 1500}
}
revenue=0
expensive=orders[101]['price']
name=''
for key in orders:
  #Find total revenue
  revenue+=orders[key]['price']
  #Find most expensive product
  if orders[key]['price']>=expensive:    
    name=orders[key]['product']
    expensive=orders[key]['price']

print(f'Total revenue : {revenue}')
print(f"Most expensive product '{name}' : {expensive}")
'''







#! REAL-WORLD HARD DATA (E-Commerce Company)
company = {
    "employees": {
        "E101": {
            "name": "Rahul Sharma",
            "department": "IT",
            "salary": 55000,
            "skills": ["Python", "SQL", "React"],
            "projects": ("Ecommerce", "Dashboard")
        },
        "E102": {
            "name": "Neha Verma",
            "department": "Sales",
            "salary": 48000,
            "skills": ["Excel", "Communication"],
            "projects": ("Leads",)
        },
        "E103": {
            "name": "Amit Singh",
            "department": "IT",
            "salary": 62000,
            "skills": ["Python", "Django", "AWS"],
            "projects": ("API", "Cloud")
        },
        "E104": {
            "name": "Priya Patel",
            "department": "HR",
            "salary": 45000,
            "skills": ["Communication", "Management"],
            "projects": ("Hiring",)
        }
    },

    "products": {
        "P201": {
            "name": "Laptop",
            "price": 55000,
            "stock": 10,
            "sold": [2, 1, 3, 2]
        },
        "P202": {
            "name": "Mouse",
            "price": 700,
            "stock": 50,
            "sold": [5, 8, 6, 10]
        },
        "P203": {
            "name": "Keyboard",
            "price": 1500,
            "stock": 30,
            "sold": [3, 4, 2]
        }
    },

    "customers": {
        "C301": {
            "name": "Arjun",
            "city": "Indore",
            "purchases": ["Laptop", "Mouse"],
            "amount": (55000, 700)
        },
        "C302": {
            "name": "Simran",
            "city": "Bhopal",
            "purchases": ["Keyboard"],
            "amount": (1500,)
        },
        "C303": {
            "name": "Rohit",
            "city": "Delhi",
            "purchases": ["Laptop", "Keyboard"],
            "amount": (55000, 1500)
        }
    }
}

# :fire: 12 HARD QUESTIONS

#! Q1. Find highest salary employee name
# Expected Output:Amit Singh
'''
high=0
name=''
for key in company['employees']:
    temp=company["employees"][key]['salary']
    if temp>high:
       name=company["employees"][key]['name']
       high=temp
print(name)
'''



#! Q2. Find total salary of all employees
# Expected Output:  210000
'''
total=0
for key in company['employees']:
    total+=company["employees"][key]['salary']
print(total)
'''

#! Q3. Find all employees who know Python
# Expected Output:
# Rahul Sharma
# Amit Singh
'''
for key in company['employees']:
    if 'Python' in company["employees"][key]['skills']:
       print(company["employees"][key]['name'])
'''



#! Q4. Find employee working on maximum number of projects
# Expected Output:  Rahul Sharma
'''
large=0
name=''
for dic in company["employees"].values():
  if len(dic)>large:
    large=len(dic)
    name=dic['name']

print(name)
'''



#! Q5. Find total revenue generated by each product
# Expected Output:
# Laptop 440000
# Mouse 20300
# Keyboard 13500
'''
for val in company["products"].values():
  revenue=sum(val['sold'])*val['price']
  print(val['name'],revenue)
'''




#! Q6. Find most sold product
# Expected Output:  Mouse
'''
name=''
max_pro=0
for val in company["products"].values():
  sold=sum(val['sold'])
  if sold>max_pro:
    name=val['name']
    max_pro=sold

print(name)
'''



#! Q7. Find product with lowest stock
# Expected Output:  Laptop
'''
name=company["products"]['P201']['name']
max_pro=sum(company["products"]['P201']['sold'])
for val in company["products"].values():
  sold=sum(val['sold'])
  if sold<max_pro:
    name=val['name']
    max_pro=sold

print(name)
'''




#! Q8. Find customer who spent most money
# Expected Output:  Rohit
'''
most=0
name=''
for dic in company["customers"].values():
  temp=sum(dic['amount'])
  if temp>most:
    name=dic['name']
    most=temp
print(name)
'''

#! Q9. Find total revenue from all customers
# Expected Output:  113700
'''
revenue=0
for dic in company["customers"].values():
  revenue+=sum(dic['amount'])

print(f'Total revenue of customer : {revenue}')
 ''' 





#! Q10. Find all unique skills in company (use set)
# Expected Output:
# {'Python', 'SQL', 'React', 'Excel', 'Communication', 'Django', 'AWS', 'Management'}
'''
skills=set()
for dic in company["employees"].values():
  skills.update(dic['skills'])
print(skills)
'''



#! Q11. Find department with highest total salary
# Expected Output: IT
'''
most=0
dept=''
for dic in company["employees"].values():
  if dic['salary']>most:
    dept=dic['department']
    most=dic["salary"]
print(dept)
'''




#! Q12. Find most expensive product purchased by customers
# Expected Output: Laptop

most=0
name=''
for dic in company["products"].values():
  if dic['price']>most:
    most=dic["price"]
    name=dic['name']
print(name)