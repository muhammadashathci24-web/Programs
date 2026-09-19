arr= list(map(int,input().split()))
pos_count=0
neg_count=0

for value in arr:
    if value ==0:
        pass
    elif value > 0:
        pos_count+=1
    else:
        neg_count+=1
        
print("Positive elements: ",pos_count,"negative count: ",neg_count)
