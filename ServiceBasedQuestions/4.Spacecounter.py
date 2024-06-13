s="Hello world hi"
# print(s.count(" "))
count=0
for i in s:
    if i == " ":
        count+=1
print(count)