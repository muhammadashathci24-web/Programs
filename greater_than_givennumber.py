n = int(input())
arr= list(map(int,input().split()))


for value in arr:
    if value > n:
        print(value,end=" ")