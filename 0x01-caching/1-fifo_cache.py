#!/usr/bin/python3
""" FIFO caching """

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """Class that inherits from BaseCaching and is a FIFO caching system"""
    def __init__(self):
        """Initializes the FIFOCache instance.
            Calls the parent class's constructor to initialize
            the `cache_data` dictionary.
        """
        super().__init__()
        self.key_list = []

    def put(self, key, item):
        """
        Stores an item in the cache.

        Args:
            key (str): The key to identify the item.
            item (any): The item to be stored.

        -   If both `key` and `item` are provided,
            the item is added to the cache dictionary.

        -   If adding a new item exceeds the cache limit
            defined in `BaseCaching.MAX_ITEMS`, the oldest item in
            the cache is removed according to FIFO order.

        -   If the `key` already exists, it removes the key from
            its current position in `key_list` before re-adding it
            to the end, updating the cache's order for FIFO.
        """
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS and \
                                       key not in self.cache_data:
                self.evict()
            if key in self.cache_data:
                self.key_list.remove(key)
            self.key_list.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves an item from the cache.

        Args:
            key (str): The key of the item to retrieve.

        Returns:
            The value associated with the key if found, otherwise None.

        If the key does not exist in the cache, it returns `None`.
        """
        if key and key in self.cache_data:
            return self.cache_data[key]
        return None

    def evict(self):
        """Evicts the oldest item from the cache"""
        del_key = self.key_list.pop(0)
        del self.cache_data[del_key]
        print(f'DISCARD: {del_key}')
