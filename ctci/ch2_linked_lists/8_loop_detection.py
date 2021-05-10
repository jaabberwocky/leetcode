from LinkedList import Node, LinkedList


def loop_detection(ll: LinkedList) -> Node:
    nodes = set()

    c = ll.head
    while c is not None:
        if c in nodes:
            return c
        else:
            nodes.add(c)
            c = c.next
    return None  # no loop


class Test:

    def test_1(self):
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)

        ll = LinkedList()
        ll.set_head(n1)
        ll.append_to_tail(n2, n3, n2)

        assert loop_detection(ll) is n2

    def test_2(self):
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)

        ll = LinkedList()
        ll.set_head(n1)
        ll.append_to_tail(n2, n3)

        assert loop_detection(ll) is None
