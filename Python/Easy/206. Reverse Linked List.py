# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseListIterative(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        curr = head

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev

    def reverseListRecursive(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # recursively
        if head is None or head.next is None:
            return head

        revLst = self.reverseListRecursive(head.next)
        head.next.next = head
        head.next = None
        return revLst
