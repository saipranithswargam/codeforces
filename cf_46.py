n,k=input().split()
n=int(n)
k=int(k)
if n%2==0:
    if k<=(n/2):
        print(int(2*k-1))
    else:
        k=k-(n/2)
        print(int(2*k))
else:
    if k<=(n+1)/2:
        print(int(2*k-1))
    else:
        k=k-((n+1)/2)
        print(int(2*k))
