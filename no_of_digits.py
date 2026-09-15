n = int(input())
count=0

while n%10 ==0:
    n=n//10
    count=count+1
else:
    while(n!=0):
        n=n//10
        count=count+1
        

print(count)