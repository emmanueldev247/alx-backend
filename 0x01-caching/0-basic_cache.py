#!/usr/bin/python3
""" Basic dictionary """

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """Class that inherits from BaseCaching and is a Basic caching system"""
    def __init__(self):
        """Initializes the BasicCache instance.
            Calls the parent class's constructor to initialize
            the `cache_data` dictionary.
        """
        super().__init__()

    def put(self, key, item):
        """
        Stores an item in the cache.

        Args:
            key (str): The key to identify the item.
            item (any): The item to be stored.

        If both `key` and `item` are provided,
        the item is added to the cache dictionary.
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves an item from the cache.

        Args:
            key (str): The key of the item to retrieve.

        Returns:
            The value associated with the key if found, otherwise None.
        """
        if key and key in self.cache_data:
            return self.cache_data[key]
        return None
