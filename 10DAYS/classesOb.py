'''
class ->  collection of data members and member functions
object-> it can access and communicate with the data members and member functions of the class
'''
import streamlit as st
class Movie:
    def __init__(self,mName,mActor):
        self.mName = mName
        self.mActor = mActor
        pass
    def get_details(self):
        print(f"{self.mName} starring {self.mActor}")
        pass
mName = input("Enter movie name:")
mActor = input("Enter actor:")
m1=Movie(mName,mActor)
m1.get_details()
st.title(f"{mName} starring {mActor}") 

