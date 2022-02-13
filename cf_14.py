st=int(input())
stones=input()
li=[str(i) for i in stones]
count=0
for i in range(1,st):
    if li[i-1]==li[i]:
        count=count+1
if count==st:
    print(count-1)
else:
    print(count)
