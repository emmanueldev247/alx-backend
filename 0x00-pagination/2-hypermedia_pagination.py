#!/usr/bin/env python3
"""Script designed to handle pagination for a dataset"""

import csv
import math
from typing import Any, Dict, List, Tuple


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieve a page of data from the dataset
        based on the page number and page size.

        Args:
            page (int): page number to retrieve (1-based index). Defaults to 1.
            page_size (int): number of items per page. Defaults to 10.

        Returns:
            List[List]: A list of rows representing the requested page of data.
                        Each row is a list of values, corresponding
                        to a single record in the dataset.

        Raises:
            AssertionError: If `page` or `page_size` is not a positive integer.
    """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        my_range = index_range(page, page_size)
        data = self.dataset()
        return data[my_range[0]: my_range[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """
        Retrieve a paginated dataset along with additional information.

        Args:
            page (int): page number to retrieve (1-based index). Defaults to 1.
            page_size (int): number of items per page. Defaults to 10.

        Returns:
            Dict[str, Any]: A dictionary with pagination details, containing:
                - page_size (int): The length of the current dataset page.
                - page (int): The current page number.
                - data (List[List]): The dataset page as a list of records.
                - next_page (Optional[int]): The number of the next page,
                                            or None if there is no next page.
                - prev_page (Optional[int]): The number of the previous page,
                                          or None if there is no previous page.
                - total_pages (int): The total number of pages in the dataset.
    """

        data = self.get_page(page, page_size)
        total_pages = (len(self.dataset()) + page_size - 1) // page_size
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            "page_size": page_size,
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }


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
