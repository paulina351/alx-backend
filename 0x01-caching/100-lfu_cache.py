#!/usr/bin/python3
"""LFU Caching"""


from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """Creating a a class LFUCache that
        inherits from BaseCaching and is a caching system:
    """
    def __init__(self):
        """Initializing the class"""
        super().__init__()
        self.history = []
        self.frequency = {}

    def put(self, key, item):
        """To assign to the dictionary
            self.cache_data the item value for the key key.
        """
        if key is None or item is None:
            pass
        else:
            length = len(self.cache_data)
            if length >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                lfu = min(self.frequency.values())
                lfu_keys = []
                for k, v in self.frequency.items():
                    if v == lfu:
                        lfu_keys.append(k)
                if len(lfu_keys) > 1:
                    lru_lfu = {}
                    for k in lfu_keys:
                        lru_lfu[k] = self.history.index(k)
                    discard = min(lru_lfu.values())
                    discard = self.history[discard]
                else:
                    discard = lfu_keys[0]

                print("DISCARD: {}".format(discard))
                del self.cache_data[discard]
                del self.history[self.history.index(discard)]
                del self.frequency[discard]
            if key in self.frequency:
                self.frequency[key] += 1
            else:
                self.frequency[key] = 1
            if key in self.history:
                del self.history[self.history.index(key)]
            self.history.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """To return the value in self.cache_data linked to key.
        """
        if key is not None and key in self.cache_data.keys():
            del self.history[self.history.index(key)]
            self.history.append(key)
            self.frequency[key] += 1
            return self.cache_data[key]
        return None
