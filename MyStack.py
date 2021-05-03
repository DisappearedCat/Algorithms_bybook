class MyStack:
    __items = []  # Items of Stack

    def is_empty(self):
        return len(self.__items) == 0

    def size(self):
        return len(self.__items)

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        return self.__items.pop()

    def peek(self):
        return self.__items[len(self.__items) - 1]