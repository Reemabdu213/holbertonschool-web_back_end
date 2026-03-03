#!/usr/bin/env python3
"""Module that prints statistics about Nginx logs stored in MongoDB."""
from pymongo import MongoClient


def log_stats() -> None:
    """Print statistics about Nginx logs stored in the logs.nginx collection."""
    client = MongoClient("mongodb://127.0.0.1:27017")
    collection = client.logs.nginx

    total = collection.find().count()
    print(f"{total} logs")

    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.find({"method": method}).count()
        print(f"\tmethod {method}: {count}")

    status_count = collection.find(
        {"method": "GET", "path": "/status"}
    ).count()
    print(f"{status_count} status check")


if __name__ == "__main__":
    log_stats()
