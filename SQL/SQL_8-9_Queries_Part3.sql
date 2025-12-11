-- Trigger
create table employee1(eid int,date_of_insertion date)

delimiter $$
create trigger emp_insert_record 
after insert
on employee_master 
FOR each row
begin
	insert into employee1 values(new.eid,curdate());
end$$

select * from employee1

insert into employee_master(ename,city,salary,email,dept_id)
values("Rohit","JamNagar",9090,"rohit@gmail.com",5) ;

create table employee_backup(emp_id int,emp_name varchar(20),dept_id int,date_of_delete datetime)

delimiter $$
create trigger emp_backup_record 
before delete
on employee_master 
FOR each row
begin
	-- insert into employee_backup values(old.eid,old.ename,old.dept_id,now());
    insert into employee_backup values(23,'tewet',23,now());
end$$


select * from employee_backup

delete from employee_master where eid=32