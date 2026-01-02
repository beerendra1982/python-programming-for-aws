import boto3


# Create an S3 client
def bucket_contents():
    s3 = boto3.client("s3")

    bucket_name = "beeru-bucket"

    response = s3.list_objects_v2(Bucket=bucket_name)

    print(f"Files in bucket '{bucket_name}':")

    if "Contents" in response:
        for obj in response["Contents"]:
            print(f"- {obj['Key']}")
    else:
        print("Bucket is empty or does not exist.")


def list_buckets():
    s3 = boto3.client("s3")

    response = s3.list_buckets()

    print("S3 Buckets:")
    for bucket in response["Buckets"]:
        print(f"- {bucket['Name']}")


from botocore.exceptions import NoCredentialsError, ClientError


def upload_csv_to_s3(local_file, bucket_name, s3_key):
    """
    Upload a local CSV file to an S3 bucket.

    :param local_file: Path to the local CSV file (e.g., 'data/file.csv')
    :param bucket_name: Target S3 bucket name
    :param s3_key: S3 object key (e.g., 'uploads/file.csv')
    """
    s3 = boto3.client("s3")

    try:
        s3.upload_file(local_file, bucket_name, s3_key)
        print(f"Uploaded successfully to s3://{bucket_name}/{s3_key}")
    except FileNotFoundError:
        print("Local file not found.")
    except NoCredentialsError:
        print("AWS credentials not found.")
    except ClientError as e:
        print(f"Upload failed: {e}")


if __name__ == "__main__":
    list_buckets()
    upload_csv_to_s3(
        local_file="data/emp.csv", bucket_name="beeru-bucket", s3_key="incoming/emp.csv"
    )
    bucket_contents()
