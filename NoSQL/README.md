# NoSQL

This project covers the fundamentals of NoSQL databases, specifically MongoDB,
including querying, inserting, updating, and deleting documents using both
the mongo shell and Python with PyMongo.

## Learning Objectives

- What NoSQL means
- Difference between SQL and NoSQL
- What is ACID
- What is document storage
- NoSQL types and benefits
- How to query, insert, update, and delete in MongoDB
- How to use MongoDB with Python (PyMongo)

## Requirements

- Ubuntu 20.04 LTS
- MongoDB 4.4
- Python 3.9
- PyMongo 4.8.0
- pycodestyle 2.5.*

## Files

### MongoDB Shell Scripts

| File | Description |
|------|-------------|
| `0-list_databases` | List all databases |
| `1-use_or_create_database` | Create or use database `my_db` |
| `2-insert` | Insert a document in collection `school` |
| `3-all` | List all documents in collection `school` |
| `4-match` | List documents with `name="Holberton school"` |
| `5-count` | Count documents in collection `school` |
| `6-update` | Add attribute `address` to matching documents |
| `7-delete` | Delete documents with `name="Holberton school"` |

### Python Scripts

| File | Description |
|------|-------------|
| `8-all.py` | List all documents in a collection |
| `9-insert_school.py` | Insert a new document in a collection |
| `10-update_topics.py` | Update topics of a school document |
| `11-schools_by_topic.py` | Return schools with a specific topic |
| `12-log_stats.py` | Print stats about Nginx logs in MongoDB |
