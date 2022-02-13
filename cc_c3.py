test=int(input())
for i in range(test):
    side,x,y=input().split()
    side=int(side)
    x=int(x)
    y=int(y)
    # mid=(side+1)/2
    # if x==mid-1 and y==mid:
    #     print(1)
    # elif x==mid and y==mid-1:
    #     print(1)
    # elif x==mid and y==mid+1:
    #     print(1)
    # elif x==mid+1 and y==mid:
    #     print(1)
    # else:
    #     print(0)
    if x%2!=0:
        if y%2==0:
            print(1)
        else:
            print(0)
    elif x%2==0:
        if y%2!=0:
            print(1)
        else:
            print(0)
