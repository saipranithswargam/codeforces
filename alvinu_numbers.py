import math
m,n=map(int,input().split())
rem1m=math.floor((m-4)/5)+1
rem2m=math.floor((m-3)/5)+1
rem3m=math.floor((m-2)/5)+1
rem4m=math.floor((m-1)/5)+1
rem1n=math.floor((n-4)/5)+1
rem2n=math.floor((n-3)/5)+1
rem3n=math.floor((n-2)/5)+1
rem4n=math.floor((n-1)/5)+1
c1=rem1m*rem4n
c2=rem2m*rem3n
c3=rem3m*rem2n
c4=rem4m*rem1n
c5=int(m/5)*int(n/5)
print(c1+c2+c3+c4+c5)

