#!/usr/bin/python3
"""Basic dictionary"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """Basic"""
    def put(self, key, item):
        """put an item in the key"""
        if not (key is None or item is None):
                self.cache_data[key] = item

    def get(self, key):
        """return an item by get"""
        if key is None or not (key in self.cache_data):
            return None
        return self.cache_data[key]
