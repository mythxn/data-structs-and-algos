# 2D array data is stored contiguously, i.e the next
# item is stored in the next index but in a hash table
# the index is calculated using a hash function. this
# allows for string based indexing as well

# arr[get_hash(key)] = value


class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for _ in range(self.MAX)]

    # using ascii values
    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    # 0(1)
    def __setitem__(self, key, val):
        hash_val = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[hash_val]):
            if len(element) == 2 and element[0] == key:
                self.arr[hash_val][idx] = (key, val)
                found = True
        if not found:
            self.arr[hash_val].append((key, val))

    # 0(1)
    def __getitem__(self, key):
        hash_val = self.get_hash(key)
        for element in self.arr[hash_val]:
            if element[0] == key:
                return element[1]

    # 0(1)
    def __delitem__(self, key):
        hash_val = self.get_hash(key)
        for idx, element in enumerate(self.arr[hash_val]):
            if element[0] == key:
                del self.arr[hash_val][idx]
