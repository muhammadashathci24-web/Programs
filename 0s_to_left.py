nums = list(map(int,input().split()))
    
x =0

for i in range(0,len(nums)):
    if nums[i]==0:
        nums[x], nums[i] = nums[i], nums[x]
        x+=1
        
print(nums)