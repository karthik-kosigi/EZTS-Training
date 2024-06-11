import random
tranction=()
ac1=123456
op_bal=5000
avl_bal=op_bal
while True:
    print("1.Todo tranction 2.view 3.exit")
    ch=int(input("Enter choice :"))
    if ch==1:
        ty=input("Traction deposit or withdraw: d/w :")
        if ty=='w':
            while True:
                wd=int(input("Enter withdraw amount :"))
                if avl_bal<wd:
                    print("insufficient balance.Try again..")
                else:
                    avl_bal-=wd
                    tid=random.randint(100000,999999)
                    tranction=tranction+((tid,ac1,ty,wd,avl_bal),)
                    print("Withdraw done")
                    break
        elif ty=='d':
            dp=int(input("Enter deposit amount: "))
            avl_bal+=dp
            tid=random.randint(100000,999999)
            tranction=tranction+((tid,ac1,ty,dp,avl_bal),)
            print("Deposit done")
    elif ch==2:
        if len(tranction)<=0:
            print("No transactions..")
        for i in tranction:
            print(*i)
    elif ch==3:
        print("exiting...Thank you")   
        break
    else:
        print("Incorrect choice..Try again.")