string=input()
string=[str(i) for i in string]
new=string[string.index("h"):(string.index("o")+1)]
print(new)
for i in new :
    if i not in "helo":
        new.remove(i)
for i in new :
    if i not in "helo":
        new.remove(i)


print(new)
up_se=sorted(set(new),key=string.index)
print(up_se)

if string.index("l")<string.index("o") and string.index("l")> string.index("e"):
    if string.count("l")>2:
        out=True
l="".join([str(i) for i in up_se])
if l=="helo" and out:
    print("YES")
else:
    print("NO")
