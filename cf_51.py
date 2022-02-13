n=int(input())
Sum=input().split()
Sum=[int(i) for i in Sum]
Sum=sum(Sum)
den=100*n
r=Sum/den
s=r*100
print('%.12f'%s)#is used in python for setting precision
print(1/4)
