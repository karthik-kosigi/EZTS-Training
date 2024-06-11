# # # print("hello worldṇ")
# # # s=input()
# # # r,t="ing","ly"
# # # if len(s) > 3 and s.endswith(r):
# # #     print(s[:-3]+t)
# # # else:
# # #     print(s if len(s) <= 3 else s + r)

# # s=input()
# # s=s.split()
# # print(s[0])
# # count=len(s[0])
# # for i in range(len(s)):
# #     if len(s[i]>len(s[i+1])):
# #         count=len(s[i])
# # print(count)

# # swap first and last letter
# str=input()
# if len(str)>=2:
#     ns =str[-1]+ str[1:-1]+str[0]
#     print("Modified string :",ns)
# else:
#     print("string is too short.")


# # remove odd index values
# s=input()
# ns= s[::2]
# print("Modified string :",ns)

# s=input('')
# while s.upper()!= "QUIT" :
#     print(len(s))
#     s=input()
# import datetime
# # date=datetime.date.today()
# # date1=datetime.date.today()
# # end_date=date + datetime.timedelta(days=28)
# # print(date)
# # print(end_date)
# date="N.A"
# date1="N.A"
# if date==date1:
#     print("Equal")

# st=input()
# length=len(st)
# print(length)


x=1
y=20
flag=False
for i in range(x,y+1):
    if i%2==0:
        print(i,end=" ")
        flag=True
if flag==False:
    print("NA")


n=5
for i in range(n):
    if i==0 or i==1:
        print(i,end=" ")
    else:
        print()