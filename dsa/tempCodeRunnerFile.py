##Queue using linked list

class Node:
    def __init__(self,val,prity):
        self.data=val
        self.priority=prity
        self.next=None
class PriorityQueue:
    def __init__(self):
        self.front=None
    def is_empty(self):
         return self.front is None
    def enq(self,ele,priority):
        nn=Node(ele,priority)
        if self.is_empty() or priority>self.front.priority:
            nn.next=self.front
            self.front=nn
        else:
            current=self.front
            while current.next and current.next.priority>priority:
                current=current.next
            nn.next=current.next
            current.next=nn
    def deq(self):
        if self.is_empty():

            print("Queue underflow..")
            return None
        data=self.front.data
        self.front=self.front.next
        return data
    
    def peek(self):
        if self.is_empty():
            print("Queue is Empty")
        else:
            print("peek of element: ",self.front.data)
    def display(self):
        if self.is_empty():
            print("Queue is Empty")
        else:
            current=self.front
            while current:
                print(f"({current.data},{current.priority}",end=" ")
                current=current.next
            print()
q=PriorityQueue()
while True:
    print("1.Enqueue 2.dequeue 3.display 4.peek 5.Exit ")
    ch=int(input("Enter your choice: "))
    if ch==1:
        ele=int(input("Enter Element to be inserted: "))
        priority=int(input("enter priority: "))
        q.enq(ele,priority)
    elif ch==2:
        q.deq()
    elif ch==3:
        q.display()
    elif ch==4:
        q.peek()
    elif ch==5:
        break