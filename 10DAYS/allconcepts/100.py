# # calulate the sum of digits of a number where each digit is powers to no of digits..
# num=1634
# length = 0
# temp=num
# while(temp>0):
#     length+=1
#     temp=temp//10

# sum=0
# while(num>0):
#     rem=num%10
#     sum += rem**length
#     num=num//10
# print(sum)



# # ****
# # *  *
# # *  *
# # ****
# n=4
# for i in range(n):
#     for j in range(n):
#         if i==0 or j==0 or j==n-1 or i==n-1 :
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()





# descerium number
#175 = 1**1 + 7**2 + 5**3
# num1 = 175
# cnt=0
# length = 0
# temp=num1
# while(temp>0):
#     length+=1
#     temp=temp//10

# sum=0
# while(num1>0):
#     rem=num1%10
#     sum += rem**length
#     length-=1
#     num1=num1//10
# print(sum)




# odd and b,d,f,h == true
# alp = "bdfh"
# coordinates="g3"
# if coordinates[0] in alp and int(coordinates[1])%2!=0:
#     print("True")
# elif int(coordinates[1])%2==0:
#     print("True")
# else:
#     print("False")





# no_of_prisoners=6
# no_of_chocolates = 12
# starting_point = 3

# last = (no_of_chocolates + starting_point-1) % no_of_prisoners
# if last==0:
#     print(no_of_prisoners)
# else:
#     print(last)