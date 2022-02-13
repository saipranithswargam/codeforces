matrix=[]#empty list
for i in range(5):#runs 5 times
    ask=input().split()#1 2 3 4 5=[1,2,3,4,5]as string
    li=[int(i) for i in ask]#string is modified into int
    matrix.append(li)#lists are addedd to matrix
row1=matrix[0]#[1,2,3,4,5]
row2=matrix[1]#1 0 0 0 0   
row3=matrix[2]#0 0 0 0 0      
row4=matrix[3]#0 0 * 0 0
row5=matrix[4]#0 0 0 0 0
if (1 in row1):#0 0 0 0 0
    if (row1.index(1)==0) or (row1.index(1)==4):
        print(4)
    elif (row1.index(1)==1) or (row1.index(1))==3:
        print(3)
    elif (row1.index(1)==2):
        print(2)
if (1 in row2):
    if (row2.index(1)==0) or (row2.index(1)==4):
        print(3)
    elif (row2.index(1)==1) or (row2.index(1)==3):
        print(2)
    elif (row1.index(1)==2):
        print(1)
if (1 in row3):
    if (row3.index(1)==0) or (row3.index(1)==4):
        print(2)
    elif (row3.index(1)==1) or (row3.index(1)==3):
        print(1)
    elif (row3.index(1)==2):
        print(0)

if (1 in row4):
    if (row4.index(1)==0) or (row4.index(1)==4):
        print(3)
    elif (row4.index(1)==1) or (row4.index(1)==3):
        print(2)
    elif (row4.index(1)==2):
        print(1)

if (1 in row5):
    if row5.index(1)==0 or row5.index(1)==4:
        print(4)
    elif row5.index(1)==1 or row5.index(1)==3:
        print(3)
    elif row5.index(1)==2:
        print(2)

    