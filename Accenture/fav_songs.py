s="abcacahjsaaaa"
k=3
a="a"
maxx=0
for i in range(len(s)-k+1):
    c=(s[i:i+k].count(a))
    maxx=max(c,maxx)
print(maxx)

