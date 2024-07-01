class Stack:
    def __init__(self) -> None:
        self.items=[]
    def push(self,data):
        self.items.append(data)
    def pop(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    def display(self):
        print(self.items)
    def top(self):
        return self.items[-1]
st = Stack()
exp = "{[1+2]"
for i in exp:
    st.display()
    if i =="[" or i=="(" or i=="{":
        st.push(i)

    if i == "]" :
        if st.top()=="[":
            st.pop()
    elif i==")":
        if st.top()=="(":
            st.pop()
    elif i=="}":
        if st.top()=="{":
            st.pop()
    elif i=="]"or i==")" or "}":
        st.push(i)

print(st.size())   
    
if st.size()==0:
    print("valid")
else:
    print("invalid")