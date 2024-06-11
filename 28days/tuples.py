# # tpl=(11,22,33,44,55)
# # for i in tpl:
# #     print(i,end=" ")

# # tpl=(11,22,33,44,55)
# # index=0
# # while index<len(tpl):
# #     print(tpl[index],end=' ')
# #     index+=1

# tpl=(11,22,33,44,55)
# for i in range(len(tpl)):
#     print(tpl[i],end=' ')

# #immutable

# k=11,22,33,44,55
# print(k)
# print(k[0])
# k[0]=90

# s=([1,2,3,4],[11,22],'python')
# s[0][0]=10
# del(s[0][2])
# print(s[0][0])
# print(s)

# (x,y)=(10,20)
# print(x)

# #unpacking
# k=11,22,33,44,55
# print(k)
# s=1,2,3,k,6,7
# print(s)
# s=(1,2,3,*k,6,7)
# print(s)

# *k,v=11,22,33
# print(k)
# print(v)
# k,*v=11,22,19
# print(k)
# print(v)
# v[0]=33
# print(v[0])

# *k,v,r=11,22,33,44,55
# print(k,v,r)
# print(len(k))
# print(min(k))
# print(max(k))
# print(sum(k))
# print(any(k))
# a=reversed(*k)
# print(a)

# print(dir(tuple))

# ply=["Kohli","Rohit"]
# jry=[18,45]
# tm=list(zip(ply,jry))
# print(tuple(tm))
# print(list(tm))
# print(tm[0])

# lst=[1,2,3,4,5]
# dtpl=tuple(i ** 2 for i in lst)
# print(dtpl)
# print(type(dtpl))

# lst=[-12,84,11,22,-3,0,-24]
# pstv_tpl=tuple(i for i in lst if i > 0)
# print(pstv_tpl)

# tpl=()
# n=int(input("Enter no.of elements in tuple :"))
# for i in range(n):
#     ele=int(input())
#     tpl=tpl+(ele,)
#     print(id(tpl))#every time it creates new tuple
# print(tpl)

