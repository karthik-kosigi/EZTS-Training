# que=[]
# frnt=rr=-1
# sz=int(input("Enter the size of the queue: "))
# def en_que():
#     global frnt,rr
#     if rr==sz-1:
#         print("queue overflow")
#     else:
#         ele=int(input("Enter element to enqueue :"))
#         if rr==-1:
#             frnt=0
#         rr=rr+1
#         que.append(ele)
# def de_que():
#     global frnt,rr
#     if rr==-1:
#         print("Queue is empty..")
#     else:
#         ele=que[frnt]
#         frnt+=1
#         print(f"Element {ele} dequeued..") 

# def display():
#     if frnt==-1 or frnt>rr:
#         print("Queue is empty..")
#     else:
#         for i in range(frnt,rr+1):
#             print(que[i],end=" ")
# def peek():
#     global frnt,rr
#     if frnt==-1 or frnt>rr:
#         print("Queue is Empty..")
#     else:
#         print("Front Element of the queue is:",que[frnt])


# while True:
#     print("1.insert 2.delete")
#     ch=int(input("Enter your choice: "))
#     if ch==1:
#         en_que()
#     elif ch==2:
#         de_que()
#     elif ch==3:
#         peek()
#     elif ch==3:
#         display()
#     elif ch==4:
#         print("Terminated..")
#         break
#     else:
#         print("Invalid choice try again")












# que=[]
# frnt=rr=-1
# sz=int(input("Enter the size of the queue: "))
# def en_que():
#     if len(que)==sz:
#         print("Queue Overflow")
#     else:
#         ele=int(input("Enter element to be enqueued:"))
#         que.append(ele)
#         print(que)
# def de_que():
#     global frnt,rr
#     if not que:
#         print("Queue undderflow..")
#     else:
#         ele=que.pop(0)
#         print(f"Element {ele} dequeued..")

# def display():
#     if not que:
#         print("Queue is empty..")
#     else:
#         for i in que:
#             print(i,end=" ")
# def peek():
#     global frnt,rr
#     if frnt==-1 or frnt>rr:
#         print("Queue is Empty..")
#     else:
#         print("Front Element of the queue is:",que[frnt])


# while True:
#     print("1.insert 2.delete")
#     ch=int(input("Enter your choice: "))
#     if ch==1:
#         en_que()
#     elif ch==2:
#         de_que()
#     elif ch==3:
#         peek()
#     elif ch==3:
#         display()
#     elif ch==4:
#         print("Terminated..")
#         break
#     else:
#         print("Invalid choice try again")












# ##Queue using linked list

# class Node:
#     def __init__(self,val):
#         self.data=val
#         self.next=None
# class Queue:
#     def __init__(self):
#         self.front=self.rear=None

#     def enq(self):
#         ele=int(input("Enter Element: "))
#         nn=Node(ele)
#         if self.rear is None:
#             self.front=self.rear=nn
#         else:
#             self.rear.next=nn
#             self.rear=nn
#     def deq(self):
#         if self.front is None:
#             print("Queue underflow..")
#         else:
#             ele=self.front.data
#             print(f"{ele} deleted")
#             self.front=self.front.next
#             if self.front==None:
#                 self.rear=None
#     def peek(self):
#         if self.front is None:
#             print("Queue Empty..")
#         else:
#             print(self.front.data)

#     def display(self):
#         current=self.front
#         while current:
#             print(current.data,end=" ")
#             current=current.next
# q=Queue()
# while True:
#     print("1.Enqueue 2.dequeue 3.display ")
#     ch=int(input("Enter your choice: "))
#     if ch==1:
#         q.enq()
#     elif ch==2:
#         q.deq()
#     elif ch==3:
#         q.display()




# ## circular queue(ring buffer)

# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class CircularQueue:
#     def __init__(self,size):
#         self.front=None
#         self.rear=None
#         self.size=size
#         self.count=0
    
#     def is_full(self):
#         return self.count==self.size
#     def is_empty(self):
#         return self.count==0
#     def enq(self,data):
#         if self.is_full():
#             print("Queue Overflow")
#             return
#         else:
#             nn=Node(data)
#             if self.is_empty():
#                 self.front=nn
#             else:
#                 self.rear.next=nn
#             self.rear=nn
#             self.rear.next=self.front
#             self.count+=1
#     def deq(self):
#         if self.is_empty():
#             print("Queue underflow")
#         else:
#             data=self.front.data
#             if self.front==self.rear:
#                 self.front=None
#             else:
#                 self.front=self.front.next
#                 self.rear.next=self.front
#             self.count-=1
#             print(data," Deleted")
#     def peek(self):
#         if self.is_empty():
#             print("Queue is empty")
#         else:
#             print("peek of element: ",self.front.data)
#     def display(self):
#         if self.is_empty():
#             print("Queue is empty")
#         else:
#             temp=self.front
#             while True:
#                 print(temp.data,end=' ')
#                 temp=temp.next
#                 if temp==self.front:
#                     break


# size=int(input("Enter size of queue: "))
# q=CircularQueue(size)
# while True:
#     print("1.enqueue 2.dequeue 3.peek 4.display 5.exit")
#     ch=int(input("Enter your choice: "))
#     match ch:
#         case 1:
#             ele=int(input("Enter element : "))
#             q.enq(ele)
#         case 2:
#             q.deq()
#         case 3: 
#             q.peek()
#         case 4:
#             q.display()
#         case 5:
#             break









# ##Queue using linked list

# class Node:
#     def __init__(self,val,prity):
#         self.data=val
#         self.priority=prity
#         self.next=None
# class PriorityQueue:
#     def __init__(self):
#         self.front=None
#     def is_empty(self):
#          return self.front is None
#     def enq(self,ele,priority):
#         nn=Node(ele,priority)
#         if self.is_empty() or priority>self.front.priority:
#             nn.next=self.front
#             self.front=nn
#         else:
#             current=self.front
#             while current.next and current.next.priority>priority:
#                 current=current.next
#             nn.next=current.next
#             current.next=nn
#     def deq(self):
#         if self.is_empty():

#             print("Queue underflow..")
#             return None
#         data=self.front.data
#         self.front=self.front.next
#         return data
    
#     def peek(self):
#         if self.is_empty():
#             print("Queue is Empty")
#         else:
#             print("peek of element: ",self.front.data)
#     def display(self):
#         if self.is_empty():
#             print("Queue is Empty")
#         else:
#             current=self.front
#             while current:
#                 print(f"{current.data},{current.priority}",end=" ")
#                 current=current.next
#             print()
# q=PriorityQueue()
# while True:
#     print("1.Enqueue 2.dequeue 3.display 4.peek 5.Exit ")
#     ch=int(input("Enter your choice: "))
#     if ch==1:
#         ele=int(input("Enter Element to be inserted: "))
#         priority=int(input("enter priority: "))
#         q.enq(ele,priority)
#     elif ch==2:
#         q.deq()
#     elif ch==3:
#         q.display()
#     elif ch==4:
#         q.peek()
#     elif ch==5:
#         break
















