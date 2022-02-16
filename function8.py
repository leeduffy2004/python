def Tax(Salary):
    T=Salary*20/100
    return T

Salary=int(input("Enter your Salary:"))
NetSalary=Salary-Tax(Salary)

print("Tax:", Tax(Salary))  
print("Net Salary:",NetSalary)

