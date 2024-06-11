# ls1=[11,22,'k',"k","kv",65.75,True,False]
# print(ls1)

#concatenation (+)
# lst=[10,20,30]
# lst1=['a','b','c']
# lst2=lst+lst1
# print(lst2)

#repetition(*)

# lst=[10,20,30]
# lst1=lst*2
# print(lst1)

#nested lists
# lst=[11,22,33,[44,55,66],77,88]
# print(lst)
# print(lst[3])


# #append() method
# lst=[11,22,33,[44,55,66],77,88]
# lst.append(99)
# print(lst)

# #count()
# k=[1,2,3,4,1,21,5,1,1,33,]
# print(k.count(1))
# print(k.count(20))

# # insert()
# k=[1,2,3,4,1,21,5,1,1,33]
# k.insert(20,'kart')
# print(k)

# #pop()
# k=[1, 2, 'kart', 3, 4, 1, 21, 5, 1, 1, 33]
# k.pop()
# print(k)
# k.pop(3)
# print(k)

# ##sort()
# v=[1,2,3,4,1,21,5,1,1,33]
# print(v)
# v.sort()
# print(v)

# ##extend()
# k=[11,22,33]
# v=[44,55,66]
# k.extend(v)
# print(k)
# v.extend(k)
# print(v)

# #remove()
# k=[11,22,33]
# k.remove(33)
# print(k)
# k.remove(44)
# print(k)

# #reverse()
# k=[11,22,33]
# k.reverse()
# print(k)

# print(dir(list))

# #looping in lists
# lst=[11,22,33,44,55]
# for i in lst:
#     print(i,end=' ')

# #list comprehensions

# lst=[1,2,3,4,5]
# dbl_lst=[i**2 for i in lst]
# print(dbl_lst)

# lst=[-12,84,11,22,-3,0,-25]
# pst_lst=[i for i in lst if i>0]
# print(pst_lst)

# lst=[1,2,3,4,5,6,7]
# odd_lst=[i for i in lst if i%2!=0]
# print(odd_lst)

# n=int(input("Enter no of elements: "))
# lst=[]
# for i in range(n):
#     lst.append(int(input(f"Enter element {i+1} :")))
# print(lst)



# lst=[]
# s=input("Enter element :")
# while s!='quit':
#     lst.append(s)
#     s=input("Enter element :")
# print(lst)

# l=[1,2,3,4,5]
# ch=input("")
# n=int(input("Enter no of places to shift :"))
# for i in range(n):
#     a=l.pop()
#     l.insert(0,a)
# print(l)

# l=[1,2,3,4,5]
# n=int(input("Enter no of places to shift :"))
# l=l[-n:]+l[:-n]
# print(l)
# l=l[n:]+l[:n]
# print(l)


# l=[1,2,3,4,3,1,2,1,4,5,6,7]
# nl=[]
# for i in l:
#     if i not in nl:
#         nl.append(i)
# print(nl)

# l=[1,-2,3,-4,-3,1,2,1,-4,5,6,7]
# pt= [i for i in l if i>0]
# print(pt)