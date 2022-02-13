n=int(input())
s1="I hate that"
s2="I love that"
s3="I hate it"
s4="I love it"
for i in range(1,n+1):
    if i%2!=0:
        if n-i==0:
            print(s3,end=" ")
        else:
            print(s1,end=" ")
    else:
        if n-i==0:
            print(s4,end=" ")
        else:
            print(s2,end=" ")
