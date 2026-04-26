show databases;
use shivamdb;
show tables;

CREATE TABLE students (
  student_id INT PRIMARY KEY,
  name VARCHAR(50),
  email VARCHAR(100) UNIQUE,
  phone VARCHAR(15),
  city VARCHAR(50),
  age INT
);


CREATE TABLE courses (
  course_id INT PRIMARY KEY,
  course_name VARCHAR(50),
  duration INT,        -- in months
  fees DECIMAL(10,2)
);


CREATE TABLE teachers (
  teacher_id INT PRIMARY KEY,
  teacher_name VARCHAR(50),
  subject VARCHAR(50),
  experience INT
);


CREATE TABLE enrollments (
  enrollment_id INT PRIMARY KEY,
  student_id INT,
  course_id INT,
  teacher_id INT,
  enroll_date DATE,
  grade VARCHAR(2),

  FOREIGN KEY (student_id) REFERENCES students(student_id),
  FOREIGN KEY (course_id) REFERENCES courses(course_id),
  FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id)
);



INSERT INTO students VALUES
(1,'Amit','amit1@gmail.com','9876543210','Delhi',20),
(2,'Ravi','ravi2@gmail.com','9876543211','Mumbai',21),
(3,'Sita','sita3@gmail.com','9876543212','Pune',19),
(4,'Geeta','geeta4@gmail.com','9876543213','Delhi',22),
(5,'Raj','raj5@gmail.com','9876543214','Jaipur',23),
(6,'Priya','priya6@gmail.com','9876543215','Delhi',20),
(7,'Anil','anil7@gmail.com','9876543216','Mumbai',21),
(8,'Sunil','sunil8@gmail.com','9876543217','Pune',22),
(9,'Neha','neha9@gmail.com','9876543218','Delhi',20),
(10,'Pooja','pooja10@gmail.com','9876543219','Jaipur',19),
(11,'Karan','karan11@gmail.com','9876543220','Delhi',21),
(12,'Arjun','arjun12@gmail.com','9876543221','Mumbai',22),
(13,'Rohit','rohit13@gmail.com','9876543222','Pune',23),
(14,'Meena','meena14@gmail.com','9876543223','Delhi',20),
(15,'Vikas','vikas15@gmail.com','9876543224','Jaipur',21),
(16,'Nisha','nisha16@gmail.com','9876543225','Delhi',22),
(17,'Asha','asha17@gmail.com','9876543226','Mumbai',19),
(18,'Deepak','deepak18@gmail.com','9876543227','Pune',20),
(19,'Manoj','manoj19@gmail.com','9876543228','Delhi',23),
(20,'Tina','tina20@gmail.com','9876543229','Jaipur',21),
(21,'Rahul','rahul21@gmail.com','9876543230','Delhi',22),
(22,'Sneha','sneha22@gmail.com','9876543231','Mumbai',20),
(23,'Varun','varun23@gmail.com','9876543232','Pune',21),
(24,'Komal','komal24@gmail.com','9876543233','Delhi',19),
(25,'Yash','yash25@gmail.com','9876543234','Jaipur',22);



INSERT INTO courses VALUES
(101,'Math',6,5000),
(102,'Science',6,6000),
(103,'English',4,4000),
(104,'Computer',8,8000),
(105,'History',5,4500);


INSERT INTO teachers VALUES
(1,'Mr. Sharma','Math',10),
(2,'Ms. Gupta','Science',8),
(3,'Mr. Khan','English',6),
(4,'Ms. Verma','Computer',12),
(5,'Mr. Singh','History',9);


INSERT INTO enrollments VALUES
(1,1,101,1,'2024-01-10','A'),
(2,1,102,2,'2024-01-12','B'),
(3,2,103,3,'2024-01-15','A'),
(4,2,104,4,'2024-01-18','B'),
(5,3,101,1,'2024-02-01','C'),
(6,3,105,5,'2024-02-03','B'),
(7,4,102,2,'2024-02-05','A'),
(8,4,103,3,'2024-02-06','A'),
(9,5,104,4,'2024-02-08','B'),
(10,5,105,5,'2024-02-10','C'),

(11,6,101,1,'2024-03-01','A'),
(12,7,102,2,'2024-03-02','B'),
(13,8,103,3,'2024-03-03','A'),
(14,9,104,4,'2024-03-04','B'),
(15,10,105,5,'2024-03-05','A'),

