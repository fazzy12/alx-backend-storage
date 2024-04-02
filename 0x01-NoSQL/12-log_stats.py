#!/usr/bin/env python3
""" script that provides some stats about Nginx logs stored in MongoDB:
"""

from pymongo import MongoClient

def log_stats(mongo_collection):
    """Total number of documents in the collection
    """
    total_logs = mongo_collection.count_documents({})

    # Count of each method type
    method_counts = {}
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        method_counts[method] = mongo_collection.count_documents(
            {"method": method})

    # Number of documents with method=GET and path=/status
    status_check_count = mongo_collection.count_documents(
        {"method": "GET", "path": "/status"})

    # Printing the results
    print(f"{total_logs} logs")
    print("Methods:")
    for method, count in method_counts.items():
        print(f"    method {method}: {count}")
    print(f"{status_check_count} status check")

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    collection = db.nginx
    log_stats(collection)
