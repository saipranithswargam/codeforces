n=int(input())
num=input().split()
num=[int(i) for i in num]
count_odd=[]
count_even=[]
for i in num:
    if i%2==0:
        count_even.append(i)
    else:
        count_odd.append(i)
if len(count_odd)==1:
    print(num.index(count_odd[0])+1)
else:
    print(num.index(count_even[0])+1)
    

