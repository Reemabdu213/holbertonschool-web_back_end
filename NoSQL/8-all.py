#!/usr/bin/env python3
"""Module that provides a function to list all documents in a collection."""


def list_all(mongo_collection):
    """List all documents in a MongoDB collection.

    Args:
        mongo_collection: A PyMongo collection object to query.

    Returns:
        A list of all documents in the collection, or an empty list
        if the collection contains no documents.
    """
    documents = list(mongo_collection.find())
    return documents if documents else []
