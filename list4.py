nums=[]
choice="Y"

while choice=="Y":
    num=int(input("Enter any Number:"))
    nums.append(num)
    choice=input("Do you want to add another number - Y/N:")

print("You have entered:",len(nums),"numbers")