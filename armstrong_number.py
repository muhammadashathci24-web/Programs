n= abs(int(input()))

x=n
actual= n
cube =0
count=0

while x!=0:
    x//=10
    count+=1

while n!=0:
    digit = n%10
    cube = cube + digit ** count
    n//=10
    
if actual == cube:
    print(cube ," is an armstrong number.")
else:
    print(cube ," is not an armstrong number.")
    