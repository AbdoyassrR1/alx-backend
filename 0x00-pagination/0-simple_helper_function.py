#!/usr/bin/env python3
"""return a tuple of size two containing a start index and an end index"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """return a tuple of size two containing a start index and an end index"""
    start_idx = (page - 1) * page_size
    end_idx = page * page_size
    return (start_idx, end_idx)
