import pymongo as p



if __name__ == "__main__": 
    client = p.MongoClient("mongodb://localhost:27017")
    db=client["Airnetworks"]
    users=db["userdata"]
