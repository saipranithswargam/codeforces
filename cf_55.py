import math
n=int(input())
l=input().split()
l=[int(i) for i in l]
fo=l.count(4)
th=l.count(3)
to=l.count(2)
on=l.count(1)
tax=fo+th+int(to/2)
if th>=on:
    if to%2==0:
        print(tax)
    elif to%2!=0:
        print(tax+1)
elif th<on:
    on=on-th
    if to%2==0:
        if on%4==0:
            print(tax+int(on/4))
        elif on%4!=0:
            print(tax+int(on/4)+1)
    elif to%2!=0:
        on=on-2
        tax+=1
        if on%4==0:
            print(tax+int(on/4))
        elif on%4!=0:
            print(tax+int(on/4+1))


8