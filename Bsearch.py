arr = [1,2,3,4,5,6,7]
s=6
l=0
r=len(arr)-1

while l<=r:
    mid=(l+r)//2
    
    if arr[mid]==s:
        print(mid)
        break
    elif arr[mid]<s:
        l=mid +1
    else:
        r=mid-1
else:
    print("not found")

    