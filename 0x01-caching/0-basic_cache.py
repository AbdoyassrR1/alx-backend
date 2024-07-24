#!/usr/bin/env python3
""" BaseCaching module """
BaseCaching = __import__('BaseCaching').BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache """
    def __init__(self):
        """Initiliazef"""
        super().__init__()
        self.cache_data = {}

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
