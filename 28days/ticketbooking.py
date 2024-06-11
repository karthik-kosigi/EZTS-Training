confirm=5
waiting=3
count=0
book={}
while True:
    print("1.booking  2.view  3.cancel")
    ch=int(input("Enter choice: "))
    if ch==1:
        if count<8:
            name=input("Enter name: ")
            age=int(input("Enter age: "))
            start=input("Enter starting: ")
            dest=input("Enter destination: ")
            count+=1
            book[count]={'Name':name,'Age':age,'Source':start,'Destination':dest,'Status':"waiting"}
            print(book)
        else:
            print("Tickets not available..")

    else:
        break
print(book)




