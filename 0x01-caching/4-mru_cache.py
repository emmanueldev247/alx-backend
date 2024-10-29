#!/usr/bin/python3
""" MRU caching """

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """Class that inherits from BaseCaching and is an MRU caching system"""
    def __init__(self):
        """Initializes the LRUCache instance.
            Calls the parent class's constructor to initialize the
            `cache_data` dictionary and initializes an additional list
            `key_list` to keep track of the order of keys for MRU eviction.
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

        -   If adding a new item exceeds the cache limit defined in
            `BaseCaching.MAX_ITEMS`, the most recently used (LRU) item
            is removed.

        -   If the `key` already exists, it removes the key from
            its current position in `key_list` before re-adding it
            to the end, updating the cache's MRU order.
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

        -  If the `key` exists, it removes the key from its current position in
          `key_list` and re-adds it to the end, updating the MRU order.
        """
        if key and key in self.cache_data:
            self.key_list.remove(key)
            self.key_list.append(key)
            return self.cache_data[key]
        return None

    def evict(self):
        """Evicts the most recently used item from the cache."""

        del_key = self.key_list.pop()
        del self.cache_data[del_key]
        print(f'DISCARD: {del_key}')
