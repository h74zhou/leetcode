# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None

        dummy = ListNode()
        dummy.next = head

        prev = dummy
        curr = head

        while curr and curr.next:
            next = curr.next
            curr.next = next.next
            next.next = curr
            prev.next = next
            prev = curr
            curr = curr.next

        return dummy.next
