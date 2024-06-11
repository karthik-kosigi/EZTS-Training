# class College():
#     def Clg(self):
#         print("College: ")
# class Department(College):
#     def dpt(self):
#         print("Department: ")
# class designation(Department):
#     def dsgn(self):
#         print("Designation: ")
# ob=designation()
# ob.Clg()
# ob.dpt()
# ob.dsgn()


class Vehicle:
    def wheels(self):
        pass
class Cycle(Vehicle):
    def wheels(self):
        return "two"
