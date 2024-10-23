#!/usr/bin/env python3
"""
Module contains Python function that inserts
a new document in a collection based on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """
    Python function that inserts a new document in
    a collection based on kwargs
    """
    result = mongo_collection.insert({**kwargs})
    id = result.insertedId
    return id
