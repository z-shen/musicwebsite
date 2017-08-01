import pymongo

class Database():
    def __init__(self, url, database):
        self.url = url
        self.client = pymongo.MongoClient([self.url])
        self.database = self.client[database]

    def insert(self,collection,data):
        self.database[collection].insert(data)

    def find(self, collection, data):
        return self.database[collection].find(data)

    def find_one(self, collection, data):
        return self.database[collection].find_one(data)


    def remove(self, collection, data):
        self.database[collection].remove(data)
