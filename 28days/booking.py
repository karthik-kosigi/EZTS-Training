count=0
book={}

print("1.booking  2.view  3.cancel")
ch=input("Enter choice: ")
if ch==1:
    name=input("Enter name: ")
    age=int(input("Enter age: "))
    start=input("Enter starting: ")
    dest=input("Enter destination: ")
    count+=1
    book['Name']=name
    book['Age']=age

print(book)