(16,11,101,1,'2024-03-06','B'),
(17,12,102,2,'2024-03-07','A'),
(18,13,103,3,'2024-03-08','B'),
(19,14,104,4,'2024-03-09','A'),
(20,15,105,5,'2024-03-10','C'),

(21,16,101,1,'2024-03-11','A'),
(22,17,102,2,'2024-03-12','B'),
(23,18,103,3,'2024-03-13','A'),
(24,19,104,4,'2024-03-14','B'),
(25,20,105,5,'2024-03-15','A'),

(26,21,101,1,'2024-03-16','B'),
(27,22,102,2,'2024-03-17','A'),
(28,23,103,3,'2024-03-18','B'),
(29,24,104,4,'2024-03-19','A'),
(30,25,105,5,'2024-03-20','C');


select * from students;
select * from courses;
select * from teachers;
select * from enrollments;

-- 1. Student + Course
SELECT s.name, c.course_name
FROM students s
JOIN enrollments e ON s.student_id = e.student_id
JOIN courses c ON e.course_id = c.course_id;

-- 2. Student + Course + Teacher
SELECT s.name, c.course_name, t.teacher_name
FROM enrollments e
JOIN students s ON e.student_id = s.student_id
JOIN courses c ON e.course_id = c.course_id
JOIN teachers t ON e.teacher_id = t.teacher_id;


-- 3. LEFT JOIN Practice
SELECT s.name, e.course_id
FROM students s
LEFT JOIN enrollments e ON s.student_id = e.student_id;


-- find student inroll whos course and teacher
select s.name, c.course_name, t.teacher_name from students s 
join enrollments e on s.student_id=e.student_id 
join courses c on c.course_id=e.course_id 
join teachers t on t.teacher_id=e.teacher_id;


select * from students s 
left join enrollments e on e.student_id = s.student_id;

select * from enrollments ;




-- -------------- JOIN ----------------

-- 🔥 🔹 LEVEL 1: Basic JOIN (1–10)
-- Show all students with their course names
select s.name,c.course_name from students s 
left join enrollments e on e.student_id = s.student_id
left join courses c on c.course_id=e.course_id;

-- Show student name and teacher name
select s.name,t.teacher_name from students s 
left join enrollments e on e.student_id = s.student_id
left join teachers t on t.teacher_id=e.teacher_id;

-- List all enrollments with student details
-- Show course name with enrolled student names
-- Get all students who enrolled in "Math"
-- Show all teachers teaching any course
-- Display enrollment date with student name
-- Get course fees with student names
-- Show students with their grades
-- List all students and courses (INNER JOIN)
-- 🔥 🔹 LEVEL 2: LEFT JOIN (11–20)
-- Show all students and their courses (include students with no course)
-- Find students who are NOT enrolled in any course
-- Show all courses with students (include empty courses)
-- Find courses with no enrollments
-- Show all teachers with assigned courses
-- Find teachers who are not teaching any course
-- Show all students with grades (include NULL grades)
-- Get students with or without enrollment
-- Show course list with number of students
-- List students who didn’t get any grade
-- 🔥 🔹 LEVEL 3: RIGHT JOIN (21–25)
-- Show all courses with student names (RIGHT JOIN)
-- Find courses with no students using RIGHT JOIN
-- Show all teachers even if they have no students
-- Display course and teacher even if no enrollment exists
-- Show all records from courses and matching students
-- 🔥 🔹 LEVEL 4: MULTIPLE JOIN (26–35)
-- Show student name, course name, and teacher name
-- Display student + course + grade + teacher experience
-- Get students enrolled after a specific date with course
-- Show all enrollments with full details
-- Find students with grade ‘A’ and their courses
-- Get teacher-wise student list
-- Count students per teacher
-- Show courses with highest number of students
-- Find students enrolled in more than one course
-- Display top 3 courses with highest enrollments
-- 🔥 🔹 LEVEL 5: ADVANCED JOIN (36–45)
-- Find students who enrolled in ALL courses
-- Find students who enrolled in ONLY one course
-- Show students with same course (self join concept)
-- Find duplicate enrollments (if any)
-- Show highest grade student in each course
-- Find students who share same teacher
-- Display student pairs in same course
-- Get courses with average grade
-- Find teachers teaching multiple courses
-- Show course with highest fee and enrolled students
-- 🔥 🔹 LEVEL 6: INTERVIEW LEVEL (46–50)
-- Find second highest enrolled course
-- Show students who never got grade 'A'
-- Find top-performing student (based on grades)
-- Get student who enrolled earliest in each course
-- Show students who enrolled in both Math AND Science


