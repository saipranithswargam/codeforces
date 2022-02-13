stri=input()
li=[int(i) for i in stri]
y=[]
n=[]
if len(li)>=7:
    for i in range((len(li)-6)):
        li2=li[i:i+7]
        se=set(li2)
        i=i+1
        if len(se)==2:
            n.append(1)
        else:
            y.append(1)
    if len(y)>=1:
        print("YES")
    else:
        print("NO")
else:
    print("NO")

        

