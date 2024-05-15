import pymongo

if __name__ == '__main__':
    client = pymongo.MongoClient("mongodb://localhost:27017")
    print(client)
    db = client["library"]
    collection = db["users"]
    
    #update one
    prev = {'name':'Aishni'}
    next = {"$set":{'email':'aishni@gmail.com'}}
    
    #update many
    update_email = collection.update_many(prev, next)
    print(update_email)