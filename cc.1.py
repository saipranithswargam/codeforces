a,b=input().split()#we cannot us the strings with commas here..wee need to take just single letters
a=float(a)
b=float(b)
if (a%5==0 or a%5==1) and b+0.5>=a:
    rem=b-a-0.50
    format_float = "{:.2f}".format(rem)
    print(format_float)
else:
    format_float2="{:.2f}".format(b)#this is for makin the output to have two decimals
    print(format_float2)