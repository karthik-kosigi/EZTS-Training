n=7
arr=[5,6,4,5,2,3,4]
cnt=0
for i in range(1,n):
    if arr[i-1]>arr[i]:
        cnt+=1
print(cnt)
