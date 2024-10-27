#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import Dict, List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Retrieve a paginated dataset starting from a specified index
        and return additional pagination metadata.

        Args:
            index (int): starting index for the current page in the dataset.
                        Defaults to None.
            page_size (int): The number of items per page. Defaults to 10.

        Returns:
            Dict: A dictionary containing:
                - index (int): The starting index of the current page.
                - next_index (int): The starting index for the next page.
                - page_size (int): The number of items on the current page.
                - data (List): A list of dataset items for the current page.
        """
        indexed_dataset = self.__indexed_dataset
        assert index >= 0 and index < len(indexed_dataset) - 1
        assert page_size > 0

        data = []
        stop_index = index + page_size
        next_index = index
        i = index

        while i < stop_index:
            row = indexed_dataset.get(i)
            if row:
                data.append(row)
            else:
                stop_index += 1
            next_index += 1
            i += 1

        return {
            "index": index,
            "next_index": next_index,
            "page_size": page_size,
            "data": data
        }
