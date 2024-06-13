n = 13  
arr = [-1,-1,-1,-1,1,1,1,1,1,1,-1,-1,-1]
count=0
summ=0
for i in range(0,n):
    summ +=arr[i]
    if summ==0:
        count+=1
print(count)