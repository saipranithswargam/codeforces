a,b=input().split()
a=int(a)
b=int(b)
count=0
while True:
    if a<=b:
        a=a*3
        b=b*3
        count=count+1
    else:
        break
print(count)
    
