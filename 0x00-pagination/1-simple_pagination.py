#!/usr/bin/env python3
"""simple pagination"""

import csv
import math
from typing import List


def idx_range(page: int, page_size: int) -> tuple:
    """Use index_range to find the correct indexes to
        paginate the dataset correctly and return the appropriate
    """
    begin = (page - 1) * page_size
    return (begin, begin + page_size)


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
        """A method named get_page that takes two integer arguments
            page with default value 1 and page_size with default value 10.
        """
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        begin, end = idx_range(page, page_size)
        dataset = self.dataset()
        return [] if (begin >= len(dataset) or
                      end >= len(dataset)) else dataset[begin:end]
