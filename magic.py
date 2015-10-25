import boto, uuid, recognisePeople, database

def upload(personalImgFile, personalImgURL, name):
	name = name.strip(' \t\n\r')
	name = name.replace(' ', '_')
	name = name.lower()

	if not personalImgURL :
		#convert path to url by storing in aws s3
		connS3 = boto.connect_s3()
		bucket = connS3.get_bucket('taglett.com')

		fileID = str(uuid.uuid4())
		filename = '%s.jpg' % fileID
		s3FilePath = '/taglettImages/training/%s' % filename

		key = bucket.new_key(s3FilePath)
		key.set_contents_from_file(personalImgFile)
		key.set_acl('public-read')

		personalImgURL = key.generate_url(expires_in=0, query_auth=False, force_http=True)

	# Add to DB
	database.addToDB(personalImgURL, name)

	# Training the clarifai api
	recognisePeople.train(personalImgURL, name)

def check(personalImgFile, personalImgURL, name):

	if not personalImgURL :
		#convert path to url by storing in aws s3
		connS3 = boto.connect_s3()
		bucket = connS3.get_bucket('taglett.com')

		fileID = str(uuid.uuid4())
		filename = '%s.jpg' % fileID
		s3FilePath = '/taglettImages/checking/%s' % filename

		key = bucket.new_key(s3FilePath)
		key.set_contents_from_file(personalImgFile)
		key.set_acl('public-read')

		personalImgURL = key.generate_url(expires_in=0, query_auth=False, force_http=True)

	# Getting the score of prediction
	score = recognisePeople.predictResult(personalImgURL, name)
	return score
