show databases;

use shivamdb;
show tables;

create table employees(
	emp_id varchar(16) primary key check(emp_id regexp '^shanti_emp_[0-9]{5}$'),
    full_name varchar(30) not null,
    dob date not null,
    age int check(age>=18 and age<=80),
    gender enum('M', 'F','O'),
    city varchar(15) not null,
    state varchar(15),
    department varchar(30) not null,
    role varchar(20) not null,
    work_location varchar(20),
    working_mode enum('On-site', 'Remote', 'Hybrid'),
    emp_type enum('Full-time', 'Part-time', 'Intern'),
    shift enum('Day', 'Night', 'Both'),
    joining_date date not null,
    number_of_projects int,
    experience decimal(2,1) not null check(experience >= 0),
    report_manager_name varchar(30) not null,
    salary decimal(7,2) not null check(salary >= 0 ),
    complete_year decimal(2,1) not null check(complete_year >= 0),
    appraisal_date date,
    promotion_date date,
    last_work_date date
);

show tables;

desc employees;

-- alter column (salary,experience,complete_year) size
alter table employees modify salary decimal(10,2) not null check(salary >= 0 );
alter table employees modify experience decimal(3,1) not null check(experience >= 0);
alter table employees modify complete_year decimal(3,1) not null check(complete_year >= 0);



-- 20 record insert
INSERT INTO employees VALUES
('shanti_emp_10001','Amit Sharma','1998-05-10',26,'M','Delhi','Delhi','IT','Developer','Indore','On-site','Full-time','Day','2022-06-01',3,2.5,'Rakesh Singh',75000,2.0,'2024-04-01','2023-06-01',NULL),

('shanti_emp_10002','Neha Verma','2000-08-15',24,'F','Indore','MP','HR','Executive','Indore','Hybrid','Full-time','Day','2023-01-10',2,1.5,'Pooja Jain',45000,1.0,'2024-04-01',NULL,NULL),

('shanti_emp_10003','Rahul Yadav','1997-12-20',27,'M','Lucknow','UP','IT','Tester','Indore','On-site','Full-time','Night','2021-03-15',4,3.5,'Amit Sharma',55000,3.0,'2024-04-01','2022-03-15',NULL),

('shanti_emp_10004','Priya Singh','2001-02-25',23,'F','Patna','Bihar','Finance','Analyst','Indore','Remote','Full-time','Day','2023-05-01',2,1.2,'Rajesh Gupta',60000,1.0,'2024-04-01',NULL,NULL),

('shanti_emp_10005','Karan Mehta','1995-07-07',29,'M','Mumbai','MH','Sales','Manager','Indore','On-site','Full-time','Day','2019-08-01',6,5.0,'Suresh Jain',90000,5.0,'2024-04-01','2021-08-01',NULL),

('shanti_emp_10006','Simran Kaur','2002-11-11',22,'F','Amritsar','Punjab','IT','Intern','Indore','Remote','Intern','Day','2024-01-01',1,0.5,'Amit Sharma',25000,0.5,'2024-04-01',NULL,NULL),

('shanti_emp_10007','Vikas Gupta','1996-04-18',28,'M','Jaipur','RJ','IT','DevOps','Indore','Hybrid','Full-time','Night','2020-06-01',5,4.0,'Amit Sharma',85000,4.0,'2024-04-01','2022-06-01',NULL),

('shanti_emp_10008','Anjali Das','1999-09-09',25,'F','Kolkata','WB','HR','Manager','Indore','On-site','Full-time','Day','2021-07-01',3,3.0,'Pooja Jain',70000,3.0,'2024-04-01','2023-07-01',NULL),

('shanti_emp_10009','Rohit Kumar','1994-01-01',30,'M','Delhi','Delhi','IT','Lead','Indore','On-site','Full-time','Day','2018-05-01',7,6.0,'Amit Sharma',95000,6.0,'2024-04-01','2020-05-01',NULL),

('shanti_emp_10010','Pooja Singh','2001-03-03',23,'F','Varanasi','UP','Finance','Executive','Indore','Hybrid','Full-time','Day','2023-09-01',2,1.0,'Rajesh Gupta',48000,1.0,'2024-04-01',NULL,NULL),

('shanti_emp_10011','Deepak Mishra','1997-10-10',27,'M','Patna','Bihar','IT','Developer','Indore','On-site','Full-time','Day','2022-02-01',4,3.0,'Amit Sharma',78000,3.0,'2024-04-01','2023-02-01',NULL),

('shanti_emp_10012','Kavita Sharma','2000-12-12',24,'F','Delhi','Delhi','HR','Executive','Indore','Remote','Full-time','Day','2023-04-01',2,1.5,'Pooja Jain',42000,1.0,'2024-04-01',NULL,NULL),

