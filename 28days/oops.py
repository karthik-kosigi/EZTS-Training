# class Test:
#     id=11222
# t=Test()
# print(t.id)


# class Emp():
#     name=None
#     eid=None
#     def set_details(self,nm,id):
#         self.name=nm
#         self.eid=id
#     def dsply(self):
#         print(self.name,self.eid)
# e1=Emp()
# e2=Emp()
# e1.set_details("K V ",1122)
# e2.set_details("Karthik" ,1123)
# e2.dsply()
# e1.dsply()




# class Emp():
#     name=None
#     eid=None
#     def set_details(self,nm,id):
#         self.name=nm
#         self.eid=id
#     def dsply(self):
#         print(self.name,self.eid)
# e=[]
# for i in range(5):
#     e.append(Emp.set_details("K V ",1122))
# for i in range(5):
#     print(e[i])


# class Emp():
#     def __init__(self,nm,id):
#         self.name=nm
#         self.eid=id
#     def dsply(self):
#         print(self.name,self.eid)

# e1=Emp("k v",1122)
# e1.dsply()






##converrting an instance to a string
# class Point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#         print(self.x)
# p=Point(12,34)
# print(p)


# class Point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def __str__(self):
#         return "({0},{1})".format(self.x,self.y)
# p=Point(12,34)
# print(p)



# class Point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def reflect_x(self):
#         self.x=self.x
#         self.y=-(self.y)
#     def __str__(self):
#         return "({0},{1})".format(self.x,self.y)
# p=Point(3,-5)
# p.reflect_x()
# print(p)



# class Point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def reflect_x(self):
#         return Point(self.x,-self.y)
#     def __str__(self):
#         return "({0},{1})".format(self.x,self.y)
# op=Point(3,-5)
# rp=op.reflect_x()
# print(op,rp)


# ##calculating midpoint
# class Point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def __str__(self):
#         return "({0},{1})".format(self.x,self.y)
#     def mid_p(p1,p2):
#         mx=(p1.x+p2.x)/2
#         my=(p1.y+p2.y)/2   
#         return Point(mx,my)
# p1=Point(-2,1)
# p2=Point(5,4)
# r=p1.mid_p(p2)
# print(str(r))


# ##calculating midpoint
# class Point:
#     def __init__(self,x,y,z):
#         self.x=x
#         self.y=y
#         self.z=z
#     def __str__(self):
#         return "({0},{1},{2})".format(self.x,self.y,self.z)
#     def mid_p(p1,p2):
#         mx=(p1.x+p2.x)/2
#         my=(p1.y+p2.y)/2
#         mz=(p1.z+p2.z)/2   
#         return Point(mx,my,mz)
# p1=Point(-2,1,3)
# p2=Point(5,4,5)
# r=p1.mid_p(p2)
# print(str(r))



# ##Data encapsulation
# class Emp:
#     def __init__(self,nm,id):
#         self.name=nm
#         self.__eid=id
#     def __dsply(self):
#         print(self.name,self.__eid)
# e1=Emp(" K K ",1122)
# print(e1.name)
# e1._Emp__dsply()
# print(e1._Emp__eid)



# class ABC():
#     def __init__(self,var1,var2):
#         self.var1=var1
#         self.__var2=var2
#     def display(self):
#         print("From class method ,var1=",self.var1)
#         print("From class method ,var2=",self.__var2)
# obj = ABC(10,20)
# obj.display()
# print("From main module,var1=",obj.var1)
# print("From main module,var2=",obj._ABC__var2)


# class ABC():
#     def __init__(self,var1,var2):
#         self.var1=var1
#         self.__var2=var2
#     def display(self):
#         print("From class method ,var1=",self.var1)
#         print("From class method ,var2=",self.__var2)
# class DEF():
#     def __init__(self,var1,var2):
#         self.var1=var1
#         self.__var2=var2
#     def dis(self):
#         obj1=ABC(30,40)
#         obj1.display()
# obj=DEF(10,20)
# obj.dis()


# class ABC():
#     def __init__(self,var):
#         self.var=var
#     def display(self):
#         print("Var is =",self.var)
#     def add_2(self):
#         self.var +=2
#         self.display()
# obj =ABC(10)
# obj.add_2()

