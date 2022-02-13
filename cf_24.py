num,times=input().split()
num=[int(i) for i in num]
times=int(times)

for i in range(times):
    if num[-1]==0:
        num.remove(num[-1])
    else:
        num[-1]=num[-1]-1
num="".join(str(i) for i in num)
print(num)
