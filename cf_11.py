test=int(input())
for i in range(test):
    len_seq=int(input())
    seq=input().split()
    lis=[int(i) for i in seq ]
    for i in lis:
        if (i>=(lis.index(i)+1)):
            lis.insert(lis.index(i),lis.index(i))
    print(len(lis)-len_seq-1)



    
     