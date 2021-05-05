import MyDoublyLinkedList as DoubleLL


class MyDeque:
    def __init__(self):
        self.__leftmost = None
        self.__rightmost = None
        self.__size = 0

    def is_empty(self):
        """

        :return: boolean
        """

        return self.__size == 0

    def size(self):
        return self.__size

    def push_left(self, data):
        node = DoubleLL.Node(data)
        if self.__size == 0:
            self.__leftmost = self.__rightmost = node
        else:
            node.right = self.__leftmost
            self.__leftmost = node
        self.__size += 1

    def push_right(self, data):
        node = DoubleLL.Node(data)
        if self.__size == 0:
            self.__rightmost = self.__leftmost = node
        else:
            node.left = self.__rightmost
            self.__rightmost = node
        self.__size += 1

    def pop_left(self):
        if self.__size == 0:
            return None

        node = self.__leftmost
        self.__leftmost = node.right
        self.__size -= 1
        return node.data

    def pop_right(self):
        if self.__size == 0:
            return None

        node = self.__rightmost
        self.__rightmost = node.left
        self.__size -= 1
        return node.data
