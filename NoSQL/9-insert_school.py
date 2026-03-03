#!/usr/bin/env python3
"""Module that provides a function to insert a document in a collection."""


def insert_school(mongo_collection, **kwargs):
    """Insert a new document in a MongoDB collection using keyword arguments.

    Args:
        mongo_collection: A PyMongo collection object to insert into.
        **kwargs: Key-value pairs representing the document fields.

    Returns:
        The _id of the newly inserted document.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
