salaries=[500,600,700,800,900,1000,1,2,3,4,5,6,7,8,9,1200,1300,1500,16000,1000]

i=0
total=0

while i<len(salaries):
    total=total+salaries[i]
    i=i+1
print(total)
print(total/len(salaries))

print("---------------------")
