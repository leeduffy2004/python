Salary=int(input("Enter your Salary:"))
if Salary>=2000:
    Tax=Salary*20/100

if Salary<2000:
    Tax=Salary*10/100
    
Net=Salary-Tax

print("Tax:", Tax)
print("Net Salary:",Net)

