s="abc"
cnt=0
for i in s.lower():
    if i not in "aeiou":
        cnt+=1
tot=1
for i in range(1,cnt+1):
    tot=tot*i
print(tot)