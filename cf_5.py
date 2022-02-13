test=int(input())
X=0
for i in range(test):
    ask=input()
    if ask=="++X":
        X=X+1
    elif ask=="X++":
        X=X+1
    elif ask=="--X":
        X=X-1
    elif ask=="X--":
        X=X-1
print(X)

