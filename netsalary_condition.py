#to find the netsalary after the deduction of income tax based on the condition of gross salary



emp_id=1001
basic_salary=15000
allowances=6000
monthly_gross_salary=basic_salary+allowances
if(monthly_gross_salary<=5000):
	income_tax=0
	net_salary=monthly_gross_salary
elif(monthly_gross_salary>=5001 and monthly_gross_salary<=10000):
	income_tax=(monthly_gross_salary/100)*10
	net_salary=monthly_gross_salary-income_tax
elif(monthly_gross_salary>=10000 and monthly_gross_salary<=20000):
	income_tax=(monthly_gross_salary/100)*20
	net_salary=monthly_gross_salary-income_tax
else:
	income_tax=(monthly_gross_salary/100)*30
	net_salary=monthly_gross_salary-income_tax
print("EMPLOYEE ID:",emp_id)
print("BASIC SALARY:",basic_salary)
print("ALLOWANCES:",allowances)
print("MONTHLY GROSS SALARY",monthly_gross_salary)
print("INCOME TAX:",income_tax)
print("NET SALARY:",net_salary)
		
