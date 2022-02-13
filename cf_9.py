string=input().lower()
fir=string.replace("a","")
sec=fir.replace("e","")
thr=sec.replace("i","")
fou=thr.replace("o","")
six=fou.replace("y","")
fiv=six.replace("u","")
li=[str(i) for i in fiv]
for i in range(len(li)):
    li[i]="."+li[i]
updatedstr="".join([str(i) for i in li])
print(updatedstr)





    
