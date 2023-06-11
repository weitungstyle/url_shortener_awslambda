from flask_pymongo import PyMongo


class Database(object):
    def __init__(self, app):
        self.mongo = PyMongo(app)

    def insert(self, collection, data):
        self.mongo.db[collection].insert_one(data)

    def find(self, collection, query):
        return self.mongo.db[collection].find(query)

    def find_one(self, collection, query):
        return self.mongo.db[collection].find_one(query)

    def update(self, collection, query, data):
        self.mongo.db[collection].update(query, data)

    def delete(self, collection, query):
        self.mongo.db[collection].remove(query)

    def drop(self, collection):
        self.mongo.db[collection].drop()

    def drop_all(self):
        self.mongo.drop_all()

    def duplicated(self, collection, query):
        # return short_url if find one else None
        url = self.mongo.db[collection].find_one(query)
        if not url:
            return None
        return url['short_url']
