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
        cur = dum
        node1 = l1
        node2 = l2

        while node1 is not None and node2 is not None:
            if node1.val < node2.val:
                cur.next = node1
                node1 = node1.next
                cur = cur.next
            elif node1.val > node2.val:
                cur.next = node2
                node2 = node2.next
                cur = cur.next
            else:
                cur.next = node1
                cur = cur.next
                node1 = node1.next
                cur.next = node2
                cur = cur.next
                node2 = node2.next

        while node1 is not None:
            cur.next = node1
            node1 = node1.next
            cur = cur.next

        while node2 is not None:
            cur.next = node2
            node2 = node2.next
            cur = cur.next

        return dum.next
