n= int(input())
reverse=0
num=0

if n<0 or (n%10 ==0 and n!=0):
    print("It is not a palindrome")
else:

    original = n

    while n!=0:
        num=n%10
        reverse= reverse*10 + num
        n=n//10
    
    if reverse == original:
        print("The number is palindrome")
    else:
        print("The number is not a palindrome")
    
