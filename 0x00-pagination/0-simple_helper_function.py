#!/usr/bin/env python3
"""#"""


def index_range(page: int,  page_size: int) -> tuple:
    """#"""
    begin = (page - 1) * page_size
    return (begin, begin + page_size)
