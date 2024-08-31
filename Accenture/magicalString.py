def isMagic(n):
    s=bin(n)[2:].replace("1","2")
    s=s.replace('0','1')
    summ=sum(list(int(i) for i in s))
    return True if summ%2!=0 else False

n=5
# n=4
n=7
for i in range(1,n+1):
    if isMagic(i):
        print(i)
