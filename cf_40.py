string=input()
l=["H","Q","9"]
num=[]
for i in string:
    if i in l:
        num.append(1)
if len(num)>=1:
    print("YES")
else:
    print("NO")