
import pymongo

from pymongo import MongoClient


# connect to database
connection = MongoClient('localhost', 27017)

db = connection.students

# handle to names collection
names = db.grades

item = names.find()

print item

