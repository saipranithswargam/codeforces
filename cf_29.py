number=input()
li=[str(i) for i in number]
x=li.count("4")
y=li.count("7")
if ("4" in li) or ("7" in li):
    if x+y==7:
        print("YES")
    elif x+y==4:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
