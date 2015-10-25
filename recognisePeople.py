from clarifai_basic import ClarifaiCustomModel
clarifai = ClarifaiCustomModel()

def train(ImgURL, name):
	# Positive data source
	clarifai.positive(ImgURL, name)

	# Negative data source
	clarifai.negative()

	# train the model
	clarifai.train(name)

#def predictResult(name):
	