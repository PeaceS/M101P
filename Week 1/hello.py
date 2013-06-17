import bottle
import pymongo

@bottle.route('/')
def index():

	# connect to mongoDB
	connection = pymongo.MongoClient('localhost',27017)

	# db test
	db = connection.test

	# db.names
	name = db.names

	# get single doc
	item = name.find_one()

	return '<b>Hello %s!</b>' % item['name']

bottle.run(host='localhost', port=8082)