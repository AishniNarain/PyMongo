import pymongo

if __name__ == '__main__':
    client = pymongo.MongoClient("mongodb://localhost:27017")
    print(client)
    
    #show all databases
    all_database = client.list_database_names()
    print(all_database)
    
    db = client["library"]
    col = db.list_collection_names()
    print(col)
    # collection = db["users"]
    
    
    
    
    #insert one
    # dictionary = {'name':'Aishni', 'email':'aish@gmail.com', 'role':'admin'}
    # collection.insert_one(dictionary)
    
    insert_these = [
        {'name':'Aishni', 'email':'aish@gmail.com', 'role':'admin'},
        {'name':'Alka', 'email':'alka@gmail.com', 'role':'librarian'},
        {'name':'Aman', 'email':'aman@gmail.com', 'role':'student'},
        {'name':'Sakshi', 'email':'sak@gmail.com', 'role':'guest_user'}
    ]
    
    # collection.insert_many(insert_these)