('shanti_emp_10013','Arjun Singh','1996-06-06',28,'M','Kanpur','UP','Sales','Executive','Indore','On-site','Full-time','Day','2020-08-01',5,4.0,'Suresh Jain',52000,4.0,'2024-04-01','2022-08-01',NULL),

('shanti_emp_10014','Sneha Roy','2002-02-02',22,'F','Pune','MH','IT','Intern','Indore','Remote','Intern','Day','2024-02-01',1,0.5,'Amit Sharma',23000,0.5,'2024-04-01',NULL,NULL),

('shanti_emp_10015','Manish Yadav','1995-11-11',29,'M','Bhopal','MP','IT','Manager','Indore','Hybrid','Full-time','Night','2019-03-01',6,5.5,'Amit Sharma',92000,5.0,'2024-04-01','2021-03-01',NULL),

('shanti_emp_10016','Ritu Verma','2001-01-15',23,'F','Indore','MP','Finance','Analyst','Indore','On-site','Full-time','Day','2023-06-01',2,1.2,'Rajesh Gupta',61000,1.0,'2024-04-01',NULL,NULL),

('shanti_emp_10017','Sandeep Kumar','1993-08-08',31,'M','Delhi','Delhi','IT','Architect','Indore','On-site','Full-time','Day','2017-01-01',8,7.5,'Amit Sharma',12000,7.0,'2024-04-01','2019-01-01',NULL),

('shanti_emp_10018','Neha Gupta','1999-05-05',25,'F','Jaipur','RJ','HR','Executive','Indore','Hybrid','Full-time','Day','2022-09-01',3,2.0,'Pooja Jain',45000,2.0,'2024-04-01','2023-09-01',NULL),

('shanti_emp_10019','Rakesh Patel','1996-07-07',28,'M','Ahmedabad','GJ','Sales','Manager','Indore','On-site','Full-time','Day','2020-05-01',5,4.5,'Suresh Jain',88000,4.0,'2024-04-01','2022-05-01',NULL),

('shanti_emp_10020','Aditi Singh','2003-03-03',21,'F','Rewa','MP','IT','Intern','Indore','Remote','Intern','Day','2024-03-01',1,0.3,'Amit Sharma',22000,0.2,'2024-04-01',NULL,NULL);



-- 30 record insert
INSERT INTO employees VALUES
('shanti_emp_10021','Aakash Singh','1999-04-04',25,'M','Delhi','Delhi','IT','Developer','Indore','On-site','Full-time','Day','2023-06-01',3,2.0,'Rakesh Singh',85000,2.0,'2024-04-01',NULL,NULL),

('shanti_emp_10022','Riya Sharma','2001-07-07',23,'F','Indore','MP','HR','Executive','Indore','Hybrid','Full-time','Day','2024-01-01',2,1.0,'Pooja Jain',42000,1.0,'2024-04-01',NULL,NULL),

('shanti_emp_10023','Vivek Kumar','1998-02-02',26,'M','Patna','Bihar','IT','Tester','Indore','On-site','Full-time','Night','2022-03-01',4,3.0,'Amit Sharma',56000,3.0,'2024-04-01','2023-03-01',NULL),

('shanti_emp_10024','Sneha Verma','2002-05-05',22,'F','Bhopal','MP','Finance','Analyst','Indore','Remote','Full-time','Day','2024-02-01',2,0.8,'Rajesh Gupta',61000,1.0,'2024-04-01',NULL,NULL),

('shanti_emp_10025','Rahul Mishra','1996-09-09',28,'M','Lucknow','UP','Sales','Manager','Indore','On-site','Full-time','Day','2021-05-01',6,4.5,'Suresh Jain',92000,4.0,'2024-04-01','2022-05-01',NULL),

('shanti_emp_10026','Neha Gupta','2000-01-01',24,'F','Delhi','Delhi','IT','Intern','Indore','Remote','Intern','Day','2024-03-01',1,0.5,'Amit Sharma',25000,0.5,'2024-04-01',NULL,NULL),

('shanti_emp_10027','Manish Sharma','1997-08-08',27,'M','Jaipur','RJ','IT','DevOps','Indore','Hybrid','Full-time','Night','2021-07-01',5,3.5,'Amit Sharma',88000,3.0,'2024-04-01','2023-07-01',NULL),

('shanti_emp_10028','Anita Roy','1999-11-11',25,'F','Kolkata','WB','HR','Manager','Indore','On-site','Full-time','Day','2022-08-01',3,2.5,'Pooja Jain',72000,2.0,'2024-04-01','2023-08-01',NULL),

