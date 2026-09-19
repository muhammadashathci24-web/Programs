def fact(n):
    if  n==0 or n==1:
        return 1
    else:
        return n* fact(n-1)

n= abs(int(input()))
total =0
actual = n
while n!=0:
    digit = n%10
    total = total + fact(digit)
    n//=10
    
if actual == total:
    print("Strong Number")
else:
    print("not a Strong Number")