# import re
# s="12axy44"
# res=0
# arr=re.findall("[0-9]+",s)
# for i in arr:
#     res+=int(i)
# print(res)


s="12ax4y44"
res=0
arr=[]
temp=0
for i in s:    
    if i.isdigit():
        temp=temp*10+int(i)
    else:
        arr.append(temp)
        temp=0
if temp>0:
    arr.append(temp) 
print(sum(arr))
       
    