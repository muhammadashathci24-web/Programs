n= abs(int(input()))
digit=0

smallest=10

while n>0:
    digit = n % 10
    if digit < smallest:
        smallest = digit
    n = n // 10
    
print(smallest)