('shanti_emp_10029','Karan Patel','1995-03-03',29,'M','Ahmedabad','GJ','IT','Lead','Indore','On-site','Full-time','Day','2020-06-01',7,5.5,'Amit Sharma',95000,5.0,'2024-04-01','2022-06-01',NULL),

('shanti_emp_10030','Pooja Singh','2002-10-10',22,'F','Varanasi','UP','Finance','Executive','Indore','Hybrid','Full-time','Day','2024-01-01',2,0.9,'Rajesh Gupta',48000,1.0,'2024-04-01',NULL,NULL),

('shanti_emp_10031','Deepak Yadav','1997-12-12',27,'M','Patna','Bihar','IT','Developer','Indore','On-site','Full-time','Day','2022-02-01',4,3.0,'Amit Sharma',78000,3.0,'2024-04-01','2023-02-01',NULL),

('shanti_emp_10032','Kavita Singh','2000-06-06',24,'F','Delhi','Delhi','HR','Executive','Indore','Remote','Full-time','Day','2023-05-01',2,1.2,'Pooja Jain',43000,1.0,'2024-04-01',NULL,NULL),

('shanti_emp_10033','Arjun Verma','1996-04-04',28,'M','Kanpur','UP','Sales','Executive','Indore','On-site','Full-time','Day','2021-08-01',5,4.0,'Suresh Jain',52000,4.0,'2024-04-01','2023-08-01',NULL),

('shanti_emp_10034','Sneha Gupta','2001-09-09',23,'F','Pune','MH','IT','Intern','Indore','Remote','Intern','Day','2024-02-01',1,0.5,'Amit Sharma',23000,0.5,'2024-04-01',NULL,NULL),

('shanti_emp_10035','Manoj Kumar','1995-11-11',29,'M','Bhopal','MP','IT','Manager','Indore','Hybrid','Full-time','Night','2020-03-01',6,5.0,'Amit Sharma',91000,5.0,'2024-04-01','2022-03-01',NULL),

('shanti_emp_10036','Ritu Sharma','2001-01-01',23,'F','Indore','MP','Finance','Analyst','Indore','On-site','Full-time','Day','2023-06-01',2,1.0,'Rajesh Gupta',60000,1.0,'2024-04-01',NULL,NULL),

('shanti_emp_10037','Sanjay Gupta','1994-08-08',30,'M','Delhi','Delhi','IT','Architect','Indore','On-site','Full-time','Day','2018-01-01',8,6.5,'Amit Sharma',98000,6.0,'2024-04-01','2020-01-01',NULL),

('shanti_emp_10038','Neha Jain','1999-05-05',25,'F','Jaipur','RJ','HR','Executive','Indore','Hybrid','Full-time','Day','2022-09-01',3,2.0,'Pooja Jain',45000,2.0,'2024-04-01','2023-09-01',NULL),

('shanti_emp_10039','Rakesh Kumar','1996-07-07',28,'M','Ahmedabad','GJ','Sales','Manager','Indore','On-site','Full-time','Day','2020-05-01',5,4.5,'Suresh Jain',89000,4.0,'2024-04-01','2022-05-01',NULL),

('shanti_emp_10040','Aditi Sharma','2003-03-03',21,'F','Rewa','MP','IT','Intern','Indore','Remote','Intern','Day','2024-03-01',1,0.3,'Amit Sharma',22000,0.2,'2024-04-01',NULL,NULL),

('shanti_emp_10041','Vikas Singh','1998-06-06',26,'M','Delhi','Delhi','IT','Developer','Indore','On-site','Full-time','Day','2022-07-01',4,3.0,'Amit Sharma',80000,3.0,'2024-04-01','2023-07-01',NULL),

('shanti_emp_10042','Pooja Patel','2000-08-08',24,'F','Surat','GJ','Finance','Executive','Indore','Hybrid','Full-time','Day','2023-08-01',2,1.5,'Rajesh Gupta',50000,1.0,'2024-04-01',NULL,NULL),

('shanti_emp_10043','Rohit Sharma','1995-10-10',29,'M','Mumbai','MH','IT','Lead','Indore','On-site','Full-time','Day','2020-01-01',7,5.0,'Amit Sharma',95000,5.0,'2024-04-01','2022-01-01',NULL),

('shanti_emp_10044','Neha Singh','2001-11-11',23,'F','Patna','Bihar','HR','Executive','Indore','Remote','Full-time','Day','2023-04-01',2,1.2,'Pooja Jain',42000,1.0,'2024-04-01',NULL,NULL),

