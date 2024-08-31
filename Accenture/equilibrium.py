def equ(n,a):
    for i in range(n):
        if sum(a[:i])==sum(a[i+1:]):
            return i
    return -1
n=7
a=[-7,1,5,2,-4,3,0]
# a=[1,2,3]
print(equ(n,a))