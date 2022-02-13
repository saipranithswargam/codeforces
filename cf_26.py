n,t=input().split()
n=int(n)
t=int(t)
string=input()
li=[str(i) for i in string]
while t>0:
    for i in range(len(li)-1):
        print(i)
        if  li[i]=="B":
             if li[i+1]=="G":
                li[i]="G"
                li[i+1]="B"
                i=i+1            
    t=t-1
print(li)