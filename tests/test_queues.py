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


    # def test_length_one_element_in_list(self):
    #     values = LinkedList[int]()
    #     values.head = LinkedList.Node[int](9)
    #     self.assertEqual(values.length(), 1)
    #     self.assertEqual(1, len(values))
    #
    # def test_length_many_elements_in_list(self):
    #     values = LinkedList[int]()
    #     values.head = LinkedList.Node[int](9, LinkedList.Node[int](5, LinkedList.Node[int](1)) )
    #     self.assertEqual(values.length(), 3)
    #     self.assertEqual(3, len(values))
    #
    # def test_str_empty_list(self):
    #     values = LinkedList[int]()
    #     self.assertEqual(str(values), '[]')
    #
    # def test_str_one_element_in_list(self):
    #     values = LinkedList[int]()
    #     values.head = LinkedList.Node[int](9)
    #     self.assertEqual(str(values), '[9]')


if __name__ == "__main__":
    main()