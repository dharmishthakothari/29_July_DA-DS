-- use sql_da_ds
/* create table student(student_id int,
					student_name varchar(20),
					age int,
					mobile_num int,
                    address varchar(200))
                    */
-- alter table student add semster_no int

-- drop table student
 
 -- 14th Oct

-- use sql_da_ds

 /* create table student (student_id int , student_name varchar(20), 
                                        age int,mobile_no int,address varchar(200))
    */                                    
-- describe student

-- alter table student add c_no int not null

-- alter table student drop c_no
   
-- create table student_table(roll_no int primary key auto_increment , 
-- 							student_name varchar(50) not null,
-- 							email varchar(50),
--                             age int check(age>15),
--                             address varchar(100),
--                             contact_no int unique key,
--                             city varchar(50) default "Ahmedabad")

-- create table deparment(dept_id int primary key,
-- 						dept_name varchar(20))

-- create table employee(emp_id int primary key ,
-- 					emp_name varchar(20) ,
--                     c_no int not null,
--                     salary decimal(6,2),
--                     dept_id int,
--                     foreign key (dept_id) references deparment(dept_id))

-- insert into student_table(student_name,email,age,address,contact_no) values("Prexa","pre@gmail.com",20,"Parimal",2345788)                            

select * from student_table

-- insert into student_table(student_name,email,age,address,contact_no,city) values("Khushali","khu@gmail.com",22,"vadaj",546544,'Baroda')                            

insert into student_table(student_name,email,age,address,contact_no,city) 
	values
    ("mmmmmm","mm@gmai.com",30,"Navarangpura",88888,"Surat")
    -- ("Dhruvi" ,"dh@gmail.com",21,"Narayanpura",34234,"Ahmedabad")
    