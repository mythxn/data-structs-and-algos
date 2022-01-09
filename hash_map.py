"""
    HashMap Data Type
    HashMap() Create a new, empty map. It returns an empty map collection.
    put(key, val) Add a new key-value pair to the map. If the key is already in the map then replace
                    the old value with the new value.
    get(key) Given a key, return the value stored in the map or None otherwise.
    del_(key) or del map[key] Delete the key-value pair from the map using a statement of the form del map[key].
    len() Return the number of key-value pairs stored in the map.
    in Return True for a statement of the form key in map, if the given key is in the map, False otherwise.
    """


class HashMap(object):
    _empty = object()
    _deleted = object()

    def __init__(self, size=11):
        self.size = size
        self._len = 0
        self._keys = [self._empty] * size
        self._values = [self._empty] * size

    def __getitem__(self, key):
        return self.get(key)

    def __delitem__(self, key):
        return self.del_(key)

    def __setitem__(self, key, value):
        self.put(key, value)

    def __len__(self):
        return self._len

    def hash(self, key):
        return key % self.size

    def _rehash(self, old_hash):
        # linear probing
        return (old_hash + 1) % self.size

    def put(self, key, value):
        initial_hash = hash_ = self.hash(key)

        while True:
            if self._keys[hash_] is self._empty or self._keys[hash_] is self._deleted:
                # not in map yet, or deleted; can assign key:value
                self._keys[hash_] = key
                self._values[hash_] = value
                self._len += 1
                return

            elif self._keys[hash_] == key:
                # key already exists here, assign over
                self._keys[hash_] = key
                self._values[hash_] = value
                return

            hash_ = self._rehash(hash_)
            if initial_hash == hash_:
                # table is full and wrapped around
                return None

    def get(self, key):
        initial_hash = hash_ = self.hash(key)

        while True:
            if self._keys[hash_] is self._empty:
                # that key was never assigned
                return None
            elif self._keys[hash_] == key:
                return self._values[hash_]

            hash_ = self._rehash(hash_)
            if initial_hash == hash_:
                # table is full and wrapped around
                return None

    def del_(self, key):
        initial_hash = hash_ = self.hash(key)

        while True:
            if self._keys[hash_] is self._empty:
                # that key was never assigned
                return None
            elif self._keys[hash_] == key:
                # key found, assign with deleted sentinel
                self._keys[hash_] = self._deleted
                self._values[hash_] = self._deleted
                self._len -= 1
                return

            hash_ = self._rehash(hash_)
            if initial_hash == hash_:
                # table is full and wrapped around
                return None
