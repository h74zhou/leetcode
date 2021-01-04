# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dum = ListNode()
        curr = dum
        first, second = l1, l2 # pointers to l1, l2

        while curr and first and second:
            if first.val <= second.val:
                curr.next = first
                first = first.next
            else:
                curr.next = second
                second = second.next
            curr = curr.next

        if first:
            curr.next = first
        elif second:
            curr.next = second

        return dum.next
