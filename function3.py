def SalarySlip(name,salary):
    if salary>=2000:
        Tax=salary*20/100
    else:
        Tax=salary*15/100
    netsalary=salary-Tax

    print("Name of Employee is", name)
    print("Salary",salary)
    print("Tax",Tax)
    print("Net Salary",netsalary)

SalarySlip("Lee",3000)
SalarySlip("David",5000)