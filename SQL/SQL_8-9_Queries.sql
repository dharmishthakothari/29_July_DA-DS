create database first_db
use first_db
create table student(id int,
name varchar(20),
email varchar(20),
c_no decimal(10))


create table employee(eid decimal primary key ,
ename varchar(50) not null ,
contact_no decimal(10) ,
age decimal check(age>18),
city varchar(20) default 'Ahmedabad')

alter table employee add salary decimal(10,2) 

describe employee

insert into employee(eid,ename,contact_no,age)
value(105,'dhruv',89078,21);

insert into employee(eid,ename,contact_no,age)
value(106,'Daksh',8899,21);

insert into employee(eid,ename,contact_no,age)
value(107,'Manish',9999,21);

insert into employee(eid,ename,contact_no,age)
value(108,'Shrreyans',7777,21);

select * from employee

drop table employee

-- 18th Nov
create table department(dept_id decimal primary key ,dname varchar(50))

create table employee_master(eid int primary key auto_increment,
ename varchar(20) ,
city varchar(20),
salary decimal(7,2),
email varchar(20) ,
dept_id decimal ,
foreign key (dept_id) references department(dept_id))

describe employee_master

insert into department values(3,"Production") ,
(4,"HR"),
(5,"IT"),
(6,"Networking")

select * from department

insert into employee_master(ename,city,salary,email,dept_id)
values("jil","Ahemdabad",1234,"dhar@gmail.com",null) ,
("Dhruv","Jamnagar",3968,"s@gmail.com",null),
("Nikunj","Surat",9023,"pre@gmail.com",null)


select * from employee_master

select * from department 
-- 20th Nov
-- Display employee name and city from employee table
select ename,city from employee_master

-- Display employee name as employee name and city as City of employee  from employee table
select ename as employee_name,city as 'City of Employee' from employee_master

-- Fetch only those details of employee who got more then 20000 salary
select * from employee_master where salary>20000

-- Fetch only those details of employee who got more then 20000 salary and lives in Ahmedababd
select * from employee_master where salary>20000  and city="Ahemdabad"

-- Fetch only those details of employee who got more then 20000 salary or lives in Ahmedababd
select * from employee_master where salary>20000  or city="Ahemdabad"

-- Fetch employee name and email who got salary in between 20000 to 30000
select ename,email,salary from employee_master where salary between 10000 and 50000

-- Fetch records whose city is null
select * from employee_master where city is NULL

-- Fetch employee details who are lives in surat and baroda
select * from employee_master where city in ('Surat','Baroda','Rajkot')

-- fetch employee name and email who got 12300 and 15000.25 salary
select ename,email from employee_master where salary in (12300,15000.25)

-- Display the details of employees whose name starts with d
select * from employee_master where ename like 'd%'

-- Display the details of employees whose name ends with a
select * from employee_master where ename like '%a'

-- Display the details of employees whose name starts with d , ends with a
select * from employee_master where ename like 'd%a'

-- Display the details of employee whose name have 5 character long
select * from employee_master where ename like '_____'

-- Dsiplay the details of employee whose name have second letter as a and lenth is of 6 character
select * from employee_master where ename like '_a____'

-- Display details of employees whose name contains last second letter 'h'
select * from employee_master where ename like '%h_'

-- 22nd Nov

-- Display the records ascentiding to city 
select * from employee_master order by city,ename

-- Dsiplay the recored decending wise ename 
select * from employee_master order by ename desc

-- Display employee details with departname 

select employee_master.dept_id,ename,city,email,dname from employee_master,department  
where department.dept_id=employee_master.dept_id


-- Dsiplay maximum salary from employee master
select max(salary) from employee_master 

-- Display Average and maxium of salary 
select avg(salary) as 'Average salary',max(salary) as 'maximum salary' from employee_master

-- Display how many employees 
select count(*) from employee_master

-- Left Join 
select ename,email,salary,employee_master.dept_id from employee_master left join department on
employee_master.dept_id=department.dept_id

-- right join
select ename,email,salary,employee_master.dept_id from employee_master right join department on
employee_master.dept_id=department.dept_id

-- Display sum of salary in each department 

select dname,sum(salary) from employee_master, department where department.dept_id=employee_master.dept_id
group by employee_master.dept_id

-- Find max salary in each department
select dname,max(salary) from employee_master, department where department.dept_id=employee_master.dept_id
group by employee_master.dept_id

-- 25th Nov
-- find max salary in each department having more then 25000
select dname,max(salary) from employee_master, department where department.dept_id=employee_master.dept_id
group by employee_master.dept_id having max(salary)>25000 order by dname

-- find total of employees in each depatment , 
select dname,count(*) from employee_master,department where department.dept_id=employee_master.dept_id
group by department.dept_id 


-- fetch recoreds whose department have more then 2 employees 
select dname,count(*) from employee_master,department where department.dept_id=employee_master.dept_id
group by department.dept_id having count(*)>=2

select * from employee_master limit 2

-- find max salary of each department 

select dname,max(salary) from employee_master,department where department.dept_id=employee_master.dept_id
group by department.dept_id order by dname limit 2

-- sub 
select ename,salary from employee_master where salary > (select avg(salary) from employee_master) order by ename

update employee_master set salary=12000 where eid= 15

delete from employee_master where eid=15