test=int(input())
for i in range(test):
    n,m=input().split()
    m=int(m)
    n=int(n)
    s=input()
    l=[str(i) for i in s]
    for i in range(m):
        for i in range(l):
            if (((l[i]=="0") and (l[i+1]=="1")) or ((l[i]=="0") and (l[i-1]=="0"))):
                if ((l[i+1]=="0") and (l[i-1]=="1")):
                    pass
                else:
                    l[i]="1"
    print(l)

