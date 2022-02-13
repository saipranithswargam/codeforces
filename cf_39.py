rooms=int(input())
count=0
for i in range(rooms):
    p,q=input().split()
    p=int(p)
    q=int(q)
    if q-p>=2:
        count=count+1
print(count)

        