# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        node = head
        num = ''
        while node is not None:
            num += str(node.val)
            node = node.next
        return int(num, 2)