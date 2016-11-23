import pymongo

if __name__ == "__main__":

    client = pymongo.MongoClient(localhost)
    db = client.nosqlclass

var cursor = db.Vocabulary.find({})
for document in cursor:
	print(document)
