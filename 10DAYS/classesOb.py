# '''
# class ->  collection of data members and member functions
# object-> it can access and communicate with the data members and member functions of the class
# '''
# import streamlit as st
# class Movie:
#     def __init__(self,mName,mActor):
#         self.mName = mName
#         self.mActor = mActor
#         pass
#     def get_details(self):
#         print(f"{self.mName} starring {self.mActor}")
#         pass
# mName = input("Enter movie name:")
# mActor = input("Enter actor:")
# m1=Movie(mName,mActor)
# m1.get_details()
# st.title(f"{mName} starring {mActor}") 



# class Movie:
#     def sett(self):
#         self.title = input("Movie title: ")
#         self.year = input("Year: ")
# class Actors(Movie):
#     def __init__(self):
        
#         self.actor = input("Actor Name:")
#         self.age = input("Actor age:")
#     def print(self):
#         print(f"{self.title}  {self.year}")
#         print(f"{self.actor}  {self.age}")
        
# obj = Actors()
# print()




# class Movie:
#     title = "batman"
#     year = "2019"
# class Actors(Movie):
#     actor = "Ben affleck"
#     age = 40
#     # def print(self):
#     #     print(f"{self.title}  {self.year}")
#     #     print(f"{self.actor}  {self.age}")
# class Actress(Actors):
#     name="Gal Gadot"
#     age = 30
# obj = Actress()
# print(obj.year)



# class Movie:
#     title = "batman"
#     year = "2019"
# class Actors(Movie):
#     actor = "Ben affleck"
#     age = 40
#     # def print(self):
#     #     print(f"{self.title}  {self.year}")
#     #     print(f"{self.actor}  {self.age}")
# class Actress(Movie):
#     name="Gal Gadot"
#     age = 30
# obj = Actress()
# print(obj.age)


  


# class Movie:
#     title = "batman"
#     year = "2019"
# class Actors():
#     actor = "Ben affleck"
#     age = 40
#     # def print(self):
#     #     print(f"{self.title}  {self.year}")
#     #     print(f"{self.actor}  {self.age}")
# class Actress(Movie,Actors):
#     name="Gal Gadot"
#     age = 30
# obj = Actress()
# print(obj.title)
# print(obj.actor)
# print(obj.age)




# two pointer approach
# a=[2,1,0,1,1,2,0,0]
# c0,c1,c2=0,0,0
# l=0
# r=len(a)-1
# for i in a:
#     if i ==0:
#         c0+=1
#     if i==1:
#         c1+=1
#     if i==2:
#         c2+=1
# print(c0,c1,c2)
# j=0
# while c0>0:
#     a[j]=0
#     j=j+1
#     c0-=1
# while c1>0:
#     a[j]=1
#     j+=1
#     c1-=1
# while c2>0:
#     a[j]=2
#     j+=1
#     c2-=1
# print(a)




class Student:
    def __init__(self):
        self.name = input("Enter name: ")
        self.usn = input("ENter usn: ")
        self.marks=[]
        for i in range(5):
            self.marks.append(int(input(f"Enter marks of subject {i+1}: ")))
        self.calculate(self.marks)
    def calculate(self,marks):
        self.total = sum(marks)
        self.percentage = (self.total/500)*100
        self.grade = "A" if self.percentage >70 else "B"
    def display(self):
                print(f"{self.name}\t{self.usn}\t{self.total}\t{self.grade}\t{self.percentage}")
s = [0]*2
for i in range(2):
      s[i]  = Student()
print("NAME\tUSN\tTOTAL\tGRADE\tPERCENTAGE")
for i in range(2):
      s[i].display()
    
