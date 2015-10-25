from pymongo import MongoClient

client = MongoClient()
db = client.taglettDB
collection = db.TrainingImages

def addToDB(personalImgURL, nameTag):
	image = {
		"personalImgURL": str(personalImgURL),
		"name_tag": str(nameTag)
	}
	
	return collection.insert_one(image)

def getImageData(name):
	name = name.strip(' \t\n\r')
	name = name.replace(' ', '_')

	return collection.find({"name_tag" : name})