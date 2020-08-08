# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        if fast:
            slow = slow.next

        prev = None
        while slow:
            next = slow.next
            slow.next = prev
            prev = slow
            slow = next

        start, end = head, prev

        while end:
            if start.val != end.val:
                return False
            start = start.next
            end = end.next

        return True
