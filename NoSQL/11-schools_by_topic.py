#!/usr/bin/env python3
"""Module that provides a function to find schools by a specific topic."""
from typing import List


def schools_by_topic(mongo_collection, topic: str) -> List:
    """Return a list of schools that include the specified topic.

    Args:
        mongo_collection: A PyMongo collection object to query.
        topic: The topic string to search for in the topics field.

    Returns:
        A list of school documents that have the given topic in their
        topics field.
    """
    return list(mongo_collection.find({"topics": topic}))
