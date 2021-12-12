from os import lseek
import boto3

# Let's use Amazon S3
s3 = boto3.resource('s3')

# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)

bucket_name = "myawsbucket-ex01"

# Upload a new file
data = open('Document2.pdf', 'rb')

s3.Bucket(bucket_name).put_object(Key='SampleDocument.pdf', Body=data)

file_name = "Document.pdf"
s3 = boto3.client('s3')
with open(file_name, "rb") as f:
    s3.upload_fileobj(f, bucket_name,file_name)