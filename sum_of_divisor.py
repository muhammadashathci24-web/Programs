n = abs(int(input()))
sum =0

arr=[]
if n==0:
    arr.append(0)
else:
    for i in range (1,n+1):
        if n % i == 0:
            sum + 1
        
print(sum)