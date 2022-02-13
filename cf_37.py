num_c=int(input())
val=input().split()
Sum=0
l=[int(i) for i in val]
l.sort(reverse = True)
for i in range(len(val)):
    Sum=l[i]+Sum
    Sum2=sum(l[(i+1):])
    if(Sum>Sum2):
        print(i+1)
        break
    elif(num_c==1):
        print(1)