n,h=input().split()
n=int(n)
h=int(h)
Sum=[]
l=input().split()
for i in range(len(l)):
    hi=int(l[i])
    if hi>h:
        Sum.append(2)
    else:
        Sum.append(1)
print(sum(Sum))

        