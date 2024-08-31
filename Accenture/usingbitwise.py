
a=8991
# print("odd" if a&1==1 else "even" )


# arr=[10,20,30,40,50,60]
# arr.reverse()
# print(sum(arr[::2]))




#input=5   0101
#output=10 1010  toggled

# i=80
# print(bin(80))
# print(bin(95))
# print(i^15)



# from math import log2
# n=int(input())
# k=int(log2(n))+1
# res=n^((1<<k)-1)
# print(res)


n=35
print(bin(n))
x=list(bin(n)[2:])
x.sort()
j="".join(i for i in x)
print(int(j,2)) 


