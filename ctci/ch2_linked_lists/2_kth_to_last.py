import unittest

from LinkedList import Node, LinkedList


def get_kth_node(ll: LinkedList, k: int):
    if k > len(ll):
        raise ValueError(f"Not enough items to get {k}-th item.")
    elif k == len(ll) - 1:
        return ll.head.data
    else:
        c = ll.head
        for _ in range(len(ll) - k - 1):
            c = c.next
        return c.data


class Test(unittest.TestCase):

    def setUp(self):
        ll = LinkedList()
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        n4 = Node(4)
        n5 = Node(5)

        ll.set_head(n1)
        ll.append_to_tail(n2)
        ll.append_to_tail(n3)
        ll.append_to_tail(n4)
        ll.append_to_tail(n5)
        self.ll = ll

    def test_1(self):
        self.assertRaises(ValueError, get_kth_node, self.ll, 7)

    def test_2(self):
        data = get_kth_node(self.ll, 3)
        self.assertEqual(data, 2)

    def test_3(self):
        data = get_kth_node(self.ll, 5)
        self.assertEqual(self.ll.head.data, data)

    def test_4(self):
        data = get_kth_node(self.ll, 0)
        self.assertEqual(data, 5)
