test=int(input())
for i in range(test):
    z,y,a,b,c=input().split()
    z=int(z)
    y=int(y)
    a=int(a)
    b=int(b)
    c=int(c)
    if z-y-a-b-c>=0:
        print("YES")
    else:
        print("NO")
