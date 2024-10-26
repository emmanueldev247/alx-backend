#!/usr/bin/env python3
"""Write a function named index_range that
    takes two integer arguments page and page_size
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
        Calculate the start and end index for pagination based on
        the given page number and page size.

        Args:
            page (int): The current page number (1-based index).
            page_size (int): The number of items per page.

        Returns:
            Tuple[int, int]: A tuple containing the start index and end index
                         representing the range of items for the given page.
    """

    offset = (page - 1) * page_size
    return offset, offset + page_size
