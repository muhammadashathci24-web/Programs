nums= list(map(int,input().split()))

index=0
for val in nums:
    if val!=0:
        nums[index]=val
        index+=1
for i in range(index,len(nums)):
    nums[i]=0
    
print(nums)