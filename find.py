import pymongo

if __name__ == '__main__':
    client = pymongo.MongoClient("mongodb://localhost:27017")
    print(client)
    db = client["library"]
    collection = db["users"]
    
    #find one
    one = collection.find_one({'name':'Aishni'})
    print(one)
    
    #find all
    all = collection.find({'name':'Aishni'},{'name':1, '_id':0})
    
    for item in all:
        print(item)