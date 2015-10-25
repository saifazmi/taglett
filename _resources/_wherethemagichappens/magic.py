import cgi, boto, uuid, recognisePeople

form = cgi.FieldStorage()
name = form.getvalue('name')
personalImgURL = form.getvalue('personalImgPath')

connS3 = boto.connect_s3()
bucket = conn.get_bucket('taglet.com')

s3Path = '/tagletImages/training/'
filename = str(uuid.uuid4()+'.jpg')
key = bucket.new_key(s3path+filename)
key.get_contents_from_file(imgPath)
key.set_acl('public-read')

imgURL = key.generate_url(expires_in=0, query_auth=False)

train(imgURL)
