s1=input()
s2=input()
l=[]
for i in range(len(s1)):
    if s1[i]==s2[i]:
        l.append("0")
    else:
        l.append("1")
s3="".join([str(i) for i in l])
print(s3)