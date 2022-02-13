test=int(input())
for i in range(test):
    a,b,c,d=input().split()
    a=int(a)
    b=int(b)
    c=int(c)
    d=int(d)

    if a>=b:
        b=b+c
        if a>=b:
            b=b+d
            if a>=b:
                print("N")
            elif a<b:
                print("S")
        elif b>a:
            a=a+d
            if a>=b:
                print("N")
            elif a<b:
                print("S")
    elif b>a:
        a=a+c
        if a>=b:
            b=b+d
            if a>=b:
                print("N")
            elif a<b:
                print("S")
        elif b>a:
            a=a+d
            if a>=b:
                print("N")
            elif a<b:
                print("S")

    
