#!/usr/bin/env python3
"""
Basecaching
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Caching key and value pairs
    Methods:
        put(self, key, item) which asigns to dictionary
        self.cache_data the value of the key
        If key or item is none the method should do anything
        get(self, key) Must return the value in
        self.cache_data linked to key
        if key is none or if the key doesnt exist return None
    """

    def __init__(self):
        """
        iinitializing the class using the parent class
        """
        BaseCaching.__init__(self)

    def put(self, key, item):
        """
        assigning to self.cache_data value for the key
        Args:
            key
            item
        """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """
        Return the value in self.cache_data linked to key
        if key is none or if it doesnt exist in cache pass
        """
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
