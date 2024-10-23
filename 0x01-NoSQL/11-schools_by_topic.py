#!/usr/bin/env python3
"""
this module contains a Python function that
returns the list of school having a specific topic:
"""


def schools_by_topic(mongo_collection, topic):
    """
    Python function that
    returns the list of school having a specific topic:
    """
    mongo_collection.find({topic: "topic"})
