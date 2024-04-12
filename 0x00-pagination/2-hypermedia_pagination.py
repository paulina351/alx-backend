#!/usr/bin/env python3
"""Hypermedia pagination"""

import csv
from math import ceil
from typing import List


def idx_range(page: int, page_size: int) -> tuple:
    """Implement a get_hyper method that takes the same arguments
        (and defaults) as get_page and returns a dictionary containing
        the following key-value pairs:
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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Returning an hypermedia"""
        page_data = self.get_page(page, page_size)
        total_pages = ceil(len(self.dataset()) / page_size)
        next_page = page + 1 if page + 1 < total_pages else None
        prev_page = page - 1 if page - 1 > 1 else None

        return {
            "page_size": len(page_data),
            "page": page,
            "data": page_data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
