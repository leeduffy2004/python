nums=[]
print("Enter 0 to Stop")
while True:
    num=int(input("Enter any Number:"))
    if num==0:
        break
    nums.append(num)

print("You have entered:",len(nums),"numbers")