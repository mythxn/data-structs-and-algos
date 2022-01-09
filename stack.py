"""
Stack Data Type
Stack() creates a new stack that is empty.
   It needs no parameters and returns an empty stack.
push(item) adds a new item to the top of the stack.
   It needs the item and returns nothing.
pop() removes the top item from the stack.
   It needs no parameters and returns the item. The stack is modified.
peek() returns the top item from the stack but does not remove it.
   It needs no parameters. The stack is not modified.
is_empty() tests to see whether the stack is empty.
   It needs no parameters and returns a boolean value.
"""


class Stack:
    def __init__(self, size=10):
        """
        Initialize python List with size of 10 or user given input.
        Python List type is a dynamic array, so we have to restrict its
        dynamic nature to make it work like a static array.
        """
        self._top = -1
        self._array = [None] * size

    def __len__(self):
        return self._top + 1

    def __str__(self):
        result = " ".join(map(str, self))
        return 'Top-> ' + result

    def is_empty(self):
        return self._top == -1

    def __iter__(self):
        probe = self._top
        while True:
            if probe == -1:
                return
            yield self._array[probe]
            probe -= 1

    def push(self, value):
        self._top += 1
        if self._top == len(self._array):
            self._expand()
        self._array[self._top] = value

    def pop(self):
        if self.is_empty():
            raise IndexError("stack is empty")
        value = self._array[self._top]
        self._top -= 1
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("stack is empty")
        return self._array[self._top]

    def _expand(self):
        self._array += [None] * len(self._array)  # double the size of the array
