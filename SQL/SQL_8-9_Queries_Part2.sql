
DELIMITER $$
create function get_full_name(emp_name varchar(20),emp_surname varchar(20))
returns varchar(50)
DETERMINISTIC
begin
	return concat(emp_name,' * ',emp_surname);
end$$
    
    
-- 2nd Dec

DELIMITER $$
create function getTotalDeptSalary(did int)
returns int
READS SQL DATA
begin
	declare total_salary int;
    select sum(salary) into total_salary from employee_master where dept_id=did;
    return total_salary;
end$$

-- Third 

DELIMITER $$
create function calculateSalaryWithDA(salary1 int,DA decimal(4,2))
returns decimal(10,2)
deterministic 
begin
	declare total_salary decimal(10,2);
    set total_salary=salary1+(salary1*DA);
    return total_salary;
end$$

drop function calculateSalaryWithDA;

select salary as base_salary,calculateSalaryWithDA(salary,0.2) as net_salary_with2,
calculateSalaryWithDA(salary,0.5) as net_salary_with5 from employee_master;

DELIMITER $$
create procedure GetEmployeesByDepartment(dept_name varchar(20))
begin
	select ename,city,salary,dname from employee_master,department
    where employee_master.dept_id=department.dept_id 
    and dname=dept_name;
end$$


call GetEmployeesByDepartment('Finance')
