arr=[3,2,11,7,6,3,6,4]
res=[]
for i in range(len(arr)):
    flag=0
    for j in range(i,len(arr)):
        if arr[i]>arr[j]:
            res.append(arr[j])
            break
    else:
        res.append(-1)
print(*res)

