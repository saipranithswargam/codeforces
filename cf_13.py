string=input()
li=[str(i) for i in string]
li[0]=li[0].capitalize()
new="".join([str(i) for i in li])
print(new)
