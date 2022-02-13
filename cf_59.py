test=int(input())
for i in range(test):
    num=int(input())
    l=input().split()
    l=[str(i) for i in l]
    q=set(l)
    r1=list(q)
    r1.sort()
    count=0
    for i in range(1,len(r1)):
        if (int(r1[i-1])+1)==int(r1[i]):
            count=count+1
    if len(r1)-1==count:
        if len(r1)<len(l):
            print(int(max(r1))+1)
        elif len(r1)==len(l):
            print(len(r1))






