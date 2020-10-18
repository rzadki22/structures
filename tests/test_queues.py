from unittest import TestCase, main

from structures.queues import Stack

class TestStack(TestCase):

    def test_init_without_elements(self):
        stack = Stack[int]()
        self.assertIsNone(stack.top)

    def test_front_EmptyStackError(self):
        stack = Stack[int]()
        with self.assertRaises(Stack.EmptyStackError):
            stack.front()

    def test_push_one_value(self):
        stack = Stack[int]()
        stack.push(1)
        self.assertEqual(stack.front(), 1)

    def test_push_two_values(self):
        stack = Stack[int]()
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.front(), 2)

    def test_pop_one_value(self):
        stack = Stack[int]()
        stack.push(1)
        stack.push(2)
        stack.pop()
        self.assertEqual(stack.front(), 1)

if __name__ == "__main__":
    main()