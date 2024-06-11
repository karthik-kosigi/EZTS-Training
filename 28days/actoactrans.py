import sys,random
un={}
av={}
while True:
    print("1.create a/c  2.View 3.exit 4.Transaction")
    ch=int(input("Enter choice: "))
    if ch==1:
        while True:
            ac=random.randint(100000,999999)
            if ac not in un:
                name=input("Enter a/c holder name: ")
                bal=int(input("Enter balance: "))
                un[ac]=name
                av[ac]=bal
                print("Account created...")
                break
    elif ch==2:
        if len(un)==0:
            print("no accounts")
        else:
            for i,j in un.items():
                print(i,j,av[i])

    elif ch==3:
        print("Exiting..")
        break
    elif ch==4:
        print(un)
        while True:
            un1=int(input("Enter your a/c no:  "))
            un2=int(input("Enter reciever a/c no: "))
            if un1 not in un and un2 not in un:
                print("Enter correct a/c nos...Try again.")
            else:
                while True:
                    amt=int(input("Enter amount to transfer:"))
                    if amt>av[un1]:
                        print("Insufficient balance....Try again.")
                    else:
                        av[un1]=av[un1]-amt
                        av[un2]=av[un2]+amt
                        print("Transaction done successfully..")
                        break
                break



        
