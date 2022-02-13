k=int(input())
l=int(input())
i=1
s=k
while(l>=k):
    k=pow(s,i)
    if k==l:
        print("YES")
        print(i-1)
        break
    else:
        i=i+1
else:
    print("NO")