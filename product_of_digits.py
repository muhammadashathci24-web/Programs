n= int(input())
sum=1
num=0


while n!=0:
    num=n%10
    if num!=0:
        sum=sum * num
    n=n//10
    
print(sum) 