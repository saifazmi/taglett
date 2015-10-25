import boto
conn = boto.connect_s3()

for bucket in conn.get_all_buckets():
    print "{name}\t{created}".format(
            name = bucket.name,
            created = bucket.creation_date,
    )

bucket = conn.get_bucket('taglet.com')

key = bucket.new_key('/test/hello.txt')
key.set_contents_from_string('Hello World!')
