# lst=[9,3,2,2,1,0]
# n=6
# res=[]
# # for i in range(n):
# #     res.append(lst[0])
# #     if sum(res) > sum(lst)-lst[0]:
# #         break
# #     else:
# #         lst.pop(0)

# while(sum(res)<=sum(lst)-lst[0]):
#     res.append(lst[0])
#     lst.pop(0)

# print(sum(res))


# n=6
# numbers=[1,3,3,4,3,3,3,4,4]
# new=[]
# count=0
# for i in numbers:
#     if i not in new:
#         new.append(i)
#     else:
#         count+=1
# print(count)



# s="abdc"
# j=1
# c=0
# while j<len(s):
#     if ord(s[c])<ord(s[j]):
#         c=j
#     j+=1
# print(s[c:])

# s="abdce"
# h=0
# for i in range(len(s)):
#     if ord(s[h])<ord(s[i]):
#         h=i
# print(s[h:])



# n=6
# play=[3,4,-8,-3,4,9]
# sum,a,=0,0
# for i in play:
#     sum+=i
#     if sum<1:
#         a+=(-1*sum)
#         sum=0
# print(a) 

