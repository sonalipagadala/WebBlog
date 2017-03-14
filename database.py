import pymongo


class Database(object):
    URI = "mongodb://127.0.0.1:27017"   # Uniform Resource Identifier:A String of characters which helps to identify a resource
    DATABASE = None

    @staticmethod      #static as that of c++ & java
    def initialize():                 # A method used to initialize all the attributes in a class
        client = pymongo.MongoClient(Database.URI)     # Connecting to the mongo instance.Now, client has a list of all the databases
        Database.DATABASE = client['fullstack']     #DATABASE has a list of all the collections

    @staticmethod
    def insert(collection, data):
        return Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
       return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)