('shanti_emp_10045','Anil Yadav','1997-03-03',27,'M','Lucknow','UP','Sales','Executive','Indore','On-site','Full-time','Day','2021-05-01',5,3.5,'Suresh Jain',53000,3.0,'2024-04-01','2023-05-01',NULL),

('shanti_emp_10046','Kajal Verma','2002-09-09',22,'F','Delhi','Delhi','IT','Intern','Indore','Remote','Intern','Day','2024-02-01',1,0.4,'Amit Sharma',24000,0.3,'2024-04-01',NULL,NULL),

('shanti_emp_10047','Sunil Kumar','1996-12-12',28,'M','Kanpur','UP','IT','DevOps','Indore','Hybrid','Full-time','Night','2021-09-01',5,4.0,'Amit Sharma',87000,4.0,'2024-04-01','2023-09-01',NULL),

('shanti_emp_10048','Riya Gupta','2000-04-04',24,'F','Indore','MP','Finance','Analyst','Indore','On-site','Full-time','Day','2023-06-01',2,1.5,'Rajesh Gupta',61000,1.0,'2024-04-01',NULL,NULL),

('shanti_emp_10049','Ajay Sharma','1995-05-05',29,'M','Delhi','Delhi','IT','Manager','Indore','On-site','Full-time','Day','2019-07-01',6,5.0,'Amit Sharma',93000,5.0,'2024-04-01','2021-07-01',NULL),

('shanti_emp_10050','Ananya Singh','2003-01-01',21,'F','Bhopal','MP','IT','Intern','Indore','Remote','Intern','Day','2024-03-01',1,0.3,'Amit Sharma',21000,0.2,'2024-04-01',NULL,NULL);


-- 45 record insert
INSERT INTO employees VALUES
('shanti_emp_10051','Rahul Raj','1998-02-02',26,'M','Patna','Bihar','IT','Developer','Indore','On-site','Full-time','Day','2022-05-01',3,2.5,'Amit Sharma',78000,2.0,'2024-04-01',NULL,NULL),

('shanti_emp_10052','Sneha Kumari','2000-06-06',24,'F','Delhi','Delhi','HR','Executive','Indore','Hybrid','Full-time','Day','2023-01-01',2,1.2,'Pooja Jain',43000,1.0,'2024-04-01',NULL,NULL),

('shanti_emp_10053','Ankit Yadav','1997-09-09',27,'M','Lucknow','UP','IT','Tester','Indore','On-site','Full-time','Night','2021-04-01',4,3.0,'Amit Sharma',56000,3.0,'2024-04-01','2023-04-01',NULL),

('shanti_emp_10054','Riya Singh','2002-03-03',22,'F','Indore','MP','Finance','Analyst','Indore','Remote','Full-time','Day','2024-01-01',2,0.8,'Rajesh Gupta',60000,1.0,'2024-04-01',NULL,NULL),

('shanti_emp_10055','Deepak Kumar','1996-07-07',28,'M','Delhi','Delhi','Sales','Manager','Indore','On-site','Full-time','Day','2020-06-01',6,4.5,'Suresh Jain',92000,4.0,'2024-04-01','2022-06-01',NULL),

('shanti_emp_10056','Anjali Sharma','2001-10-10',23,'F','Bhopal','MP','IT','Intern','Indore','Remote','Intern','Day','2024-02-01',1,0.5,'Amit Sharma',24000,0.4,'2024-04-01',NULL,NULL),

('shanti_emp_10057','Vikas Patel','1995-05-05',29,'M','Ahmedabad','GJ','IT','DevOps','Indore','Hybrid','Full-time','Night','2020-03-01',5,4.0,'Amit Sharma',88000,4.0,'2024-04-01','2022-03-01',NULL),

('shanti_emp_10058','Pooja Verma','1999-11-11',25,'F','Jaipur','RJ','HR','Manager','Indore','On-site','Full-time','Day','2022-08-01',3,2.5,'Neha Jain',70000,2.0,'2024-04-01','2023-08-01',NULL),

('shanti_emp_10059','Rohit Mehta','1994-01-01',30,'M','Mumbai','MH','IT','Lead','Indore','On-site','Full-time','Day','2018-05-01',7,6.0,'Amit Sharma',95000,6.0,'2024-04-01','2020-05-01',NULL),

('shanti_emp_10060','Kajal Singh','2002-08-08',22,'F','Varanasi','UP','Finance','Executive','Indore','Hybrid','Full-time','Day','2024-01-01',2,0.9,'Rajesh Gupta',48000,1.0,'2024-04-01',NULL,NULL),

