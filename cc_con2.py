test=int(input())
for i in range(test):
    n=int(input())
    s=input()
    code=s.index("code")#indexing of code by text
    chef=s.index("chef")
    if code<chef:
        print("AC")
    elif code>chef:
        print("WA")
        