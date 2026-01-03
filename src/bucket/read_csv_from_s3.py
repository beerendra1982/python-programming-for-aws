import boto3
import pandas as pd
from io import StringIO

def read_csv_from_s3(bucket, key):
    s3 = boto3.client("s3")
    csv_obj = s3.get_object(Bucket=bucket, Key=key)
    body = csv_obj["Body"].read().decode("utf-8")
    df = pd.read_csv(StringIO(body))
    return df
