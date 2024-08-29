n=6
# cnt=0
arr=[8,10,6,2,9,7]
# for j in range(n):
#     for i in range(j+1,n):
#         if arr[j]<arr[i]:
#             break
#     else:
#         cnt+=1
# print(cnt)
cnt=1
sup=arr[-1]
for j in range(n-1,0,-1):
    if arr[j]>sup:
        cnt+=1
        sup=arr[j]
print(cnt)