('shanti_emp_10061','Sandeep Yadav','1997-12-12',27,'M','Patna','Bihar','IT','Developer','Indore','On-site','Full-time','Day','2022-02-01',4,3.0,'Amit Sharma',79000,3.0,'2024-04-01','2023-02-01',NULL),

('shanti_emp_10062','Ritu Singh','2000-04-04',24,'F','Delhi','Delhi','HR','Executive','Indore','Remote','Full-time','Day','2023-05-01',2,1.2,'Pooja Jain',42000,1.0,'2024-04-01',NULL,NULL),

('shanti_emp_10063','Arjun Kumar','1996-06-06',28,'M','Kanpur','UP','Sales','Executive','Indore','On-site','Full-time','Day','2021-08-01',5,4.0,'Suresh Jain',53000,4.0,'2024-04-01','2023-08-01',NULL),

('shanti_emp_10064','Neha Roy','2001-09-09',23,'F','Pune','MH','IT','Intern','Indore','Remote','Intern','Day','2024-02-01',1,0.5,'Amit Sharma',23000,0.4,'2024-04-01',NULL,NULL),

('shanti_emp_10065','Manoj Singh','1995-11-11',29,'M','Bhopal','MP','IT','Manager','Indore','Hybrid','Full-time','Night','2020-03-01',6,5.0,'Amit Sharma',91000,5.0,'2024-04-01','2022-03-01',NULL),

('shanti_emp_10066','Aditi Verma','2001-01-01',23,'F','Indore','MP','Finance','Analyst','Indore','On-site','Full-time','Day','2023-06-01',2,1.0,'Rajesh Gupta',61000,1.0,'2024-04-01',NULL,NULL),

('shanti_emp_10067','Sanjay Kumar','1994-08-08',30,'M','Delhi','Delhi','IT','Architect','Indore','On-site','Full-time','Day','2018-01-01',8,6.5,'Amit Sharma',98000,6.0,'2024-04-01','2020-01-01',NULL),

('shanti_emp_10068','Neha Jain','1999-05-05',25,'F','Jaipur','RJ','HR','Executive','Indore','Hybrid','Full-time','Day','2022-09-01',3,2.0,'Pooja Jain',45000,2.0,'2024-04-01','2023-09-01',NULL),

('shanti_emp_10069','Rakesh Singh','1996-07-07',28,'M','Ahmedabad','GJ','Sales','Manager','Indore','On-site','Full-time','Day','2020-05-01',5,4.5,'Suresh Jain',89000,4.0,'2024-04-01','2022-05-01',NULL),

('shanti_emp_10070','Ananya Sharma','2003-03-03',21,'F','Rewa','MP','IT','Intern','Indore','Remote','Intern','Day','2024-03-01',1,0.3,'Amit Sharma',21000,0.2,'2024-04-01',NULL,NULL),

-- (remaining continue same pattern safely)


('shanti_emp_10071','Ravi Sharma','1998-01-01',26,'M','Delhi','Delhi','IT','Developer','Indore','On-site','Full-time','Day','2022-04-01',3,2.5,'Amit Sharma',78000,2.0,'2024-04-01',NULL,NULL),

('shanti_emp_10072','Priya Verma','2000-03-03',24,'F','Indore','MP','HR','Executive','Indore','Hybrid','Full-time','Day','2023-02-01',2,1.2,'Pooja Jain',42000,1.0,'2024-04-01',NULL,NULL),

('shanti_emp_10073','Ankit Kumar','1997-07-07',27,'M','Patna','Bihar','IT','Tester','Indore','On-site','Full-time','Night','2021-05-01',4,3.0,'Amit Sharma',56000,3.0,'2024-04-01','2023-05-01',NULL),

('shanti_emp_10074','Sneha Singh','2002-06-06',22,'F','Bhopal','MP','Finance','Analyst','Indore','Remote','Full-time','Day','2024-01-01',2,0.8,'Rajesh Gupta',60000,1.0,'2024-04-01',NULL,NULL),

('shanti_emp_10075','Rahul Gupta','1996-09-09',28,'M','Lucknow','UP','Sales','Manager','Indore','On-site','Full-time','Day','2020-07-01',6,4.5,'Suresh Jain',91000,4.0,'2024-04-01','2022-07-01',NULL),

('shanti_emp_10076','Kajal Sharma','2001-10-10',23,'F','Delhi','Delhi','IT','Intern','Indore','Remote','Intern','Day','2024-02-01',1,0.5,'Amit Sharma',24000,0.4,'2024-04-01',NULL,NULL),

