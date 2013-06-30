
import pymongo
import sys

# establish a connection to the database
connection = pymongo.Connection("mongodb://localhost", safe=True)

# get a handle to the school database
db=connection.students
scores = db.grades


def delete():

    query = {'type':'homework'}

    try:
        cursor = scores.find(query)
        cursor = cursor.sort([('student_id',pymongo.ASCENDING),('score',pymongo.ASCENDING)])

    except:
        print "Unexpected error:", sys.exc_info()[0]

    sanity = 0
    printSkip = False
    for doc in cursor:
        if not printSkip:

            try:
                query_2 = {'_id':doc['_id']}
                cursor_2 = scores.remove(query_2)
                print "Deleted: %s of %s" % (doc['score'], doc['student_id'])
            except:
                print "Cannot delete:", sys.exc_info()[0]
                
        printSkip = not printSkip
    
delete()

