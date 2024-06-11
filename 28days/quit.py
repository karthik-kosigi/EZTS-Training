
# # s=input('')
# # while s.upper()!= "QUIT" :
# #     print(len(s))
# #     s=input()
# # else:
# #     print("Exiting the programming....")


# s=''
# count=1
# while count<=5 :
#     s=input()
#     if len(s)<6 :
#         print("Enter again: ")
#     else:
#         print(f"{count}:{s}")
#         count+=1


s=input()
s=s[len(s):-1:-1]
print(s)
