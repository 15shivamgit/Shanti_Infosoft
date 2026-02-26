'''dict={
  "name":"Shivam",
  'age':24,
  'cgpa':8.9
}
print(dict)
for key in  dict:
  print(dict[key])

'''





student = {
    "student_id": "STU10234",
    "personal_info": {
        "first_name": "Rahul",
        "last_name": "Sharma",
        "gender": "Male",
        "age": 21,
        "date_of_birth": "2004-05-14",
        "contact": {
            "email": "rahul.sharma@email.com",
            "phone": "9876543210",
            "address": {
                "street": "MG Road",
                "city": "Indore",
                "state": "Madhya Pradesh",
                "pincode": "452001"
            }
        }
    },

    "academic_info": {
        "course": "B.Tech",
        "branch": "Computer Science",
        "year": 3,
        "semester": 6,
        "roll_number": "CSE20230045",
        "subjects": [
            {"name": "Data Structures", "code": "CS301", "marks": 85},
            {"name": "Operating System", "code": "CS302", "marks": 78},
            {"name": "Database Management", "code": "CS303", "marks": 88},
            {"name": "Computer Networks", "code": "CS304", "marks": 81}
        ]
    },

    "attendance": {
        "total_classes": 120,
        "attended": 102,
        "percentage": 85.0
    },

    "skills": [
        "Python",
        "Java",
        "React",
        "SQL"
    ],

    "projects": [
        {
            "title": "Student Management System",
            "technology": "Python, MySQL",
            "duration": "3 months"
        },
        {
            "title": "E-commerce Website",
            "technology": "React, Node.js",
            "duration": "4 months"
        }
    ],

    "status": "Active"
}
# sum=0;
# for i in student["academic_info"]["subjects"]:
#    sum+= i["marks"]

# print(sum)
# for i in student["projects"]:
#     print(i["technology"].split(",")[0])




#print(student["personal_info"]['contact']['address']['city'])
print(student["personal_info"]['contact']['address']['city'])
