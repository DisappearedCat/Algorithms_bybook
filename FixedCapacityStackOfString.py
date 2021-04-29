class FixedCapacityStackOfString:
    __items = []  # Items of Stack
    __size = 0

    def __init__(self, cap):
        items = [None] * 10

    def is_empty(self):
        return self.__size == 0

    def is_full(self):
        return len(self.__items) == self.__size

    def size(self):
        return self.__size

    def push(self, string):
        self.__items[self.__size] = string
        self.__size += 1

    def pop(self):
        self.__size -= 1
        return self.__items[self.__size]
