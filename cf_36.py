year=(input())
y=int(year)
for i in range(y,9012):
    y=y+1
    y=str(y)
    li=[str(i) for i in y]
    l=set(li)
    if len(l)==4:
        print(y)
        break
    y=int(y)

