#!/usr/bin/env python3
"""Module for deletion-resilient hypermedia pagination for baby names."""
import csv
from typing import Dict, List, Optional


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize Server with None caches for dataset and indexed data."""
        self.__dataset = None
        self.__indexed_dataset = None

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

    def indexed_dataset(self) -> Dict[int, List]:
        """Return the dataset indexed by position, starting at 0.

        Returns:
            A dictionary mapping each original row index to its data row,
            allowing stable pagination even when rows are removed.
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Return a deletion-resilient page of data from a given index.

        This method ensures that if rows are deleted between requests, the
        client will not miss any records by using stable index-based cursors
        rather than page numbers.

        Args:
            index: The starting index of the current page (must be valid).
            page_size: The number of items to return per page.

        Returns:
            A dictionary containing:
                - index: the start index of the current page
                - next_index: the index to use for the next page request
                - page_size: the number of items returned
                - data: the list of rows for this page
        """
        dataset = self.indexed_dataset()
        total = len(dataset)

        assert isinstance(index, int) and 0 <= index < total, \
            "index must be a valid integer within the dataset range"

        data = []
        current = index
        collected = 0

        while collected < page_size and current < total:
            if current in dataset:
                data.append(dataset[current])
                collected += 1
            current += 1

        return {
            "index": index,
            "next_index": current,
            "page_size": len(data),
            "data": data,
        }
