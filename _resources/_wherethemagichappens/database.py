from pymongo import MongoClient

client = MongoClient()
db = client.taglettDB
collection = db.TrainingImages

image = {
	"personalImgURL": "http://blahblah.com/xyz.jpg",
	"name": "John Blah"
}

collection.insert_one(image)