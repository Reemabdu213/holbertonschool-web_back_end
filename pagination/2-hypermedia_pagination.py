#!/usr/bin/env python3
"""Module for hypermedia pagination over a popular baby names dataset."""
import csv
import math
from typing import Dict, List, Optional, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return a tuple of start and end indexes for the given pagination params.

    Args:
        page: The current page number (1-indexed).
        page_size: The number of items per page.

    Returns:
        A tuple (start_index, end_index) representing the range of indexes
        to slice from a dataset for the requested page.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize Server with a None dataset cache."""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Return the cached dataset, loading from CSV file if not yet loaded.

        Returns:
            The full dataset as a list of rows (excluding the header).
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return the requested page of the dataset.

        Args:
            page: The page number to retrieve (must be a positive integer).
            page_size: The number of records per page (must be a positive int).

        Returns:
            A list of rows corresponding to the requested page, or an empty
            list if the page is out of range.
        """
        assert isinstance(page, int) and page > 0, \
            "page must be a positive integer"
        assert isinstance(page_size, int) and page_size > 0, \
            "page_size must be a positive integer"

        start, end = index_range(page, page_size)
        data = self.dataset()

        if start >= len(data):
            return []

        return data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Return a dictionary with hypermedia pagination metadata and data.

        Args:
            page: The page number to retrieve (must be a positive integer).
            page_size: The number of records per page (must be a positive int).

        Returns:
            A dictionary containing:
                - page_size: number of items on the current page
                - page: current page number
                - data: the list of rows for this page
                - next_page: next page number, or None if on the last page
                - prev_page: previous page number, or None if on the first page
                - total_pages: total number of pages in the dataset
        """
        data = self.get_page(page, page_size)
        total = len(self.dataset())
        total_pages = math.ceil(total / page_size)

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages,
        }