('shanti_emp_10077','Manish Verma','1995-11-11',29,'M','Jaipur','RJ','IT','DevOps','Indore','Hybrid','Full-time','Night','2020-03-01',5,4.0,'Amit Sharma',88000,4.0,'2024-04-01','2022-03-01',NULL),

('shanti_emp_10078','Anita Kumari','1999-05-05',25,'F','Kolkata','WB','HR','Manager','Indore','On-site','Full-time','Day','2022-08-01',3,2.5,'Neha Jain',70000,2.0,'2024-04-01','2023-08-01',NULL),

('shanti_emp_10079','Rohit Singh','1994-02-02',30,'M','Mumbai','MH','IT','Lead','Indore','On-site','Full-time','Day','2018-05-01',7,6.0,'Amit Sharma',95000,6.0,'2024-04-01','2020-05-01',NULL),

('shanti_emp_10080','Pooja Patel','2002-08-08',22,'F','Varanasi','UP','Finance','Executive','Indore','Hybrid','Full-time','Day','2024-01-01',2,0.9,'Rajesh Gupta',48000,1.0,'2024-04-01',NULL,NULL),

('shanti_emp_10081','Deepak Singh','1997-12-12',27,'M','Patna','Bihar','IT','Developer','Indore','On-site','Full-time','Day','2022-02-01',4,3.0,'Amit Sharma',79000,3.0,'2024-04-01','2023-02-01',NULL),

('shanti_emp_10082','Ritu Sharma','2000-04-04',24,'F','Delhi','Delhi','HR','Executive','Indore','Remote','Full-time','Day','2023-05-01',2,1.2,'Pooja Jain',42000,1.0,'2024-04-01',NULL,NULL),

('shanti_emp_10083','Arjun Yadav','1996-06-06',28,'M','Kanpur','UP','Sales','Executive','Indore','On-site','Full-time','Day','2021-08-01',5,4.0,'Suresh Jain',53000,4.0,'2024-04-01','2023-08-01',NULL),

('shanti_emp_10084','Neha Roy','2001-09-09',23,'F','Pune','MH','IT','Intern','Indore','Remote','Intern','Day','2024-02-01',1,0.5,'Amit Sharma',23000,0.4,'2024-04-01',NULL,NULL),

('shanti_emp_10085','Manoj Kumar','1995-11-11',29,'M','Bhopal','MP','IT','Manager','Indore','Hybrid','Full-time','Night','2020-03-01',6,5.0,'Amit Sharma',91000,5.0,'2024-04-01','2022-03-01',NULL),

('shanti_emp_10086','Aditi Sharma','2001-01-01',23,'F','Indore','MP','Finance','Analyst','Indore','On-site','Full-time','Day','2023-06-01',2,1.0,'Rajesh Gupta',61000,1.0,'2024-04-01',NULL,NULL),

('shanti_emp_10087','Sanjay Singh','1994-08-08',30,'M','Delhi','Delhi','IT','Architect','Indore','On-site','Full-time','Day','2018-01-01',8,6.5,'Amit Sharma',98000,6.0,'2024-04-01','2020-01-01',NULL),

('shanti_emp_10088','Neha Jain','1999-05-05',25,'F','Jaipur','RJ','HR','Executive','Indore','Hybrid','Full-time','Day','2022-09-01',3,2.0,'Pooja Jain',45000,2.0,'2024-04-01','2023-09-01',NULL),

('shanti_emp_10089','Rakesh Patel','1996-07-07',28,'M','Ahmedabad','GJ','Sales','Manager','Indore','On-site','Full-time','Day','2020-05-01',5,4.5,'Suresh Jain',89000,4.0,'2024-04-01','2022-05-01',NULL),

('shanti_emp_10090','Ananya Singh','2003-03-03',21,'F','Rewa','MP','IT','Intern','Indore','Remote','Intern','Day','2024-03-01',1,0.3,'Amit Sharma',21000,0.2,'2024-04-01',NULL,NULL),

('shanti_emp_10091','Vikas Kumar','1998-06-06',26,'M','Delhi','Delhi','IT','Developer','Indore','On-site','Full-time','Day','2022-07-01',4,3.0,'Amit Sharma',80000,3.0,'2024-04-01','2023-07-01',NULL),

('shanti_emp_10092','Pooja Sharma','2000-08-08',24,'F','Surat','GJ','Finance','Executive','Indore','Hybrid','Full-time','Day','2023-08-01',2,1.5,'Rajesh Gupta',50000,1.0,'2024-04-01',NULL,NULL),

('shanti_emp_10093','Rohit Verma','1995-10-10',29,'M','Mumbai','MH','IT','Lead','Indore','On-site','Full-time','Day','2020-01-01',7,5.0,'Amit Sharma',95000,5.0,'2024-04-01','2022-01-01',NULL),

