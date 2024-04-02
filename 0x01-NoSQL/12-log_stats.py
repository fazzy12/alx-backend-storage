#!/usr/bin/env python3
"""This script provides some stats about Nginx logs stored in MongoDB"""

import sys
from pymongo import MongoClient


def nginx_stats_check(db_name):
    """Provides some stats about Nginx logs stored in MongoDB"""
    try:
        client = MongoClient()
        db = client[db_name]
        collec_nginx = db.nginx

        num_of_docs = collec_nginx.count_documents({})
        print(f"{num_of_docs} logs")

        print("Methods:")
        methods_list = ["GET", "POST", "PUT", "PATCH", "DELETE"]
        for method in methods_list:
            method_count = collec_nginx.count_documents({"method": method})
            print(f"\tmethod {method}: {method_count}")

        status = collec_nginx.count_documents(
            {"method": "GET", "path": "/status"})
        print(f"{status} status check")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <database_name>")
        sys.exit(1)

    db_name = sys.argv[1]
    nginx_stats_check(db_name)
