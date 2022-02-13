strin=input()
li=[str(i)  for i in strin]
dist=set(li)
length=len(dist)
if length%2==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")