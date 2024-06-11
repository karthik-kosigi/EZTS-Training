import datetime
import pymongo as p
import time
import pandas as pd

if __name__ == "__main__": 
    client = p.MongoClient("mongodb://localhost:27017")
    db=client["Airnetworks"]
    users=db["userdata"]


    accounts={}
    def cal_end_date(amount):
        if amount==280:
            return 28
        elif amount==550:
            return 56
        elif amount==820:
            return 86
        elif amount==1600:
            return 168
        else:
            return amount//12
    def add_mobile_account(mobile_number,owner_name,balance=0):
        if users.find_one({"_id":mobile_number}) is None:       
            accounts[mobile_number]={"OwnerName":owner_name,"Balance":balance,"Last_Recharge_Date":"N.A","Validity":'N.A'}
            data = {
                "_id": mobile_number,
                "OwnerName": owner_name,
                "Balance": balance,
                "Last_Recharge_Date": "N.A",
                "Validity": "N.A",
            }
            users.insert_one(data)
            print("Creating Account",end="")
            for i in range(3):
                time.sleep(1)
                print(".",end="")
            print("\nAccount created successfully!")
            print(users.find_one({"-id":mobile_number}))
        else:
            print(f"Account with mobile number {mobile_number} already exists...")

    def recharge_mobile(mobile_number,amount):
        # if mobile_number in accounts.keys():
        # if users.find_one({"-id":mobile_number}):
        #     date=datetime.date.today()
        #     end_date=date + datetime.timedelta(days=cal_end_date(amount))
        #     accounts[mobile_number]["Balance"]+=amount
        #     accounts[mobile_number]["Last_Recharge_Date"]=date
        #     accounts[mobile_number]["Validity"]=end_date
        #     users.update_one({"-id":mobile_number},{"$inc": {"Balance":amount}})
        #     print(users.find_one({"-id":mobile_number}))
        #     print("Recharge Pending",end="")
        #     for i in range(5):
        #         time.sleep(1)
        #         print(".",end="")

        if users.find_one({"_id":mobile_number}):
            users.update_one({"_id":mobile_number},{"$inc":{"Balance": amount}})
            date=datetime.date.today()
            temp=users.find_one({"_id":mobile_number})
            if temp['Validity']=='N.A':
                end_date=date + datetime.timedelta(days=cal_end_date(amount))
            else:
                end_date=pd.to_datetime(temp['Validity'])+datetime.timedelta(days=cal_end_date(amount))
            users.update_one({"_id":mobile_number},{"$set":{"Last_Recharge_Date":str(date)}})
            users.update_one({"_id":mobile_number},{"$set":{"Validity":str(end_date)}})
            print("\nRecharge Done successfully :)")
        else:
            print(f"Account with mobile number {mobile_number} does not exists...")
    def check_mobile_balance(mobile_number):
        # if  mobile_number in accounts.keys():
        #     print("Account Balance: ",accounts[mobile_number]["Balance"])
        #     print("Validity upto: ",accounts[mobile_number]["Validity"])

        # else:
        #     print(f"Account with mobile number {mobile_number} does not exists...")   
        document = users.find_one({"_id": mobile_number})
        if document:
            print(f"Mobile number: {mobile_number}")
            print(f"Owner Name: {document['OwnerName']}")
            print(f"Balance: {document['Balance']}")
            print(f"Last Recharge Date: {document['Last_Recharge_Date']}")
            print(f"Validity: {document['Validity']}")
        else:
            print("Mobile number not found")
    def display_mobile_account_details(mobile_number):
        if users.find_one({"_id": mobile_number}) is None:
            print("No Account with this Number...")
        else:
            get=users.find_one({"_id":mobile_number})    
            print('----------------Air Networks-----------------')
            print('                         Date:%s\n'%datetime.date.today())
            print('Name:               %20s'%get['OwnerName'])
            print('Mobile Number:      %20s'%mobile_number)
            print('Balance:            %20s'%get["Balance"])
            print('Last Recharge Date: %20s'%get["Last_Recharge_Date"])
            print('Validity upto:      %20s'%get["Validity"]) 
            print('---------------------------------------------')
            users.create_index(["Balance"])
            result=users.find().sort("Balance")
            print(result)
    while True:
        print("1.Add New Mobile Account \n2.Recharge mobile Number \n3.Check mobile account balance \n4.Display account info \n5.Exit")
        ch=int(input("Enter your choice: "))
        if ch==1:
            owner_name=input("Enter Owner Name: ")
            while True:
                mobile_number=int(input("Enter Mobile number: "))
                confirm=int(input("Confirm Mobile number: "))
                if len(str(mobile_number))==10 and mobile_number.is_integer():
                    if mobile_number==confirm:
                        add_mobile_account(mobile_number,owner_name)
                        break
                    else:
                        print("Numbers does not match! Try again...")
                else:
                    print("Mobile number should be 10 digits and must be interger Try again..")
            
        elif ch==2:
            mobile_number=int(input("Enter Mobile Number:"))
            print("special packs: \n28 days : rs.280\n56 days : rs.550\n84 days : rs.820\n6 months pack(168 days) : rs.1600\nNormal Pack : rs.12 per day")
            amount=int(input("Enter Amount to Recharge: "))
            recharge_mobile(mobile_number,amount)
        elif ch==3:
            mobile_number=int(input("Enter Mobile Number:"))
            check_mobile_balance(mobile_number)

        elif ch==4:
            mobile_number=int(input("Enter Mobile number: "))
            display_mobile_account_details(mobile_number)
        elif ch==5:
            print("Exiting...Thank You!")
            client.close()
            
            break
        else:
            print("Invalid choice..Try again")
    