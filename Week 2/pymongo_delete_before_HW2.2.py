
import pymongo
import sys

# establish a connection to the database
connection = pymongo.Connection("mongodb://localhost", safe=True)

# get a handle to the school database
db=connection.students
scores = db.grades


def find():

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
            print "%s : %s" % (doc['student_id'], doc['score'])

            try:
                query_2 = {'sutdent_id':doc['student_id'],'score':doc['score']}
                cursor_2 = scores.find(query_2)
                cursor_2 = cursor_2.remove()
            except:
                print "Cannot delete:", sys.exc_info()[0]
                #scores.find({'sutdent_id':doc['student_id'],'score':doc['score']}).remove()
        printSkip = not printSkip
    
find()

