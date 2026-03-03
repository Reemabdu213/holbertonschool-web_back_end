#!/usr/bin/env python3
"""Module that provides a function to update topics of a school document."""
from typing import List


def update_topics(mongo_collection, name: str, topics: List[str]) -> None:
    """Update the topics field of all documents matching the given school name.

    Args:
        mongo_collection: A PyMongo collection object to update.
        name: The name of the school to update.
        topics: A list of strings representing the new topics for the school.

    Returns:
        None
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
