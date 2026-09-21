arr = list(map(int,input().split()))
count=0
for i in range(0,len(arr)):
    if arr[i]==0:
        for j in range(i,count,-1):
            arr[j]=arr[j-1]
        arr[count]=0
        count+=1
        
print(arr)
        


