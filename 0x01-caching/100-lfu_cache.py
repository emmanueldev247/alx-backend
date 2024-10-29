#!/usr/bin/python3
""" LFU caching """

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """Class that inherits from BaseCaching and is an LFU caching system

    This cache evicts the least frequently used items when it reaches its
    capacity. If multiple items share the same frequency count, the item
    that has been in the cache the longest (Least Recently Used) will be
    removed first.
    """
    def __init__(self):
        """Initializes the LRUCache instance.

        - Calls the parent class's constructor to initialize the `cache_data`
          dictionary.
        - Initializes `key_freq`, a dictionary to track the access frequency
          of each key.
        - Initializes `key_list` to maintain the order of access for keys,
          which helps in applying LRU when there’s a frequency tie.
        """
        super().__init__()
        self.key_freq = {}
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
            `BaseCaching.MAX_ITEMS`, the item with the lowest frequency is
            evicted.

        -   In case of a tie in frequency counts, the Least Recently Used (LRU)
            item among them is removed.

        -   If the `key` already exists, its frequency is incremented, and its
            position in `key_list` is updated to reflect recent access.
        """
        if key and item:
            if key in self.cache_data:
                self.key_list.remove(key)
                self.key_freq[key] += 1
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS and \
                                          key not in self.cache_data:
                    self.evict()
                self.key_freq[key] = 1

            self.key_list.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves an item from the cache.

        Args:
            key (str): The key of the item to retrieve.

        Returns:
            The value associated with the key if found, otherwise None.

        - If `key` exists, its frequency count is incremented.
        - The key is moved to the end of `key_list` to update its LRU status.
        """
        if key and key in self.cache_data:
            self.key_list.remove(key)
            self.key_list.append(key)
            self.key_freq[key] += 1
            return self.cache_data[key]
        return None

    def evict(self):
        """Evicts the least frequently used item from the cache.

        - Finds the minimum frequency among all items and identifies the keys
          with that frequency.
        - If only one item has the lowest frequency, it is removed.
        - If multiple items share the lowest frequency, the Least Recently Used
          (LRU) item among them is discarded.
        """
        min_freq = min(self.key_freq.values())
        probation_list = []
        for key, value in self.key_freq.items():
            if value == min_freq:
                probation_list.append(key)
        if len(probation_list) == 1:
            del_key = probation_list[0]
        else:
            for key in self.key_list:
                if key in probation_list:
                    del_key = key
                    break

        del self.cache_data[del_key]
        del self.key_freq[del_key]
        self.key_list.remove(del_key)
        print(f'DISCARD: {del_key}')
