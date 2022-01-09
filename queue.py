"""
Queue Abstract Data Type
* Queue() creates a new queue that is empty.
  It needs no parameters and returns an empty queue.
* enqueue(item) adds a new item to the rear of the queue.
  It needs the item and returns nothing.
* dequeue() removes the front item from the queue.
  It needs no parameters and returns the item. The queue is modified.
* is_empty() tests to see whether the queue is empty.
  It needs no parameters and returns a boolean value.
* peek() returns the front element of the queue.
"""


class Queue():
    def __init__(self, capacity=10):
        """
        Initialize python List with capacity of 10 or user given input.
        Python List type is a dynamic array, so we have to restrict its
        dynamic nature to make it work like a static array.
        """
        self._array = [None] * capacity
        self._front = 0
        self._rear = 0
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def enqueue(self, value):
        if self._rear == len(self._array):
            self._expand()
        self._array[self._rear] = value
        self._rear += 1
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError('queue is empty')
        value = self._array[self._front]
        self._array[self._front] = None
        self._front += 1
        self._size -= 1
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError('queue is empty')
        return self._array[self._front]

    def _expand(self):
        self._array += [None] * len(self._array)

    def __iter__(self):
        probe = self._front
        while True:
            if probe == self._rear:
                return
            yield self._array[probe]
            probe += 1
