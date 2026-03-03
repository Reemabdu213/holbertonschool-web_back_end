#!/usr/bin/env python3
"""Module providing a helper function for pagination index calculation."""
from typing import Tuple


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
