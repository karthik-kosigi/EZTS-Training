import pymongo as p  

if __name__ == "__main__":     
    client=p.MongoClient("mongodb://localhost:27017")
    db=client["mydatabase"]
    users=db["mycollection"]
    alldbs=client.list_database_names()
    print(alldbs)
    print(db.list_collection_names())