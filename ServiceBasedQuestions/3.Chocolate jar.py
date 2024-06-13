# jars = [10,20,30]
# n=3
# A=0
# for i in jars:
#     cho = i//n if i%n==0 else (i//n)+1
#     A+=cho
# print(A)



# for B
jars = [10,20,30]
n=3
B=0
for i in jars:
    if i%n==2:
        cho=i//n+1
    else:
        cho = i//n
    B+=cho
print(B)