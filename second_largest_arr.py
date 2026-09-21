nums= list(map(int,input().split()))

max_num= nums[0]
smax_num=nums[1]

for i in range(2,len(nums)):
    if nums[i]>max_num:
        smax_num = max_num
        max_num = nums[i]
        
print(smax_num)