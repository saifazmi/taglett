import boto, uuid
connS3 = boto.connect_s3()

for bucket in connS3.get_all_buckets():
    print "{name}\t{created}".format(
            name = bucket.name,
            created = bucket.creation_date,
    )


bucket = connS3.get_bucket('taglett.com')

fileID = str(uuid.uuid4())
filename = '%s.jpg' % fileID
s3FilePath = '/taglettImages/training/%s' % filename
#print s3Path+filename

key = bucket.new_key(s3FilePath)
personalImgPath = '/home/saif/Pictures/Wallpapers/circuit.jpg'
key.set_contents_from_filename(personalImgPath)
key.set_acl('public-read')

# k = Key(bucket)
# k.key = s3Path+filename
# k.set_contents_from_file('/home/saif/Pictures/Wallpapers/circuit.jpg')

# personalImgURL = k.generate_url(expires_in=0, query_auth=False)
personalImgURL = key.generate_url(expires_in=0, query_auth=False, force_http=True)
print personalImgURL