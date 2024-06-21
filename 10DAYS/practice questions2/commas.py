# str="1000"
# sum=0
# if len(str)>6:
#     sum+=int(str)-999999
# if len(str)>3:
#     sum+=int(str)-999

# print(sum)
sum=0
n=12456789
i=0
m=1
rem=n%1000
while(n!=0):
    r=n%1000
    sum=sum+(r*i*m*1000)
    i+=1
    n=n//1000
    m=m*1000
print(sum+rem)

