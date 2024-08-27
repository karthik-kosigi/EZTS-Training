s1="ABCLKSJK"
s2="DEFG"
res=""
i=0
while i<len(s1) and i<len(s2):
    res+=s1[i]
    res+=s2[i]
    i+=1
res+=s1[i:]
res+=s2[i:]

print(res)