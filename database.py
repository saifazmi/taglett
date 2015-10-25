from pymongo import MongoClient

def addToDB(personalImgURL, nameTag):
	client = MongoClient()
	db = client.taglettDB
	collection = db.TrainingImages

	image = {
		"personalImgURL": str(personalImgURL),
		"name_tag": str(nameTag)
	}
	
	collection.insert_one(image)