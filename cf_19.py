test=int(input())
x=[]
y=[]
z=[]
for i in range(test):
    main=input().split()
    updated=[int(i) for i in main]
    x.append(updated[0])
    y.append(updated[1])
    z.append(updated[2])
if sum(x)==sum(y)==sum(z)==0:
    print("YES")
else:
    print("NO")
     