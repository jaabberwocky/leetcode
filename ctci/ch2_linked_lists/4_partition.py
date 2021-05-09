import unittest

from LinkedList import Node, LinkedList


def test_decorator(test_fn, *args, **kwargs):
    print("------")
    test_fn(*args, **kwargs)
    print("------")


def partition(ll: LinkedList, x: Node) -> LinkedList:
    c = ll.head
    partition_value = x.data
    lt_list = []
    gte_list = []

    while c is not None:
        if c.data < partition_value:
            lt_list.append(c)
        else:
            gte_list.append(c)
        c = c.next

    sorted_ll = LinkedList()

    for ind, el in enumerate(lt_list + gte_list):
        el.next = None
        if ind == 0:
            sorted_ll.set_head(el)
        else:
            sorted_ll.append_to_tail(el)
    return sorted_ll


class Test(unittest.TestCase):

    def test_1(self):
        ll = LinkedList()
        n1 = Node(3)
        n2 = Node(5)
        n3 = Node(8)
        n4 = Node(5)
        n5 = Node(10)
        n6 = Node(2)
        n7 = Node(1)

        ll.set_head(n1)
        ll.append_to_tail(n2, n3, n4, n5, n6, n7)

        sorted_ll = partition(ll, Node(5))
        sorted_ll.print_all_nodes()  # visual test
        print("-----")

    def test_2(self):
        ll = LinkedList()
        n1 = Node(1)
        n2 = Node(4)
        n3 = Node(5)
        n4 = Node(5)
        n5 = Node(10)
        n6 = Node(6)
        n7 = Node(1)

        ll.set_head(n1)
        ll.append_to_tail(n2, n3, n4, n5, n6, n7)

        sorted_ll = partition(ll, Node(6))
        sorted_ll.print_all_nodes()  # visual test
