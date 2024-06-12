# cred = {}
# def loginandRegister():
#     name = input("Enter first name:")
#     mob=input("Enter mobile number:")
#     username=input("Enter Username: ")
#     passwd = input("Enter password:")
#     cred[username] = passwd
#     print("Registration successfull..")

#     while True:
#         username=input("Enter Username: ")
#         passwd = input("Enter password:")
#         if cred[username]==passwd:
#             print("Login successfull..")
#             break
#         else:
#             print("Invalid credentials.. Enter again..")

# if __name__=="__main__":
#     loginandRegister()




# arr=[1,0,3,0,4,0,2]
# count = len(arr)
# j=0
# for i in range(count):
#     if arr[i]!=0:
#         arr[j]=arr[i]
#         j+=1
# while(j<count):
#     arr[j]=0
#     j+=1
# print(arr)

# def setting(**arg):
#     print(type(arg))

# setting(1,2,3,4)




# def fibb(n):
#     if n==0 or n==1:
#         return n
#     else:
#         return fibb(n-1)+fibb(n-2)
# for i in range(10):
#     print(fibb(i))


# def power(n,m):
#     if m==0:
#         return 1
#     elif m%2==0:
#         return power(n,m//2)*power(n,m//2)
#     else:
#         return power(n,m//2)*power(n,m//2)*n
# print(power(5,5))

# def power(n,m):
#     if m==0:
#         return 1
#     else:
#         return n*power(n,m-1)
# print(power(5,5))




# def summation(n):
#     if n==0:
#         return 0
#     else:
#         return (n%10) + (summation(n//10))
# print(summation(168))



# n=6
# p=2
# arr=[i for i in range(1,n+1)]
# arr[0]=1
# arr.append(n)
# res = (arr.index(p))// 2
# print(res)
