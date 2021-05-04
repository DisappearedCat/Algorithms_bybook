import unittest
import FixedCapacityStackOfString
import MyStack
import MyStackQueue


class TestFixedCapacityStackOfString(unittest.TestCase):
    def test(self):
        stack = FixedCapacityStackOfString.FixedCapacityStackOfString(10)
        self.assertEqual(stack.is_empty(), True)

        string = "AAA"
        stack.push(string)
        self.assertEqual(stack.is_empty(), False)
        self.assertEqual(stack.size(), 1)

        test_string = stack.pop()
        self.assertEqual(test_string, string)
        self.assertEqual(stack.is_empty(), True)

        for i in range(10):
            stack.push("A")

        self.assertEqual(stack.is_full(), True)


class TestMyStack(unittest.TestCase):
    def test(self):
        stack = MyStack.MyStack()
        self.assertEqual(stack.is_empty(), True)

        string = "AAA"
        stack.push(string)
        self.assertEqual(stack.is_empty(), False)
        self.assertEqual(stack.size(), 1)

        test_string = stack.pop()
        self.assertEqual(test_string, string)
        self.assertEqual(stack.is_empty(), True)

        for i in range(10):
            stack.push("A")
        ch = stack.peek()
        self.assertEqual(ch, "A")
        self.assertEqual(stack.size(), 10)


class TestMyStackQueue(unittest.TestCase):
    def test(self):
        sq = MyStackQueue.MyStackQueue(1)

        sq.push(2)
        sq.push(3)

        pop = sq.pop()
        pop2 = sq.pop()
        self.assertEqual(pop, 1)
        self.assertEqual(pop2, 2)

        sq = MyStackQueue.MyStackQueue(1)
        sq.push(2)
        sq.push(3)
        sq.insert(2.5, 2)
        sq.insert(4, sq.size)
        sq.insert(0, 0)

        test_list = [0, 1, 2, 2.5, 3, 4]
        for i in test_list:
            pop = sq.pop()
            self.assertEqual(pop, i)


if __name__ == '__main__':
    unittest.main()
