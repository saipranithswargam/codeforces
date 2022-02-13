test=int(input())
for i in range(test):
    le=int(input())
    li=input().split()
    li2=[int(k) for k in li]
    a=min(li2)
    b=max(li2)
    c=li2.index(a)
    d=li2.index(b)
    e=int(le/2)
    if (c>e) and (d>e):
        if c>d:
            print((le-d))
        elif c<d:
            print((le-c))
    elif (c<e) and (d<e):
        if c>d:
            print(c+1)
        elif d>e:
            print(d+1)


    

    
    
