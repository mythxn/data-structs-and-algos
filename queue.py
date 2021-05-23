# a queue is exactly same as stack except
# stacks are lifo, but queue is fifo
# first in, first out

from collections import deque


class Queue:
    def __init__(self):
        self.buffer = deque()

    # 0(1)
    def enqueue(self, data):
        self.buffer.appendleft(data)

    # 0(1)
    def dequeue(self):
        return self.buffer.pop()

    def size(self):
        return len(self.container)

    def is_empty(self):
        return not bool(self.size())

    def __str__(self):
        return self.buffer.__str__()
