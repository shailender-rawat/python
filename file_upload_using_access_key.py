from os import lseek
import boto3

s3client = boto3.client(
    's3',
    aws_access_key_id="AKIA4TPQDK6BSGTVUNU7",
    aws_secret_access_key="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"
)

bucket_name = "myawsbucket-ex01"
file_name = "Document.pdf"

with open(file_name, "rb") as f:
    s3client.upload_fileobj(f, bucket_name,file_name)