s1=input().strip()
s2=input().strip()
l=[str(i) for i in s1 ]
l=l[::-1]
s3="".join([str(i) for i in l])
if s2==s3:
    print("YES")
else:
    print("NO")
