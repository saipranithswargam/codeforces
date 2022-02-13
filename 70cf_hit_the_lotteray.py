import math
n=int(input())
count=0
while(n!=0):
    if n-100>=0:
        count+=math.floor(n/100)
        n=n%100
    elif n-20>=0:
        count+=math.floor(n/20)
        n=n%20
    elif n-10>=0:
        count+=math.floor(n/10)
        n=n%10
    elif n-5>=0:
        count+=math.floor(n/5)
        n=n%5
    else:
        count+=n
        n=0
print(count)