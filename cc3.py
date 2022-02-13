n,k=input().split()
n=int(n)
k=int(k)
count=0
for i in range(n):
    ask=int(input())
    if ask%k==0:
        count=count+1
print(count)
