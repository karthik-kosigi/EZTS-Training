t=[73,74,75,71,69,72,76,73]
res=[]
for i in range(len(t)):
    for j in range(i+1,len(t)):
        if t[j]>t[i]:
            res.append(j-i)
            break
    else:
        res.append(0)
print(res)






# i=0
# j=1
# flag=0
# while i<=len(t) and j<len(t):
#     if t[i]<t[j]:
#         res.append(j-i)
#         i+=1
#         j=i+1
#         flag=1
#     else:
#         j+=1
# print(res)
