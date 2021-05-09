import unittest

from LinkedList import LinkedList, Node


def remove_dups(ll: LinkedList):
    d = dict()
    c = ll.head
    prev = None

    while c is not None:
        if c.data in d:
            prev.next = c.next
            c = c.next
        else:
            d[c.data] = 1
            prev = c
            c = c.next


class Test(unittest.TestCase):

    def test_1(self):
        ll = LinkedList()

        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(2)

        ll.set_head(n1)
        ll.append_to_tail(n2)
        ll.append_to_tail(n3)
        remove_dups(ll)

        self.assertEqual(len(ll), 2)

    def test_2(self):
        ll = LinkedList()

        n1 = Node(1)
        n2 = Node(1)

        ll.set_head(n1)
        ll.append_to_tail(n2)
        remove_dups(ll)

        self.assertEqual(len(ll), 1)
