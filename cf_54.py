
n=int(input())
l=input().split()
l=[int(i) for i in l]
fo=l.count(4)
th=l.count(3)
to=l.count(2)
on=l.count(1)
tax=fo+th
if on>th:
    if to%2!=0:
        on=on-2
        tax+=1
        if on/4==0:
            tax+=int(on/4)
        else:
            tax+=int(on/4)+1

    else:
        if on%4==0:
            tax+=int(on/4) 
        else:
            tax+=int(on/4)+1
elif to%2!=0:
    tax+=1
print(tax)