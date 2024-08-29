# s="apples"
# f="a"
# t="p"
s="coders"
f="c"
t="r"
for i in s:
    if i==f:
        s=s.replace(i,t.upper())
        continue
    elif i==t:
        s=s.replace(i,f.upper())
        continue

print(s.lower())
