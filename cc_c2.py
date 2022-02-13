test=int(input())
for i in range(test):
    row,seat=input().split()
    row=int(row)
    seat=int(seat)
    if row%2==0 and seat%2==0:
        maxir=row/2
        maxis=seat/2
        print(int(maxir*maxis))
    elif row%2==0 and seat%2!=0:
        maxis=(seat+1)/2
        maxir=row/2
        print(int(maxis*maxir))
    elif row%2!=0 and seat%2==0:
        maxis=seat/2
        maxir=(row+1)/2
        print(int(maxis*maxir))
    elif row%2!=0 and seat%2!=0:
        maxir=(row+1)/2
        maxis=(seat+1)/2
        print(int(maxis*maxir))

    