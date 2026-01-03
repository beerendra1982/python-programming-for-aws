from pymongo import MongoClient
import pandas as pd

def insert_into_mongodb(df, mongo_uri, db_name, collection_name):
    try:
        # Convert DataFrame to JSON-safe Python types
        df = df.where(pd.notnull(df), None)

        records = df.to_dict(orient="records")

        client = MongoClient(mongo_uri)
        db = client[db_name]
        collection = db[collection_name]

        result = collection.insert_many(records)
        print(f"Inserted {len(result.inserted_ids)} records")

    except Exception as e:
        print("Error inserting into MongoDB:", e)
        raise
