import boto3

# Create an S3 client
s3 = boto3.client('s3')

bucket_name = "beeru-bucket"

response = s3.list_objects_v2(Bucket=bucket_name)

print(f"Files in bucket '{bucket_name}':")

if "Contents" in response:
    for obj in response["Contents"]:
        print(f"- {obj['Key']}")
else:
    print("Bucket is empty or does not exist.")
