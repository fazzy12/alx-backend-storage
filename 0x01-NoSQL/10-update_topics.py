#!/usr/bin/env python3
"""
    Update topics of a school document based on the name.
"""

def update_topics(mongo_collection, name, topics):
    """
    Args:
        mongo_collection: pymongo collection object.
        name (str): The school name to update.
        topics (list of str): The list of topics approached in the school.

    Returns:
        None
    """
    # Update documents matching the name
    mongo_collection.update_many({'name': name}, {'$set': {'topics': topics}})
