from pymongo.mongo_client import MongoClient
import pandas as pd
import json

# from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://arkaofficial13:arkaofficial13@cluster0.cusn9p9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# Create a new client and connect to the server
client = MongoClient(uri)


# create database name and collection name
DATABASE_NAME="Wafer fault prediction"
COLLECTION_NAME="waferfault"

# read the data as a dataframe
df=pd.read_csv(r"D:/ML_projects/wafer_fault_prediction/Wafer_fault_prediction/notebook/wafer_23012020_041211.csv")
df=df.drop("Unnamed: 0",axis=1)

# Convert the data into json
json_record=list(json.loads(df.T.to_json()).values())

#now dump the data into the database
client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)