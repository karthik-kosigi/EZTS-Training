# print(ord("a"))
# print(chr(97))

s="abcdzyxd"
en=""
for i in s:
    en+=en.join(chr(122-ord(i.lower())+97))
print(en)
