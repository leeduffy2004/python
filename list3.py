nums=[24,3,75,7]

i=1
Big=nums[0]

while i<len(nums):
    if nums[i]>Big:
        Big=nums[i]
    i=i+1

print("Highest number is:", Big)