class Array:
    # dynamic array (python)
    def __init__(self, list):
        self._list = list

    # access - Θ(1)
    def access(self, index):
        return self._list[index]

    # search - Θ(n)
    def search(self, value):
        for i in range(len(self._list)):
            if self._list[i] == value:
                return i

    # insert - Θ(n) - until index + swap rest
    def insert(self, index, value):
        self._list.insert(index, value)

    # delete - Θ(n) - until index + swap rest
    def delete(self, index):
        del self._list[index]

    # print - 0(n)
    def __str__(self):
        return str(self._list)


# dynamic arrays solve memory limit problem by copying
# over the entire initial array to a new memory space,
# so append takes 0(n) but this is worst-case scenario,
# on best and average cases it only takes 0(1) time.
