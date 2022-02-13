stops=int(input())
matrix=[]
maxi=[]
for i in range(stops):
    inn=input().split()
    li=[int(i)for i in inn]
    matrix.append(li)
maxi.append(matrix[0][1])
for i in range(stops-1):
    # max1=matrix[0][1]+matrix[1][1]-matrix[1][0]
    maxx2=maxi[i]+matrix[i+1][1]-matrix[i+1][0]
    maxi.append(maxx2)
print(max(maxi))


