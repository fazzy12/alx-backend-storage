#!/usr/bin/env python3
"""12. Log stats"""

# from pymongo import MongoClient

# if __name__ == "__main__":
#     client = MongoClient('mongodb://127.0.0.1:27017')
#     collection = client.logs.nginx
#     count = collection.count_documents({})

#     print(f'{count} logs')
#     print('Methods:')
#     for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
#         count = collection.count_documents({'method': method})
#         print(f'\tmethod {method}: {count}')
#     count = collection.count_documents({'method': 'GET', 'path': '/status'})
#     print(f'{count} status check')
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient()
db = client.logs
collection = db.nginx

# Get total number of documents in collection
total_logs = collection.count_documents({})

# Get counts for each method
methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
method_counts = {method: collection.count_documents(
    {"method": method}) for method in methods}

# Get count for status check
status_check_count = collection.count_documents(
    {"method": "GET", "path": "/status"})

# Display stats
print(f"{total_logs} logs")
print("Methods:")
for method, count in method_counts.items():
    print(f"\tmethod {method}: {count}")
print(f"{status_check_count} status check")