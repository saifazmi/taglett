from clarifai_basic import ClarifaiCustomModel
clarifai = ClarifaiCustomModel()

def train(ImgURL, name):
	# Positive data source
	clarifai.positive(ImgURL, name)

	negative_source = ["https://ollienollie.files.wordpress.com/2009/10/untitled-181.jpg",
	"https://c2.staticflickr.com/4/3500/3895160739_51bd7a644a.jpg",
	"http://www.facesmainst.com/manager/profile/pix/photo252-20091124013740.jpg",
	"http://static1.squarespace.com/static/5577b787e4b02cd823df9127/5578c73be4b0b454e5bdce91/5578c785e4b007898ac4a747/1433978757441/face32.jpg",
	"http://www.funnyfacespictures.net/pictures/funny-faces-crazy_eyes.jpg",
	"https://c2.staticflickr.com/6/5190/5580706695_cc7cf9d96c_b.jpg",
	"http://farm8.staticflickr.com/7005/6404355801_e90c7fe1ff_z.jpg",
	"http://www.lahiguera.net/cinemania/actores/julian_villagran/fotos/2551/julian_villagran.jpg",
	"http://www.polyvore.com/cgi/img-thing?.out=jpg&size=l&tid=92080475"
	"http://img2-3.timeinc.net/people/i/2010/news/100719/lindsay-lohan-1-240.jpg",
	"http://4.bp.blogspot.com/_cG2SV6Pnny4/SVEMe3VpLEI/AAAAAAAABic/tysh9iiyGuQ/s400/12_b.jpg",
	"http://www.polyvore.com/cgi/img-thing?.out=jpg&size=l&tid=116178971"
	]

	# Negative data source
	for negative in negative_source:
		clarifai.negative(negative,name)

	# train the model
	clarifai.train(name)

def predictResult(testURL, name):
	resultJSON = clarifai.predict(testURL, name)
	confidenceScore = resultJSON['urls'][0]['score']
	return str(confidenceScore)
