num=int(input())
fac=[]
# num1=int(num)
# li=set(num)
# li=list(li)
# if num1%7==0 or num1%4==0:
#     print("YES")
#     li=list(li)
# elif len(li)==2:
#     if ((li[0]=="4") and (li[1]=="7")):
#         print("YES")
#     elif ((li[0]=="7") and(li[1]=="4")):
#         print("YES")
#     else:
#         print("NO")
# else:
#     print("NO")
res=[]
for i in range(1,num+1):
    if num%i==0:
        fac.append(i)
l=[str(i) for i in fac]
for i in l:
    s=set(i)
    l=list(s)
    if len(s)==2:
        if ((l[0]=="4") and (l[1]=="7")):
             res.append(1)
        elif ((l[0]=="7") and(l[1]=="4")):
            res.append(1)
if 4 in fac:
    res.append(1)
if 7 in fac:
    res.append(1)
if len(res)>0:
    print("YES")
else:
    print("NO")

    


    