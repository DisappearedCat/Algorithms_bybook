import MyLinkedList


class MyStackQueue:
    def __init__(self, data):
        self.head = MyLinkedList.MyLinkedList(data)
        self.size = 1

    def push(self, data):
        """
        push data at the start of queue

        :param data:
        """

        new_last = MyLinkedList.MyLinkedList(data)
        last = self.__last_node()
        last.next = new_last
        self.size += 1

    def pop(self):
        """

        :return: first element or None if size == 0
        """
        if self.size == 0:
            return None

        new_first = self.head.next
        pop = self.head
        self.head = new_first
        self.size -= 1
        return pop.data

    def insert(self, data, k):
        """
        push data before elem k
        for k == size equivalent to push
        :param k:
        :param data:
        """
        if k == self.size:
            self.push(data)
        elif k == 0:
            new_first = MyLinkedList.MyLinkedList(data)
            new_first.next = self.head
            self.head = new_first
        else:
            node = self.head
            for i in range(k - 1):
                node = node.next

            # Need to insert data between node and node.next
            insert = MyLinkedList.MyLinkedList(data)
            insert.next = node.next
            node.next = insert

        self.size += 1

    def __last_node(self):
        node = self.head
        while node.next is not None:
            node = node.next
        return node
