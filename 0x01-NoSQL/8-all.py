#!/usr/bin/env python3

def list_all(mongo_collection):
    """
    Lists all documents in a MongoDB collection.
    Args:
        mongo_collection: pymongo collection object.
    Returns:
        A list of all documents in the collection.
    """
    documents = mongo_collection.find()
    return list(documents) if documents else []