('shanti_emp_10094','Neha Singh','2001-11-11',23,'F','Patna','Bihar','HR','Executive','Indore','Remote','Full-time','Day','2023-04-01',2,1.2,'Pooja Jain',42000,1.0,'2024-04-01',NULL,NULL),


('shanti_emp_10095','Kunal Sharma','1997-07-07',27,'M','Delhi','Delhi','IT','Developer','Indore','On-site','Full-time','Day','2022-06-01',4,3.0,'Amit Sharma',80000,3.0,'2024-04-01','2023-06-01',NULL);




-- 5 record insert (ulfat)
INSERT INTO employees VALUES
('shanti_emp_10096','Shivam Kumar','2002-11-11',24,'M','Begusarai','Bihar','IT','Developer','Indore','On-site','Full-time','Day','2022-05-01',3,2.5,'Abhishek Gurjar',99000,2.0,'2024-04-01','2026-03-31',NULL),

('shanti_emp_10097','Pranaw Gautam','1999-09-24',26,'M','Satna','MP','IT','Executive','Indore','On-site','Full-time','Day','2023-01-01',2,1.2,'Abhishek Gurjar',99001,1.0,'2024-04-01',NULL,NULL),

('shanti_emp_10098','Yukti Singh','2003-06-13',23,'F','Riva','MP','IT','Tester','Indore','On-site','Full-time','Day','2021-04-01',4,3.0,'Abhishek Gurjar',99003,3.0,'2024-04-01','2023-04-01',NULL),

('shanti_emp_10099','Aditi Singh','2002-08-24',22,'F','Umariya','MP','IT','Analyst','Indore','On-site','Full-time','Day','2024-01-01',2,0.8,'Abhishek Gurjar',99004,1.0,'2024-04-01',NULL,NULL),

('shanti_emp_10100','Smrati Nigam','2004-05-30',21,'F','Chitrakut','MP','IT','Manager','Indore','On-site','Full-time','Day','2020-06-01',6,4.5,'Abhishek Gurjar',99005,4.0,'2024-04-01','2022-06-01',NULL);




select * from employees;





-- 🧠 100 SQL Practice Questions (Employees Dataset)
-- 🔰 BASIC (1–25)
-- Show all records from employees table
select * from employees;

-- Display only emp_id and full_name
select emp_id, full_name from employees;

-- Find employees from Delhi
select * from employees where city="Delhi";


-- Show employees with salary > 50000
select * from employees where salary > 5000;

update employees set salary = 4500 where emp_id = 'shanti_emp_10050';

select * from employees where salary < 5000;


-- List employees with age between 25 and 30
select * from employees where age between 25 and 30;



-- Find employees with NULL promotion_date
select * from employees where promotion_date = NULL;



-- Show employees working in IT department
select * from employees where department= 'IT';



-- Display employees with experience > 2 years
select full_name, experience from employees where experience > 2;



-- Get employees whose name starts with 'A'
select * from employees where full_name like "A%";


-- Find employees with salary < 40000
select full_name, salary from employees where salary < 40000;


-- Show distinct cities
select distinct(city) from employees;


-- Count total employees  
select count(*) as total_emp from employees;



-- Find maximum salary
select max(salary) from employees;



-- Find minimum salary
select min(salary) from employees;


-- Calculate average salary
select avg(salary) from employees;



-- Find total salary expense
select sum(salary) from employees;



-- Show employees ordered by salary DESC
select * from employees order by salary desc;



-- Show employees ordered by age ASC
select * from employees order by age;


-- Get top 5 highest paid employees
select * from employees order by salary desc limit 5;


-- get max salary paind employees
SELECT * FROM employees ORDER BY salary DESC LIMIT 1;


-- Get bottom 5 lowest paid employees
select * from employees order by salary limit 5;




-- Find employees hired after 2022
select * from employees where joining_date between '2022-01-01' and now();



-- Show employees with 'Manager' role
select * from employees where role='manager';


-- Display employees working in 'Remote' mode
select * from employees where working_mode='remote';




-- Count employees in each city
select city, count(*) from employees group by city;



-- Find employees with more than 3 projects
select * from employees where number_of_projects > 3;



-- ⚡ INTERMEDIATE (26–60)
-- Count employees in each department
select department, count(*) from employees group by department;


-- Find average salary per department
select department, avg(salary) from employees group by department;


-- Find max salary in each department
select department, max(salary) from employees group by department;


-- Find min salary in each department
select department, min(salary) from employees group by department;


-- Count employees by gender
select gender, count(*) from employees group by gender;



-- Find total salary by city
select city,sum(salary) from employees group by city;


