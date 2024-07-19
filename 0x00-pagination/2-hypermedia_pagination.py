#!/usr/bin/env python3
"""get page"""
import csv
from typing import List, Tuple, Dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """return a tuple of size two containing a start index and an end index"""
    start_idx = (page - 1) * page_size
    end_idx = page * page_size
    return (start_idx, end_idx)


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
        """ get data from page"""
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0

        data = self.dataset()
        try:
            idx = index_range(page, page_size)
            return data[idx[0]:idx[1]]
        except IndexError:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        return a dictionary containing:
            page_size: the length of the returned dataset page
            page: the current page number
            data: the dataset page (equivalent to return from previous task)
            next_page: number of the next page, None if no next page
            prev_page: number of the previous page, None if no previous page
            total_pages: the total number of pages in the dataset as an integer
        """
        total_pages = (len(self.dataset()) + page_size - 1) // page_size
        data = self.get_page(page, page_size)

        if total_pages > page:
            next_page = page + 1
        else:
            next_page = None
        if page == 1:
            prev_page = None
        else:
            prev_page = page - 1
        return {
            "page_size": len(data),
            "page": page,
            "data": self.get_page(page, page_size),
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": (len(self.dataset()) + page_size - 1) // page_size
        }
