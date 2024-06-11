# d={'k':'11','z':'22','k':'14'}
# print(d['k'])
# d.clear()
# print(d)

# ply={'p1': {'nm':'Rohit','jrsy':45},
#      'p2': {'nm':'Kohli','jrsy':18}}
# for n,j in ply.items():
#     print(n,j)

# kys=['k','v','s']
# vls=1122
# dct=dict.fromkeys(kys,vls)
# print(dct)

# kys=['k','v','s']
# vls=1122
# dct=dict.fromkeys(kys)
# print(dct)

# d={'k':11,'v':22,'s':19}
# print(d.get('k',-1))
# print(d.get('y',-1))
# print(d.get('b'))
# print(d['b'])

# d={'k':11,'v':22,'s':19}
# for i in d.items():
#     print(i,end=' ')

# d={'k':11,'v':22,'s':19}
# for i in d.items():
#     print(*i,end=' ')

# d={'k':11,'v':22,'s':19}
# for i,(j,k) in enumerate(d):
#     print(i,j,k)

# d1={'k':11,'v':22,'s':19}
# d2={'b':2,'s':19,'a':1}
# print(d1,d2)
# d1.update(d2)
# print(d1,d2)

##setdefault()
# d={'k':11,'v':22,'s':19}
# print(d.setdefault('k',25))
# print(d.setdefault('y',25))
# print(d.setdefault('y'))

# d={}
# while True:
#     c=input("Enter character:")
#     if c!='0':
#         k=int(input("Enter ascii: "))
#         d[c]=k
#     else:
#         break
# print(d)

d={}
name=input("Enter String: ")
for i in name.lower():
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)
max_key = max(d,key=d.get)
print(max_key)

# d={}
# for i in range(3):
#     un=input("Enter user name : ")
#     pw=int(input("Enter password: "))
#     d[un]=pw
# print(d)
# un=input("Enter user name: ")
# if un in d:
#     pw=int(input("Enter password: "))
#     if d[un]==pw:
#         print("Match found")
#     else:
#         print("Match not found")
# else:
#     print("User not found")