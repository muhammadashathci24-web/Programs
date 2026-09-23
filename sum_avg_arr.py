nums = list(map(int,input().split()))

sums=0

for value in nums:
    sums = sums + value
    
avg = sums/ len(nums)

print(sums)
print(avg)