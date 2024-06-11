# class Node:
#     def __init__(self,val):
#         self.data=val
#         self.next=None
# n1=Node(10)
# n2=Node(20)
# n1.next=n2
# while n1:
#     print(n1.data)
#     n1=n1.next
# n1=7
# n2=5
# n2,n1=n1,n2
# print(n1,n2)



# class Node:
#     def __init__(self,val):
#         self.data=val
#         self.next=None
#     def display(self):
#         while self:
#             print(self.data)
#             self=self.next
# n1=Node(10)
# n2=Node(20)
# n1.next=n2
# n1.display()

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
       self.head=None
    def insert_at_end(self,ele):
        nn=Node(ele)
        if self.head==None:
            self.head=nn
        else:
            current=self.head
            while current.next:
                current=current.next
            current.next=nn
        print("Node inserted successfully....")
    def insert_at_front(self,ele):
        nn=Node(ele)
        if self.head==None:
            self.head=nn
        else:
            nn.next=self.head
            self.head=nn
        print("Node inserted successfully....")
    def delete_at_front(self):
        if self.head==None:
            print("No Elements in the list.")
        else:
            print(f"Element {self.head.data} deleted")
            current=self.head
            self.head=current.next
            del current
    def delete_at_end(self):
        if self.head==None:
            print("No Elements in the list.")
        elif self.head.next==None:
            print(f"Element {self.head.data} deleted")
            current=self.head
            self.head=None
            del current
        else:
            current=self.head
            prev=current
            while current.next:
                prev=current
                current=current.next
            print(f"Element {current.data} deleted")
            prev.next=None
            del current
    def display(self):
        if self.head==None:
            print("No Elements in the list.")
        else:
            current=self.head
            while current:
                print(current.data,end=" ")
                current=current.next
    def search(self,ele):
        pos=0
        current=self.head
        while current.next:
            pos+=1
            if current.data==ele:
                print(f"Element found at {pos}")
                break
            else:
                print("Element not found")
    def insert_before(self,ele,bef):
        nn=Node(ele)
        if self.head==None:
            print("No target element...")
      
        elif self.head.data==bef:
                nn.next=self.head
                self.head=nn
                print("Node inserted successfully...")
        else:
            current=self.head
            prev=current
            while current:
                if current.data==bef:
                    prev.next=nn
                    nn.next=current    
                    print("Node inserted successfully..")
                    break
                else:
                    prev=current
                    current=current.next
            else:
                print("Target element not found.")
    # def insert_after(self,ele,aft):
    #     nn=Node(ele)
    #     if self.head==None:
    #         print("No target element...")
    #     elif self.head.next==None:
    #         if self.head.data==aft:
    #             self.head.next=nn
    #             print("Node inserted successfully...")
    #         else:
    #             print("Target element not found.")
    #     elif self.head.next.data==aft:
    #         self.head.next=nn
    #     else:
    #         current=self.head.next
    #   
    #         while current:
    #             if current.data==aft:
    #                
    #                 nn.next=current.next  
    #                  current.next=nn
    #                 print("Node inserted successfully..")
    #                 break
    #             else:
    #                 current=current.next
    #                 
    #         else:
    #             print("Target element not found.")    
    def insert_after(self,ele,aft):
        nn=Node(ele)
        current=self.head
        while current and current.data!=aft:
            current=current.next
        if current:
            nn.next=current.next
            current.next=nn
        else:
            print("Target not found.")

    def rev(self):
        # if self.head==None:
        #     print("No elements..")
        # elif self.head.next==None:
        #     print("Only one element..")
        # else:
        #     current=llst.head
        #     curr1=self.head
        #     while current:
        #         curr1=current
        #         current=current.next
        #         curr1=curr1.next
        current=self.head
        prev=None
        while current:
            next_node=current.next
            current.next=prev
            prev=current
            current=next_node
        self.head=prev

        

llst=LinkedList()
llstrev=LinkedList()
while True:
    print("1.insert at end 2.insert in front 3.delete at front 4.delete_at end 5.display 6.search 7.insert before 8.insert after")
    ch=int(input("Enter choice: "))
    if ch==1:
        ele=int(input("Enter element to insert: "))
        llst.insert_at_end(ele)
    elif ch==2:
        ele=int(input("Enter element to insert: "))
        llst.insert_at_front(ele)
    elif ch==3:
        llst.delete_at_front()
    elif ch==4:
        llst.delete_at_end()
    elif ch==5:
        llst.display()
    elif ch==6:
        ele=int(input("Enter element to search:"))
        llst.search(ele)
    elif ch==7:
        ele=int(input("Enter element to insert: "))
        bef=int(input("Enter node where u want to insert: "))
        llst.insert_before(ele,bef)
    elif ch==8:
        ele=int(input("Enter element to insert: "))
        aft=int(input("Enter node after which u want to insert: "))
        llst.insert_after(ele,aft)
    elif ch==9:
        llst.rev()
    else:
        break


