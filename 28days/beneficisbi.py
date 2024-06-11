name_lst=[]
an_lst=[]
lmt_lst=[]
while True:
    print("1.ADD 2.VIEW")
    ch=int(input("Enter choice : "))
    if ch==1:
        name=input("Enter Name : ")
        while True:
            an=int(input("Enter account number: "))
            cn=int(input("confirm account number: "))
            if an==cn:
                tl=int(input("Enter limit:"))
                name_lst.append(name)
                an_lst.append(an)
                lmt_lst.append(tl)
                print("Beneficiary added ")
                break
            else:
                print("A/C not matched.Try again ")
    elif ch==2:
        if len(name_lst)==0:
            print("List is empty ")
        else:
            print("NAME\t\tACCOUNT NO:\tLIMIT")
            print("---------------------------")
            for i in range(len(name_lst)):
                print("%s\t\t%d\t\t%d"%(name_lst[i],an_lst[i],lmt_lst[i]))
    ch=input("Do you want to continue y/n:")
    if ch=="n":
        break

