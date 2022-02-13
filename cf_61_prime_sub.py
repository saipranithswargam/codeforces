test=int(input())
for i in range(test):
    x,y=map(int,input().split())
    diff=x-y
    if diff==1:
        print("NO")
    else:
        print("YES")