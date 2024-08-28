s1="abd"
s2="aabccad"
s1='xyz'
s2='abc'
s=''
for i in s1:
    if i in s2 and i not in s:
        s+=i
print(len(s2)-len(s))