arr = list(map(int,input().split()))
total=0
n= len(arr)

for value in arr:
    total+=value
   
avg= total / n 

print(avg)   