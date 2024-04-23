from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, user, passwd, host, port, database, collection):
        """
        Initialize the AnimalShelter class.

        :param USER: MongoDB username.
        :param PASS: MongoDB password.
        """
        
        # Initialize the MongoClient
        User = user
        Passwd = passwd
        Host = host
        Port = port
        Database = database
        Collection = collection
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (User,Passwd,Host,Port))
        self.database = self.client['%s' % (Database)] # Connect to the 'AAC' database
        self.collection = self.database['%s' % (Collection)] # Connect to the 'animals' collection in the 'AAC' database

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        """
        Insert a document into the 'animals' collection.

        :param data: A dictionary representing the document to be inserted.
        """
        if data is not None:
            self.database.animals.insert_one(data)  # data should be dictionary
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            return False

# Read method to implement the R in CRUD.
    def read(self, query):
        """
        Query the 'animals' collection based on a given query.

        :param query: A dictionary representing the query to be executed.
        :return: A list of documents that match the query.
        """
        if query is not None:
            data = self.database.animals.find(query,{"_id": False})    
        else:
            data = self.database.animals.find({},{"_id": False})
        
        return data
    
#Update method to implement the U in CRUD
    def update(self, inputData, newData):
        """
        Query the 'animals' collection based on a given query.

        :param inputData: A dictionary representing the document to be executed.
        :return: A list of documents that match the query.
        """
        if inputData is not None:
            count = 0
            for instance in inputData:
                count += 1
                result = self.database.animals.update_many(inputData, {"$set": newData})
            return count
        else:
            raise Exception("Check data input and try again")
        return result
    
#Delete method to implement D in CRUD
    def delete(self, removeData):
        """
        Delete document(s) from the 'animals' collection based on a given query.

        :param removeData: A dictionary representing the document to be executed.
        :return: The number of documents deleted.
        """
        if removeData is not None:
            count = 0
            for instance in removeData:
                count += 1
                data = self.database.animals.delete_many(removeData)
            return count
        else:
            raise Exception("Check data input and try again")
            