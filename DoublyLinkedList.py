#!/usr/bin/env python3

__author__ = "Yates Zhou"
__copyright__ = "Copyright 2020, The Python_code Project"
__credits__ = []
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Yates Zhou"
__email__ = "zhouyates@gmail.com"
__status__ = "Production"


class DoublyLinkedList(object):
    class Node(object):
        def __init__(self, data, prev = None, next = None):
            self.data = data
            if prev and next:
                self.add(prev, next)
            else:
                self.prev, self.next = self, self

        def __str__(self):
            return '%s(%s, %s)' % (str(self.data), str(self.prev.data), str(self.next.data))

        def add(self, prev, next):
            self.prev, self.next = prev, next
            prev.next, next.prev = self, self

        def remove(self):
            self.next.prev, self.prev.next = self.prev, self.next
            self.prev, self.next = self, self

    def __init__(self, l = None):
        self.head = self.Node('Head')
        self.size = 0
        if l.__class__ == list:
            for d in l:
                self.add_tail(d)

    def __iter__(self):
        node = self.head.next
        while node != self.head:
            yield node.data
            node = node.next

    def items(self):
        node = self.head.next
        while node != self.head:
            yield node.data, node
            node = node.next

    def __len__(self):
        return self.size

    def __str__(self):
        ret = 'list items[%d]:' % len(self)
        node = self.head.next
        while node != self.head:
            ret += ' ' + str(node)
            node = node.next
        return ret

    def __contains__(self, data):
        return True if self.find(data) else False

    def add_after_node(self, data, node):
        self.Node(data, node, node.next)
        self.size += 1

    def add_before_node(self, data, node):
        self.Node(data, node.prev, node)
        self.size += 1

    def add_head(self, data):
        self.add_after_node(data, self.head)

    def add_tail(self, data):
        self.add_before_node(data, self.head)

    def get_head(self):
        return self.head.next if self.head.next != self.head else None

    def get_tail(self):
        return self.head.prev if self.head.prev != self.head else None

    def pop_head(self):
        node = self.get_head()
        if node:
            node.remove()
            self.size -= 1
        return node

    def pop_tail(self):
        node = self.get_tail()
        if node:
            node.remove()
            self.size -= 1
        return node

    def remove_by_value(self, data):
        node = self.head.next
        while node != self.head:
            if node.data == data:
                node.remove()
                self.size -= 1
                return node
            else:
                node = node.next
        return None

    def remove_all_by_value(self, data):
        ret = []
        node = self.head.next
        next = None
        while node != self.head:
            next = node.next
            if node.data == data:
                node.remove()
                self.size -= 1
                ret.append(node)
            node = next
        return ret

    def remove_all(self):
        ret = []
        node = self.head.next
        next = None
        while node != self.head:
            next = node.next
            node.remove()
            self.size -= 1
            ret.append(node)
            node = next
        return ret

    def find(self, data):
        node = self.head.next
        while node != self.head:
            if node.data == data:
                return node
            else:
                node = node.next
        return None

    def find_all(self, data):
        ret = []
        node = self.head.next
        while node != self.head:
            if node.data == data:
                ret.append(node)
            node = node.next
        return ret

