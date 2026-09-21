arr = list(map(int,input().split()))

unique= set()

for value in arr:
    if value not in unique:
        unique.add(value)
        
print(unique)