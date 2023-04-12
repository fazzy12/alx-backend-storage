#!/usr/bin/env python3
# """15. Log stats - new version"""

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

    
#     data = collection.aggregate([
#             { "$group": { "_id": "$ip", "count": { "$sum": 1 } } },
#             { "$sort": { "count": -1 } },
#             { "$limit": 10 }
#         ])

#     print("IPs:")
#     for row in data:
#         print(f"\t{row.get('_id')}: {row.get('count')}")


"""12. Log stats"""

from pymongo import MongoClient
from collections import Counter

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx
    count = collection.count_documents({})

    print(f'{count} logs')
    print('Methods:')
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        count = collection.count_documents({'method': method})
        print(f'\tmethod {method}: {count}')
    count = collection.count_documents({'method': 'GET', 'path': '/status'})
    print(f'{count} status check')

    # Get top 10 most present IPs
    ip_counter = Counter(doc['ip'] for doc in collection.find())
    print('IPs:')
    for ip, count in ip_counter.most_common(10):
        print(f'\t{ip}: {count}')
