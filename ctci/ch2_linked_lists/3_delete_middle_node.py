import unittest

from LinkedList import Node, LinkedList


def delete_middle_node(ll: LinkedList, node: Node) -> None:
    c = ll.head
    prev = None

    while c.next is not None:
        if c is node:
            prev.next = c.next
            break
        else:
            prev = c
            c = c.next


class Test(unittest.TestCase):

    def test_1(self):
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

        delete_middle_node(ll, n3)
        ll.print_all_nodes()
        self.assertEqual(len(ll), 4)
