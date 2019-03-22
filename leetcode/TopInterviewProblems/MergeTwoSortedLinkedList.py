# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1 is None and l2 is None:
            return None
        
        if l1.val <= l2.val:
            head = ListNode(l1.val)
            l1 = l1.next
        else:
            head = ListNode(l2.val)
            l2 = l2.next
        
        currentNode = head
            
        while l1 is not None or l2 is not None:
            
            # check whether either list is exhausted
            if l1 is None:
                n = ListNode(l2.val)
                l2 = l2.next
                currentNode.next = n
                currentNode = n
                continue
            
            if l2 is None:
                n = ListNode(l1.val)
                l1 = l1.next
                currentNode.next = n
                currentNode = n
                continue
            
            if l1.val <= l2.val:
                n = ListNode(l1.val)
                l1 = l1.next
                currentNode.next = n
                currentNode = n
            else:
                n = ListNode(l2.val)
                l2 = l2.next
                currentNode.next = n
                currentNode = n
                
        return head