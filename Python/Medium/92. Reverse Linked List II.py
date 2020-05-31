# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dum = ListNode()
        dum.next = head
        pre = dum

        for i in range(m - 1):
            pre = pre.next

        cur = pre.next

        for i in range(n - m):
            next = cur.next
            cur.next = next.next
            next.next = pre.next
            pre.next = next

        return dum.next
