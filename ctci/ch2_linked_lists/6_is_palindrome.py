import math
import unittest
from collections import deque

from LinkedList import Node, LinkedList


def is_palindrome(ll: LinkedList) -> bool:
    midpoint = math.ceil(len(ll) / 2)
    is_odd = len(ll) % 2 != 0
    stack = deque()

    c = ll.head
    i = 0

    while c is not None:
        i += 1
        if i <= midpoint:
            stack.append(c.data)
        else:
            val = stack.pop()
            if is_odd and i == midpoint + 1:
                # skip the pivot point for oddly numbered linked-lists
                continue
            elif val != c.data:
                return False
        c = c.next
    return True


class Test(unittest.TestCase):

    def test_1(self):
        ll = LinkedList()
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(2)
        n4 = Node(1)

        ll.set_head(n1)
        ll.append_to_tail(n2, n3, n4)

        self.assertTrue(is_palindrome(ll))

    def test_2(self):
        ll = LinkedList()
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        n4 = Node(2)
        n5 = Node(1)

        ll.set_head(n1)
        ll.append_to_tail(n2, n3, n4, n5)

        self.assertTrue(is_palindrome(ll))

    def test_3(self):
        ll = LinkedList()
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        n4 = Node(3)
        n5 = Node(1)

        ll.set_head(n1)
        ll.append_to_tail(n2, n3, n4, n5)

        self.assertFalse(is_palindrome(ll))

    def test_4(self):
        ll = LinkedList()
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        n4 = Node(2)
        n5 = Node(4)

        ll.set_head(n1)
        ll.append_to_tail(n2, n3, n4, n5)

        self.assertFalse(is_palindrome(ll))
