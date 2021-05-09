import unittest
from collections import deque

from LinkedList import Node, LinkedList


def sum_list(ll_a: LinkedList, ll_b: LinkedList) -> LinkedList:
    stack_a = deque()
    stack_b = deque()

    c = ll_a.head
    while c is not None:
        stack_a.append(str(c.data))
        c = c.next

    j = ll_b.head
    while j is not None:
        stack_b.append(str(j.data))
        j = j.next

    num_a, num_b = get_int_from_stack(stack_a), get_int_from_stack(stack_b)
    total_sum = num_a + num_b
    stack_sum = get_stack_from_int(total_sum)

    return get_linked_list_from_stack(stack_sum)


def get_int_from_stack(stack):
    num = ""
    while len(stack) > 0:
        num += stack.pop()
    try:
        return int(num)
    except ValueError as e:
        print(e)


def get_stack_from_int(i: int) -> deque:
    stack = deque()
    for digit in str(i):
        stack.append(digit)
    return stack


def get_linked_list_from_stack(stack) -> LinkedList:
    ll = LinkedList()
    ll.set_head(Node(stack.pop()))

    while len(stack) > 0:
        ll.append_to_tail(Node(stack.pop()))
    return ll


class Test(unittest.TestCase):

    def test_1(self):
        ll_a = LinkedList()
        ll_a.set_head(Node(7))
        ll_a.append_to_tail(Node(1), Node(6))

        ll_b = LinkedList()
        ll_b.set_head(Node(5))
        ll_b.append_to_tail(Node(9), Node(2))

        ll_sum = sum_list(ll_a, ll_b)
        ll_sum.print_all_nodes()
        print("----")

    def test_2(self):
        ll_a = LinkedList()
        ll_a.set_head(Node(0))
        ll_a.append_to_tail(Node(0), Node(6))

        ll_b = LinkedList()
        ll_b.set_head(Node(1))
        ll_b.append_to_tail(Node(2), Node(3))

        ll_sum = sum_list(ll_a, ll_b)
        ll_sum.print_all_nodes()
        print("----")
