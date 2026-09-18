n= abs(int(input()))
total=0 
actual=n

while n!=0:
    digit= n%10
    total = total + digit
    n//=10

if actual % total == 0:
    print("Harshad number")
else:
    print("not a Harshad number")