--    --------------------- Find department with highest avg salary
select department, avg(salary) as avg_salary from employees group by department order by avg_salary desc limit 1;



-- Find employees earning above average salary
select * from employees where salary > (select avg(salary) from employees);




-- Find employees earning below average salary
select * from employees where salary < (select avg(salary) from employees);


-- Get employees with same salary
select *  from employees where salary in (select salary from employees group by salary having count(*) > 1);
select salary, count(salary) from employees group by salary having count(*) > 1;

-- Find duplicate names
select full_name, count(full_name) from employees group by full_name having count(*) > 1;

-- Show employees joined in last 2 years
select * from employees where joining_date >= curdate() - interval 2 year;


-- Find employees who never got promoted
select * from employees where promotion_date is null;

-- Find employees with NULL appraisal_date
select * from employees where appraisal_date is null;

-- Find employees with experience > complete_year
select * from employees where experience > complete_year;

-- Get employees with both promotion and appraisal done
select * from employees where promotion_date is not null and appraisal_date is not null;

-- Find employees working in hybrid mode
select * from employees where working_mode = 'hybrid';

-- Count interns
select emp_type, count(*) as intern from employees where emp_type= "intern";

-- Find employees with highest salary in each dept
select department, max(salary) from employees group by department;

-- Find employees with lowest salary in each dept
select department, min(salary) from employees group by department;

-- Get second highest salary  
select max(salary) from employees; -- max salry
select distinct(salary) from employees order by salary desc; -- sedc salary
select distinct(salary) from employees where salary < (select max(salary) from employees) order by salary desc;

-- Get third highest salary
select distinct(salary) from employees order by salary desc limit 1 offset 2;

-- Find employees with even age
select * from employees where age%2=0;

-- Find employees with odd age
select * from employees order by age desc limit 1;

-- Find employees whose name ends with 'a'
select * from employees where full_name like "%a";

-- Find employees with salary between 50k–80k
select * from employees where salary between 50000 and 80000;

-- Count employees per working mode
select working_mode, count(*) from employees group by working_mode; 

-- Find average experience per department
select department, avg(experience) from employees group by department;

-- Find total projects per department
select department, sum(number_of_projects) from employees group by department;

-- Find employees with more projects than avg
select * from employees where number_of_projects > (select avg(number_of_projects) from employees);

-- Get employees with max experience
select * from employees where experience = (select max(experience) from employees);

-- Get employees with min experience
select * from employees where experience = (select min(experience) from employees);

-- Find employees with salary same as manager
select * from employees where salary in (select salary from employees where role='manager');

-- Find employees hired in same year
select full_name, year(joining_date) as year from employees where year(joining_date) in ( select year(joining_date) from employees group by joining_date having count(*) > 1) order by year;

-- Get employees who joined in same month
select full_name, month(joining_date) as month from employees where month(joining_date) in ( select distinct(month(joining_date)) from employees group by joining_date having count(*) > 1) order by month;

-- select * from employees where full_name = "neha jain";


-- 🔥 ADVANCED (61–100)
-- Find top 3 salaries in each department
select department from employees group by department;

-- Rank employees based on salary
select full_name, dense_rank() over (order by salary desc) as rnk from employees;

-- Dense rank employees by experience
select full_name, dense_rank() over (order by experience desc) as rnk from employees;

-- Find employees with salary higher than dept avg
-- Find employees with max salary in each city
-- Find employees with min salary in each city
-- Calculate running total of salary
-- Find gap between employee salary and avg salary
-- Find employees with no projects
-- Find employees with highest projects
-- Get cumulative experience
-- Find employees whose salary increased (simulate)
-- Find employees with longest tenure
-- Find employees with shortest tenure
-- Calculate years between joining_date and today
-- Find employees older than dept avg age
-- Find employees younger than dept avg age
-- Find employees whose salary > all in dept
-- Find employees whose salary < all in dept
-- Find employees with same manager
-- Count employees under each manager
-- Find manager with most employees
-- Find manager with least employees
-- Find employees with same role and salary
-- Find employees with unique salary
-- Get employees with max salary per role
-- Get employees with min salary per role
-- Find employees promoted in last year
-- Find employees not appraised in last year
-- Find employees who left company
-- Find employees still active
-- Find employees with both remote & onsite history (assume)
-- Find employees working in more than 1 dept (assume)
-- Find employees with gap in promotion dates
-- Find employees whose salary is prime (logic)
-- Find employees with duplicate DOB
-- Find employees hired on weekends
-- Find employees with salary difference > 20k from avg
-- Find employees with longest name
-- Find employees with shortest name





