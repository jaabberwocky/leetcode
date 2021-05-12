from LinkedList import LinkedList
from Node import Node

# Access head_node => list.get_head()
# Check if list is empty => list.is_empty()
# Delete at head => list.delete_at_head()
# Search for element => list.search()
# Node class  { int data ; Node next_element;}


def delete(lst, value):
    if lst.is_empty():
        return False
    if lst.get_head().data == value:
        lst.head_node = lst.get_head().next_element
        return True
    else:
        head = lst.get_head()
        c = head.next_element
        prev = head
        while c is not None:
            if c.data == value:
                prev.next_element = c.next_element
                return True
            else:
                c = c.next_element
        return False