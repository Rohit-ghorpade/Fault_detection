
from pymongo.mongo_client import MongoClient
import pandas as pd
import json


# url
uri = "mongodb+srv://RG:dh9JJfyOtRGP38JM@cluster0.dfp1h.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# create a new client and connect to server
client = MongoClient(uri)


# create database name and collection name
DATABASE_NAME ='SensorDATA'
COLLECTION_NAME =  'wefer'

df = pd.read_csv('/content/wafer_23012020_041211.csv')

df.drop('Unnamed: 0',axis = 1, inplace = True)

json_record = list(json.loads(df.T.to_json()).values())


client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)