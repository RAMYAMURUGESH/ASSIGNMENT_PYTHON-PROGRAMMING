#to find the netsalary after the deduction of income tax


emp_id=1001
basic_salary=15000
allowances=6000
monthly_gross_salary=basic_salary+allowances
if monthly_gross_salary>=10000:
	income_tax=(monthly_gross_salary/100)*20
	net_salary=monthly_gross_salary-income_tax
else:
	income_tax=0
	net_salary=monthly_gross_salary
print("EMPLOYEE ID:",emp_id)
print("BASIC SALARY:",basic_salary)
print("ALLOWANCES:",allowances)
print("MONTHLY GROSS SALARY",monthly_gross_salary)
print("INCOME TAX:",income_tax)
print("NET SALARY:",net_salary)
		
