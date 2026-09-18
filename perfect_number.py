n = abs(int(input()))
total =0

if n==0:
    total=-1
else:
    for i in range (1,n):
        if n % i == 0:
            total+= i
if n == total:
    print(n,"is a Perfect number")
else:
    print(n,"is a not a Perfect number")