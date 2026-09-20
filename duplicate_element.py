arr = list(map(int,input().split()))
x= set()
c=0
for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]==arr[j]:
            x.add(arr[i])
            c+=1
            break
    
print(x)  

arr.remove(x)

print(arr)