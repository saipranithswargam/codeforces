test=int(input())
num=input().split()
num=[str(i) for i in num]
li=[]
for i in range(1,test+1):
    li.append(i)
for i in num:
    pri=(num.index(i))+1
    ind=int(i)-1
    li.pop(ind)
    # li.remove(rem)
    li.insert(ind,pri)
print(*li)


