m = int(input("Enter number"))
count=1
if m<=1:
    print("invalid")
    exit(0)
for i in range(2,int(m**0.5)+1,2):
    if m%i==0:
        count+=1

if count<2:
    print("valid message")
else:
    print("not valid")