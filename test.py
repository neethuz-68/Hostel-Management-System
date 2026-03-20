from pymongo import MongoClient

client = MongoClient("mongodb+srv://hostel_user:<passwd>@cluster0.ogxovkm.mongodb.net/?appName=Cluster0")
db = client["hostel_management"]

print("Connected successfully!")