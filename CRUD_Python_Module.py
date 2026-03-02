#Roger Fisher 2/4/2026

from pymongo import MongoClient

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self, username, password): 
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection.
        
        # Connection Variables 
        USER = username
        PASS = password
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 
        
        # Initialize Connection 
        self.client = MongoClient('mongodb://%s:%s@%s:%d?authSource=admin' % (USER,PASS,HOST,PORT)) 
        self.database = self.client[DB] 
        self.collection = self.database[COL]
    
    #--------------------------------------------------------------------        
    # Complete this create method to implement the C in CRUD. 
    
    # Inserts a new document into the animals collection
    def create(self, document):
        if document is not None: 
            self.collection.insert_one(document) 
            return True
        else: 
            return False 
        
    #----------------------------------------------------------------------
    # Create method to implement the R in CRUD.
    
    # Retrieve the documents from the animals collection that match the query
    def read(self, query):
        if query is not None:
            results = self.collection.find(query)
            return list(results)
        else:
            return[]
    
    #---------------------------------------------------------------------
    # Update Method to implement U in CRUD
    
    # Update the existing documents that match the query
    def update(self, query, new_values):
        if query is not None and new_values is not None:
            result = self.collection.update_many(
                query,
                {"$set": new_values}
            )
            return result.modified_count
        else: 
            return 0
    #---------------------------------------------------------------------    
    # Delete Method to implement D in CRUD
    
    # Delete the documents from the animals collection that match the query
    def delete (self, query):
        if query is not None: 
            result = self.collection.delete_many(query)
            return result.deleted_count
        else: 
            return 0 