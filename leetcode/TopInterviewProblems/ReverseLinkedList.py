# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        stackValues = []
        node = head
        
        while node is not None:
            stackValues.append(node.val)
            node = node.next
            
        # construct LinkedList
        try:
            newHead = ListNode(stackValues.pop())
        except IndexError:
            # this means empty linkedlist was given
            return None
        
        newNode = newHead
        while len(stackValues) > 0:
            n = ListNode(stackValues.pop())
            newNode.next = n
            newNode = n
        
        return newHead