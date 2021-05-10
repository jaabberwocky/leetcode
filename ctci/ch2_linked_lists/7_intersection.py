from LinkedList import Node, LinkedList


def intersection(ll_a: LinkedList, ll_b: LinkedList) -> Node:
    a_nodes = set()

    a, b = ll_a.head, ll_b.head
    while a is not None:
        a_nodes.add(a)
        a = a.next

    while b is not None:
        if b in a_nodes:
            return b
        else:
            b = b.next
    return None


class Test:

    def test_1(self):
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        n4 = Node(4)
        n5 = Node(5)

        ll_a = LinkedList()
        ll_a.set_head(n1)
        ll_a.append_to_tail(n2, n3)

        ll_b = LinkedList()
        ll_b.set_head(n4)
        ll_b.append_to_tail(n2)

        intersecting_node = intersection(ll_a, ll_b)
        assert intersecting_node == n2

    def test_2(self):
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        n4 = Node(4)
        n5 = Node(5)

        n6 = Node(6)
        n7 = Node(7)

        ll_a = LinkedList()
        ll_a.set_head(n1)
        ll_a.append_to_tail(n2, n3, n4, n5)

        ll_b = LinkedList()
        ll_b.set_head(n6)
        ll_b.append_to_tail(n7)

        assert intersection(ll_a, ll_b) is None
