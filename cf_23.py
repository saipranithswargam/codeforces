string=input()
li=[str(i) for i in string]
upper=0
lower=0
for i in li:
    if i.islower():
        lower=lower+1
    elif i.isupper():
        upper=upper+1
if upper>lower:
    print(string.upper())
elif upper<lower or upper==lower:
    print(string.lower())


