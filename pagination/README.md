# Pagination

This project explores different pagination strategies for datasets using Python.

## Learning Objectives

- How to paginate a dataset with simple `page` and `page_size` parameters
- How to paginate a dataset with hypermedia metadata (HATEOAS)
- How to paginate in a deletion-resilient manner

## Files

| File | Description |
|------|-------------|
| `0-simple_helper_function.py` | Simple helper that returns start/end index for a given page |
| `1-simple_pagination.py` | Paginate a dataset with `page` and `page_size` parameters |
| `2-hypermedia_pagination.py` | Paginate with hypermedia metadata |
| `3-hypermedia_del_pagination.py` | Deletion-resilient hypermedia pagination |

## Setup

Place `Popular_Baby_Names.csv` in the project root directory.

## Requirements

- Python 3.9
- Ubuntu 20.04 LTS
- pycodestyle 2.5.*
