test=int(input())
num=52
count=0
for i in range(test):
    k=int(input())
    for i in range(num):
        if num%k!=0:
            count+=1
            num=num-1
        elif num%k==0:
            print(count)
            count=0
            break
    
