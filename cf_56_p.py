n=int(input())
l=input().split()
l=[int(i) for i in l]
res=[]
count=1
for i in range(1,len(l)):
    if l[i-1]<=l[i]:
        count+=1
    elif l[i-1]>l[i]:
        res.append(count)
        count=1
res.append(count)
print(max(res))



    