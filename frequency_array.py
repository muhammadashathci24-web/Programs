arr = list(map(int,input().split()))
count=[0] * (max(arr)+1)

for value in arr:
    count[value]+=1
    
for i in range(0,len(count)):
    if count[i]!=0:
        print(i," : ",count[i])