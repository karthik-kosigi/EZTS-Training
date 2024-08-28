no=17
# st=0
# for i in range(no**2,-1,-1):
#     if no-(2**i)>=0:
#         no=no-(2**i)
#         st+=1
# print(st)
print((bin(no)).count("1"))

