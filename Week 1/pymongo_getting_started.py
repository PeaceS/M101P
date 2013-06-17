import pymongo

from pymongo import MongoClient


# connect to db
connection = MongoClient('localhost', 27017)

# db test
db = connection.test

# handle to "name" collection
# db.names
names = db.names

item = names.find_one()

# get 'name'
print item['name']