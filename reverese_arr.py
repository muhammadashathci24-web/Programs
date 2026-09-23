nums= list(map(int,input().split()))

left =0
right = len(nums)-1

while left < right:
    nums[left],nums[right] = nums[right],nums[left]
    left+=1
    right-=1
    
print(nums)