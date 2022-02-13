
n=int(input())
li=["a","b","c","d","e"]
while (n>1):
    li.append(li[0])
    li.append(li[0])
    li.remove(li[0])

    n=n-1
if li[0]=="a":
    print("Sheldon")
elif li[0]=="b":
    print("Leonard")
elif li[0]=="c":
    print("Penny") 
elif li[0]=="d":
    print("Rajesh")
elif li[0]=="e":
    print("Howard")




    
    
