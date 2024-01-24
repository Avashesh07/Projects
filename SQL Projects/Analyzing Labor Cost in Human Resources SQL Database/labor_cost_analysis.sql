--Exploring Relevant Tables--

SELECT * FROM departments
LIMIT 10;

SELECT * FROM dept_emp
LIMIT 10;

SELECT * FROM salaries
LIMIT 10;


--Retrieve Current Salaries and Create View--

CREATE VIEW current_salaries AS
SELECT emp_no, salary
FROM salaries
WHERE to_date > CURDATE();


--Implement Employee Department View--

CREATE VIEW current_dept_emp AS
SELECT emp_no, dept_no
FROM dept_emp
WHERE to_date > CURDATE();

--Writing Query for Accumulated Salaries by Department--

SELECT departments.dept_name, departments.dept_no,sum(current_salaries.salary) AS total_salary
FROM current_salaries
INNER JOIN current_dept_emp
ON current_salaries.emp_no = current_dept_emp.emp_no
INNER JOIN departments
ON current_dept_emp.dept_no = departments.dept_no
GROUP BY current_dept_emp.dept_no, departments.dept_name;
