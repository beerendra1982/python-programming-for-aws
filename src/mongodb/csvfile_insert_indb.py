from src.bucket.read_csv_from_s3 import read_csv_from_s3
from src.mongodb.insert_data import insert_into_mongodb
bucket_name = "beeru-bucket"
file_key = "incoming/emp.csv"

mongo_uri = "mongodb://localhost:27017"
db_name = "company"
collection_name = "employees"

# Step 1: Read CSV from S3
df = read_csv_from_s3(bucket_name, file_key)

print(df.head())

# Step 2: Insert into MongoDB
# insert_into_mongodb(df, mongo_uri, db_name, collection_name)


