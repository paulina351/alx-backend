#!/usr/bin/env python3
"""Simple helper function"""


def index_range(page: int,  page_size: int) -> tuple:
    """a function named index_range that takes two
        integer arguments page and page_size.
    """
    begin = (page - 1) * page_size
    return (begin, begin + page_size)
