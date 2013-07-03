import pymongo
import sys

# establish a connection to the database
connection = pymongo.Connection("mongodb://localhost", safe=True)

# get a handle to the school database
db=connection.school
student = db.students


def delete():

    query = {}

    try:
        cursor = student.find(query)
        cursor = cursor.sort({'_id',pymongo.ASCENDING})

    except:
        print "Unexpected error:", sys.exc_info()[0]

    sanity = 0
    for doc in cursor:
      try:
        query_2 = {'_id':doc['_id']}
        cursor_2 = student.find(query_2)
        for doc_2 in doc["scores"]:
            done = False
            if doc_2['type'] == 'homework':
                if score_store == 0.0:
                    score_store = doc_2['score']
                elif score_store > doc_2['score']:
                    score_store = doc_2['score']
                    done = True
                else:
                    done = True
            else:
                score_store = 0.0
            if done == True:
                try:
                    print "Found: %f of %s" % (score_store, doc['_id'])
                    theStudent = student.find_one({'_id':doc['_id']})
                    print theStudent['scores']
                    theQuery = {'score':score_store}
                    theCursor = theStudent['scores'].remove(theQuery)
                except:
                    print "Cannot update:", sys.exc_info()[0]
      except:
        print "Cannot delete:", sys.exc_info()[0]
                    
delete()
