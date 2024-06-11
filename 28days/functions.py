# # def add(n1,n2):
# #     sum=n1+n2
# #     return sum
# # def sub(n1,n2):
# #     sub=n1-n2
# #     return sub
# # num1=float(input("Enter the first number: "))
# # num2=float(input("Enter seconfd number: "))
# # rs=add(num1,num2)
# # su=sub(num1,num2)
# # print("Sum of %.2f and %.2f is %.2f"%(num1,num2,rs))
# # print("difference of %.2f and %.2f is %.2f"%(num1,num2,su)) 

# num1=1122
# def show():
#     global num2
#     num2=2191
#     num3=22191
#     print(num1)
#     print(num2)
#     print(num3)
# show()
# print(num1)
# print(num2)
# print(num3)




# def operation(a,b,s):
#     if s=='+':
#         return a+b
#     elif s=='-':
#         return a-b
#     elif s=='*':
#         return a*b
#     elif s=='/':
#         return a/b
#     else:
#         print("Invalid operation")
# n1=int(input("Enter 1 number: "))
# n2=int(input("Enter 2 number: "))
# print("choose operation + - * /")
# ch=input()
# print(f"result = {operation(n1,n2,ch)}")


# def details(n,r):
#     print(n.upper(),r)

# nm="k v"
# rnk=1122
# details(nm,rnk)

# def details(n,r):#errorr
#     print(n.upper(),r)

# nm="k v"
# rnk=1122
# details(rnk,nm)



# #keyword arguements
# def k(iv,fv,sv):
#     print(iv,fv,sv)
# k(fv=25.34,iv=1122,sv='Python')
# k(sv='Python',fv=25.27,iv=1122)
# #k(s='python',i=1122,f=25.19)



# #variable length arguments
# def vlp(*args):
#     print()
#     for var in args :
#         print(var,end=' ')
# vlp(1122)
# vlp(1122,25.19)
# vlp(1122,25.19,'python')
# vlp(1122,25.19,'python','programming')


# //#variable keyword length arguments()
# #keyword arguements
# def k(**kwarg):
#     print()
#     for name,value in kwarg.items():
#         print(name,value,end=' ')
# k(fv=25.34)
# k(sv='Python',fv=25.27,iv=1122)
# #k(s='python',i=1122,f=25.19)


# def display(name,course='BTech'):
#     print("Name: "+name)
#     print("Course: ",course)

# display(course="BCA",name="arav")
# display(name="Reyansh")

# def cb(x):
#     '''CUBE OF A NUMBER'''
#     print(x**3)
# print(cb.__doc__)
# cb(5)


# ##innerfunction
# def outer_func():
#     def inner_func():
#         print("Welcome to python")
#     inner_func()
# outer_func()

# ## recursive function
# def rec(n1,n2):
#     if n2==0:
#         return n1
#     else:
#         return rec(n2,n1%n2)
# num1=48
# num2=12
# result=rec(num1,num2)
# print(f"The gcd of {num1} and {num2} is: {result}")


# ##factorial function
# def fac(n1):
#     if n1==0 or n1==1:
#         return 1
#     else:
#         return n1*fac(n1-1)
# n=0 
# print(f"The factorial of {n} is {fac(n)}")


# #filter() function
# def evn_chck(n):
#     return n%2==0
# nmbrs=range(21,39)
# ev_lst=list(filter(evn_chck,nmbrs))
# print(ev_lst)


# def sqr(x):
#     return x**2
# nmbr=[1,2,3,4,5]
# sqr_lst=map(sqr,nmbr)
# print(list(sqr_lst))

# from functools import reduce
# def add(x,y):
#     return x+y

# nmbrs=[1,2,3,4,5]
# result=reduce(add,nmbrs)
# print(result)


def nm():
    print(__name__)
    print("Name: ----")
def rno():
    print("Roll no :----")
print(__name__)
nm()
rno()
