#!/usr/bin/env python3
"""Script designed to handle pagination for a dataset"""

import csv
import math
from typing import List
from typing import Tuple


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
        print(len(x))


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
