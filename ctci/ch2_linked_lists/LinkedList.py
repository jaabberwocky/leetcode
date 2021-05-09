class LinkedList:

    def __init__(self):
        self.head = None

    def set_head(self, node):
        self.head = node

    def append_to_tail(self, node):
        # O(n)
        n = self.head
        while n.next is not None:
            n = n.next
        n.next = node

    def prepend_to_head(self, node):
        tmp = self.head
        self.head = node
        self.head.next = tmp

    def print_all_nodes(self):
        c = self.head
        while c is not None:
            print(c)
            c = c.next

    def __len__(self):
        count = 0
        c = self.head

        while c is not None:
            count += 1
            c = c.next
        return count

    def __repr__(self):
        return f"Head-> {self.head}, Len: {len(self)}"


class Node:

    def __init__(self, data):
        self.next = None
        self.data = data

    def __repr__(self):
        return f"Node:[data = {self.data}]"


if __name__ == "__main__":
    # init LL with head
    ll = LinkedList()
    head = Node(1)
    ll.set_head(head)

    # add 2 nodes
    n1 = Node(2)
    n2 = Node(3)
    ll.append_to_tail(n1)
    ll.append_to_tail(n2)
    print(ll)

    # add 1 node to head
    n3 = Node(4)
    ll.prepend_to_head(n3)

    print(ll)
    print(ll.head.next)
