import unittest
import FixedCapacityStackOfString


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


if __name__ == '__main__':
    unittest.main()
