num =[1,2,3,4,5,6,7,2,4,5,5]
k=11
def fun(l,r):
    while l<r:
        num[l],num[r]=num[r],num[l]
        l+=1
        r-=1
        
fun(0,len(num)-1)
fun(0,k-1)
fun(k,len(num)-1)
print(num)
