#!/usr/bin/env python3

import unittest
from DoublyLinkedList import DoublyLinkedList


class TestStringMethods(unittest.TestCase):

    def test_init(self):
        list = DoublyLinkedList()
        self.assertEqual(str(list), 'list items[0]:')
        list = DoublyLinkedList([1, 2])
        self.assertEqual(str(list), 'list items[2]: 1(Head, 2) 2(1, Head)')

    def test_iter(self):
        list = DoublyLinkedList([0, 1, 2, 3, 4])
        self.assertEqual(' '.join([str(data) for data in list]), '0 1 2 3 4')
        self.assertEqual(' '.join([str(data) for data, node in list.items()]), '0 1 2 3 4')

    def test_contain(self):
        list = DoublyLinkedList([1, 2, 3, 4, 2])
        self.assertTrue(2 in list)
        self.assertTrue(1 in list)
        self.assertFalse(0 in list)

    def test_add_head(self):
        list = DoublyLinkedList()
        list.add_head(1)
        self.assertEqual(str(list), 'list items[1]: 1(Head, Head)')

    def test_add_tail(self):
        list = DoublyLinkedList([1])
        list.add_tail(2)
        self.assertEqual(str(list), 'list items[2]: 1(Head, 2) 2(1, Head)')

    def test_add_after_node(self):
        list = DoublyLinkedList([1, 2, 3])
        node = list.find(3)
        list.add_after_node(4, node)
        self.assertEqual(str(list), 'list items[4]: 1(Head, 2) 2(1, 3) 3(2, 4) 4(3, Head)')

    def test_add_before_node(self):
        list = DoublyLinkedList([1, 2, 3])
        node = list.find(1)
        list.add_before_node(0, node)
        self.assertEqual(str(list), 'list items[4]: 0(Head, 1) 1(0, 2) 2(1, 3) 3(2, Head)')

    def test_get_head(self):
        list = DoublyLinkedList([1, 2, 3])
        node = list.get_head()
        self.assertEqual(str(node), '1(Head, 2)')

    def test_get_head_empty(self):
        list = DoublyLinkedList()
        node = list.get_head()
        self.assertEqual(node, None)

    def test_get_tail(self):
        list = DoublyLinkedList([1, 2, 3])
        node = list.get_tail()
        self.assertEqual(str(node), '3(2, Head)')

    def test_get_tail_empty(self):
        list = DoublyLinkedList()
        node = list.get_tail()
        self.assertEqual(node, None)

    def test_pop_head(self):
        list = DoublyLinkedList([1, 2, 3])
        node = list.pop_head()
        self.assertEqual(str(node), '1(1, 1)')
        self.assertEqual(str(list), 'list items[2]: 2(Head, 3) 3(2, Head)')

    def test_pop_head_empty(self):
        list = DoublyLinkedList()
        node = list.pop_head()
        self.assertEqual(node, None)

    def test_pop_tail(self):
        list = DoublyLinkedList([1, 2, 3])
        node = list.pop_tail()
        self.assertEqual(str(node), '3(3, 3)')
        self.assertEqual(str(list), 'list items[2]: 1(Head, 2) 2(1, Head)')

    def test_pop_tail_empty(self):
        list = DoublyLinkedList()
        node = list.pop_tail()
        self.assertEqual(node, None)

    def test_remove_by_value(self):
        list = DoublyLinkedList([1, 3, 4])
        node = list.remove_by_value(5)
        self.assertEqual(node, None)
        node = list.remove_by_value(3)
        self.assertEqual(str(node), '3(3, 3)')
        self.assertEqual(str(list), 'list items[2]: 1(Head, 4) 4(1, Head)')

    def test_remove_all_by_value(self):
        list = DoublyLinkedList([1, 2, 2, 4])
        list.remove_all_by_value(2)
        self.assertEqual(str(list), 'list items[2]: 1(Head, 4) 4(1, Head)')
 
    def test_remove_all(self):
        list = DoublyLinkedList([1, 2, 2, 4])
        list.remove_all()
        self.assertEqual(str(list), 'list items[0]:')

    def test_find(self):
        list = DoublyLinkedList([1, 2, 3, 4, 2])
        node = list.find(4)
        self.assertEqual(str(node), '4(3, 2)')

    def test_find_all(self):
        list = DoublyLinkedList([1, 2, 3, 4, 2])
        nodes = list.find_all(2)
        self.assertEqual(str(nodes[0]), '2(1, 3)')
        self.assertEqual(str(nodes[1]), '2(4, Head)')
        self.assertEqual(' '.join([str(node.data) for node in nodes]), '2 2')


if __name__ == '__main__':
    unittest.main(verbosity = 2)
