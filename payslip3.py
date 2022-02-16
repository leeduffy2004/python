Salary=int(input("Enter your Salary:"))

if Salary>=1000:
    if Salary>=2000:
        Tax=Salary*25/100
    else:
        Tax=Salary*15/100
else:
    Tax =0   
    
Net=Salary-Tax

print("Tax:", Tax)
print("Net Salary:",Net)