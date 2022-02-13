test=int(input())
re=0
for i in range(test):
    n,x=input().split()
    x=int(x)
    n=int(n)
    val=input().split()
    val=[str(i) for i in val]
    val.sort(reverse=True)
    r1=[int(i) for i in val]
    r1=sum(r1)
    if x>r1:
        print(-1)
    for i in range(len(val)):
        re=int(val[i])+re
        if re>=x:
            print(i+1)
            re=0
            break
    
    

