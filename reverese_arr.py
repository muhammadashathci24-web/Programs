nums= list(map(int,input().split()))
rev_nums=list()
j=0
for i in range(len(nums)-1,0,-1):
    rev_nums[j] = nums[i]
    j+=1
    
print(rev_nums)
