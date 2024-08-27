s="321"
summ=0

# for i in range(1,len(s)+1):
#     summ+=int(s[:i])
# for i in range(1,len(s)+1):
#     summ+=int(s[i-1:])
# for i in s[1:-1]:
#     summ+=int(i)
# print(summ-int(s))

for i in range(len(s)):
    for j in range(i,len(s)):
        summ+=int(s[i:j+1])
print(summ)