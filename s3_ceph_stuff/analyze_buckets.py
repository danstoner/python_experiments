import sys

if (sys.version_info < (3, 0)):
    raise SystemExit ("This script requires Python 3. Run with python3 <script_name>")

import json, os
import boto3

def s3connection(url):
    return boto3.resource(
        's3',
        aws_access_key_id=config['env']['IDB_STORAGE_ACCESS_KEY'],
        aws_secret_access_key=config['env']['IDB_STORAGE_SECRET_KEY'],
        endpoint_url=url,
        )

S3_SOURCE_URL = 'https://s.idigbio.org'  # will need to be s2
S3_DESTINATION_URL = 'https://s2.idigbio.org'   # will need to be s3

def load_config_file(p):
    with open(p, "r") as conf:
        json_config = json.load(conf)
        config.update(json_config)

def print_count_items_in_bucket(bucket):
    count = 0
    for each in bucket.objects.all():
        count += 1
        
    print ("Item count for bucket {0}: {1} ".format(bucket.name, count))

hr = "************************************************"

config_path = "~/"  # only use config from root of homedir
config = {}

fp = os.path.realpath(os.path.join(os.path.expanduser(config_path), "idigbio.json"))
try:
    load_config_file(fp)
except IOError:
    pass

print (hr)
print ('Bucket object counts from output of  "radosgw-admin --uid idigbio bucket stats"...')


with open("after_bucket_delete_radosgw_bucket_stats.json", "r") as json_input:
    RADOSGW_BUCKET_STATS = json.load(json_input)

for entry in RADOSGW_BUCKET_STATS:
    print (entry["bucket"], end=" ")
    try:
        print (entry["usage"]["rgw.main"]["num_objects"])
    except:
        print ("0")

print (hr)

print ("Make connections...")

buckets_to_do = ["idigbio-datasets-prod", "idigbio-downloads", "idigbio-sounds-prod"]

s3_source = s3connection(S3_SOURCE_URL)
s3_destination = s3connection(S3_DESTINATION_URL)
print(S3_SOURCE_URL)

print(hr)
print("All Buckets...")
for bucket in s3_source.buckets.all():
    print(bucket.name)

print(hr)
for b in buckets_to_do:
    print("Counting", b, "...")
    print_count_items_in_bucket(s3_source.Bucket(b))

