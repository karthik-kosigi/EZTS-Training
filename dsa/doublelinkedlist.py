class Node:
    def __init__(self,val):
        self.prev=None
        self.data=val
        self.next=None
class LinkedList:
    def __init__(self):
       self.head=None
    def insert_at_end(self,ele):
        nn=Node(ele)
        if self.head==None:
            self.head=nn
        elif self.head.next==None:
            self.head.next=nn
            nn.prev=self.head
        else:
            current=self.head
            while current.next:
                current=current.next
            current.next=nn
            nn.prev=current
    def insert_at_front(self,ele):
        nn=Node(ele)
        if self.head==None:
            self.head=nn
        else:
            nn.next=self.head
            self.head.prev=nn
            self.head=nn
        print("Node inserted successfully..")
    def delete_front(self):
        if self.head==None:
            print("No elements..")
        # elif self.head.next==None:
        #     current=self.head
        #     print(f"Element {current.data} deleted")
        #     del self.head
        else:
            current=self.head
            self.head=current.next
            current.prev=None
            print(f"Element {current.data} deleted")
            del current

    def display(self):
        if self.head==None:
            print("No Elements in the list.")
        else:
            current=self.head
            while current:
                print(current.data,end=" ")
                current=current.next
    def displayrev(self):
        if self.head==None:
            print("No Elements in the list.")
        else:
            current=self.head
            while current.next:
                current=current.next
            temp=current
            while temp:
                print(temp.data,end=" ")
                temp=temp.prev
            print()
llst=LinkedList()
while True:
    print("1.insert at end 2.insert at front 8.display reverse 9.display")
    ch=int(input("Enter your choice: "))
    if ch==1:
        ele=int(input("Enter element: "))
        llst.insert_at_end(ele)
    elif ch==2:
        ele=int(input("Enter element: "))
        llst.insert_at_front(ele)
    elif ch==3:
        llst.delete_front()
    elif ch==9:
        llst.display()
    elif ch==8:
        llst.displayrev()
    else:
        break