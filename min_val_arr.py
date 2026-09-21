arr = list(map(int,input().split()))

min_val= arr[0]

for val in arr:
    if val < min_val:
        min_val = val
        
print(min_val)