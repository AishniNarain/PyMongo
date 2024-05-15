import pymongo

if __name__ == '__main__':
    client = pymongo.MongoClient("mongodb://localhost:27017")
    print(client)
    db = client["library"]
    collection = db["users"]
    
    #delete one
    data = {'name':'Alka'}
    
    # delete_data = collection.delete_one(data)
    # print(delete_data)
    
    # delete many
    delete_data = collection.delete_many(data)
    print(delete_data)