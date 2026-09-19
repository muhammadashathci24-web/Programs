arr = list(map(int,input().split()))
even_count=0
odd_count=0

for value in arr:
    if value % 2==0:
        even_count+=1
    else:
        odd_count+=1
        
print("Even:",even_count,"odd:",odd_count)
