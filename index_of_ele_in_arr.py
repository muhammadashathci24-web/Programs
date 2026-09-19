n= int(input())
arr= list(map(int,input().split()))

for i in range(0,len(arr)-1):
    if n == arr[i]:
        print("Index ",i)
        break
else:
    print(-1)
    