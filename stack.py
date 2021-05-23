# last in, first out

# access & searching takes 0(n) time
# due to lack of indexing

from collections import deque


class Stack:
    def __init__(self):
        self.container = deque()

    # 0(1)
    def push(self, data):
        self.container.append(data)

    # 0(1)
    def pop(self):
        return self.container.pop()

    # 0(1)
    def peek(self):
        return self.container[-1]

    def size(self):
        return len(self.container)

    def is_empty(self):
        return not bool(self.size())

    def __str__(self):
        return self.container.__str__()
