def fib(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
s=input("Enter a string:")
sum=0
for i in s.lower():
    val=fib(ord(i)-96)
    sum+=val
print(sum)