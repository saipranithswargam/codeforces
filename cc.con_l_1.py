test=int(input())
for i in range(test):
    dm=input().split()
    sm=input().split()
    if sum([int(i) for i in dm])>sum([int(i) for i in sm]):
        print("DRAGON")
    elif sum([int(i) for i in dm])<sum([int(i) for i in sm]):
        print("SLOTH")
    else:
        if int(dm[0])>int(sm[0]):
            print("DRAGON")
        elif int(dm[0])<int(sm[0]):
              print("SLOTH")
        else:
            if  int(dm[1])>int(sm[1]):
                print("DRAGON")
            elif  int(dm[1])<int(sm[1]):
                print("SLOTH")
            else:
                print("TIE")



