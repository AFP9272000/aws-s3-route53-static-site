import boto3

s3 = boto3.client('s3', region_name='us-east-2')

bucket_name = 'addisonengineer.org'  # must be globally unique

# Create bucket
s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint': 'us-east-2'})

# Upload file
s3.upload_file('index.html', bucket_name, 'index.html')

s3.upload_file('error.html', bucket_name, 'error.html')

print(f"✅ Uploaded 'index.html' and 'error.html' to {bucket_name}")
