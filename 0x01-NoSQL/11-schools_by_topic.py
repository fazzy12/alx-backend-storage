#!/usr/bin/env python3
"""Implemented Python function schools_by_topic to
return the list of schools having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    Args:
        mongo_collection: pymongo collection object.
        topic (str): The topic to search for.

    Returns:
        A list of school documents that cover the topic.
    """
    documents = mongo_collection.find({'topics': topic})
    return list(documents) if documents else []
