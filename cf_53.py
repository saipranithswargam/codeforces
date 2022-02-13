test=int(input())
def yes(l1,l2,l3):
    if l1==l2:
        if l3%2==0:
            return True
        else:
            False
    elif l2==l3:
        if l1%2==0:
            return True
        else:
            False
    elif l3==l1:
        if l2%2==0:
            return True
        else:
            return False
for i in range(test):
    l=input().split()
    l=[int(i) for i in l]
    v=[int(i) for i in l]
    s=max(l)
    l.remove(s)
    if yes(v[0],v[1],v[2]):
        print("YES")
    elif s==l[0]+l[1]:
        print("YES")
    else:
        print("NO")
    
            