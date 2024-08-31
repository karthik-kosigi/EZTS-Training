# n=4
# c=1
# for i in range(1,n+1):
#     for j in range(i):
#         print(c,end=" ")
#         c+=1
#     print()
    

# c=65
# for i in range(1,n+1):
#     for j in range(i):
#         print(chr(c),end=" ")
#         c+=1
#     print()




n=3
for i in range(n,0,-1):
    for j in range(n,0,-1):
        c=i
        while c>0:
            print(j,end="")
            c-=1
    print()
