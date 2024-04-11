#!/usr/bin/python3
"""LIFO Caching"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """Creating a class"""
    def __init__(self):
        super().__init__()
        self.history = []

    def put(self, key, item):
        """To assign to the dictionary
            self.cache_data the item value for the key key
        """
        if not (key is None or item is None):
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS\
                    and key not in self.cache_data:
                print(f'DISCARD: {self.history[-1]}')
                self.cache_data.pop(self.history[-1])
                del self.history[-1]
            if key in self.history:
                del self.history[self.history.index(key)]
            self.history.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """To return the value in self.cache_data linked to key.
        """
        if key is None or not (key in self.cache_data):
            return None
        return self.cache_data[key]
