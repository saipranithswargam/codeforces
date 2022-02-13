x=int(input())
steps=0
while x>0:
    if x>=5:
        steps=steps+1
        x=x-5
    elif x>=4:
        steps=steps+1
        x=x-4
    elif x>=3:
        steps=steps+1
        x=x-3
    elif x>=2:
        steps=steps+1
        x=x-2
    elif x==1:
        steps=steps+1
        x=x-1
    else:
        break
print(steps)