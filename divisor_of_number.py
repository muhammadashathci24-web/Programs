
n = int(input())
actual = n
arr=[]
if n==0:
    arr.append(0)
else:
    for i in range (1,n+1):
        if n % i == 0:
            arr.append(i)
        
print(arr)