def isGprime(n):
    if n==1 or n==2:
        return "yes"
    if n%2==0:
        return "no"
    for i in range(3,int(n**0.5)):
        if n%i==0:
            return "no"
    return 'yes'
num=123
summ=sum(list(int(i) for i in str(num)))
print(isGprime(summ))