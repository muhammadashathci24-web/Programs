arr = list(map(int,input().split()))

max_val= arr[0]

for val in arr:
    if val > max_val:
        max_val = val
        
print(max_val)