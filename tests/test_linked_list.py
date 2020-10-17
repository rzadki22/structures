from unittest import TestCase, main

from structures.lists import LinkedList

class TestLinkedList(TestCase):
    def test_init_without_elements(self):
        values = LinkedList[int]()
        self.assertIsNone(values.head)

    def test_length_empty_list(self):
        values = LinkedList[int]()
        self.assertEqual(values.length(), 0)
        self.assertEqual(0, len(values))

    def test_length_one_element_in_list(self):
        values = LinkedList[int]()
        values.head = LinkedList.Node[int](9)
        self.assertEqual(values.length(), 1)
        self.assertEqual(1, len(values))

    def test_length_many_elements_in_list(self):
        values = LinkedList[int]()
        values.head = LinkedList.Node[int](9, LinkedList.Node[int](5, LinkedList.Node[int](1)) )
        self.assertEqual(values.length(), 3)
        self.assertEqual(3, len(values))

    def test_str_empty_list(self):
        values = LinkedList[int]()
        self.assertEqual(str(values), '[]')

    def test_str_one_element_in_list(self):
        values = LinkedList[int]()
        values.head = LinkedList.Node[int](9)
        self.assertEqual(str(values), '[9]')

    def test_str_many_element_in_list(self):
        values = LinkedList[int]()
        values.head = LinkedList.Node[int](9, LinkedList.Node[int](5, LinkedList.Node[int](1)) )
        self.assertEqual(str(values), '[9, 5, 1]')

    def test_append_to_empty_list(self):
        values = LinkedList[int]()
        values.append(3)
        self.assertEqual(len(values), 1)
        self.assertEqual(str(values), '[3]')

    def test_append_to_many_elements_list(self):
        values = LinkedList[int]()
        values.head = LinkedList.Node[int](9, LinkedList.Node[int](5, LinkedList.Node[int](1)) )
        values.append(0)
        self.assertEqual(len(values), 4)
        self.assertEqual(str(values), '[9, 5, 1, 0]')

    def test_append_three_element_to_init_list(self):
        values = LinkedList[int]()
        values.head = LinkedList.Node[int](1)
        values.append(3)
        self.assertEqual(len(values), 2)
        self.assertEqual(str(values), '[1, 3]')

    def test_init_with_elements(self):
        values = LinkedList[int](9, 5, 1)
        self.assertEqual("[9, 5, 1]", str(values))

    def test_get_item_first_element(self):
        values = LinkedList[int](9, 5, 1)
        self.assertEqual(values.__getitem__(0), 9)

    def test_get_item_last_element(self):
        values = LinkedList[int](9, 5, 1)
        self.assertEqual(values.__getitem__(2), 1)

    def test_get_item_out_of_range(self):
        values = LinkedList[int](9, 5, 1)
        with self.assertRaises(IndexError):
            val = values[10]

    def test_set_first_element(self):
        values = LinkedList[int](1, 2, 3, 4, 5, 6)
        values[0] = 3
        self.assertEqual(str(values), "[3, 2, 3, 4, 5, 6]" )

    def test_set_last_element(self):
        values = LinkedList[int](9, 5, 1)
        values.__setitem__(2,2)
        self.assertEqual(str(values), "[9, 5, 2]" )

    def test_set_element_out_of_range(self):
        values = LinkedList[int](9, 5, 1)
        with self.assertRaises(IndexError):
            values.__setitem__(3, 2)

    def test_generator(self):
        values = LinkedList[int](9, 5, 1)
        val_string = ""
        for val in values.__iter__():
            val_string = val_string + f"{val} "
        self.assertEqual(val_string, "9 5 1 ")

    def test_generator_of_empty_list(self):
        values = LinkedList[int]()
        self.assertEqual(list(values.__iter__()), [])

    def test_eq_with_int(self):
        values = LinkedList[int](9, 5, 1)
        self.assertFalse(values == 1)

    def test_eq_with_str(self):
        values = LinkedList[int](9, 5, 1)
        self.assertFalse(values == "aa")

    def test_eq_with_differens_lengths(self):
        values_1 = LinkedList[int](9, 5, 1, 3)
        values_2 = LinkedList[int](9, 5, 1)
        self.assertFalse(values_1 == values_2)

    def test_eq_with_same_lengths_different_values(self):
        values_1 = LinkedList[int](9, 5, 1, 3)
        values_2 = LinkedList[int](9, 5, 1, 5)
        self.assertFalse(values_1 == values_2)

    def test_eq_with_same_lengths_same_values(self):
        values_1 = LinkedList[int](9, 5, 1, 3)
        values_2 = LinkedList[int](9, 5, 1, 3)
        self.assertTrue(values_1 == values_2)

if __name__ == "__main__":
    main()