#!/usr/bin/env python3
""" FIFO module """
from collections import deque
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ FIFO cache """
    def __init__(self):
        """ Initiliaze """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            pass
        if len(self.cache_data) == BaseCaching.MAX_ITEMS\
                and key not in self.cache_data.keys():
            keys = deque(self.cache_data.keys())
            discarded = keys.popleft()
            del self.cache_data[discarded]
            print(f"DISCARD: {discarded}")
            self.cache_data[key] = item
        else:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
