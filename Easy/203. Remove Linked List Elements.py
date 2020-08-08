# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dum = ListNode(0)
        dum.next = head
        prev = dum
        curr = head

        while curr:
            if curr.val != val:
                prev.next = curr
                prev = curr
            curr = curr.next

        if prev.next and prev.next.val == val:
            prev.next = None
        return dum.next
