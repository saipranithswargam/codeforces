x,y,z=input().split()
x=int(x)
y=int(y)
z=int(z)
net=abs(x-y)
if net>z:
    if x>y:
        print("+")
    elif x<y:
        print("-")
elif x==y and z==0:
    print(0)

else:
    print("?")
