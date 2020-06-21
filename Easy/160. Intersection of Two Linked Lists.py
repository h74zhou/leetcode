# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        listALength = 0
        listBLength = 0
        a = headA
        b = headB
        while a is not None:
            listALength += 1
            a = a.next

        while b is not None:
            listBLength += 1
            b = b.next

        diff = abs(listALength - listBLength)

        if listALength > listBLength:
            while diff > 0:
                headA = headA.next
                diff -= 1
        elif listALength < listBLength:
            while diff > 0:
                headB = headB.next
                diff -= 1

        while headA is not None and headB is not None:
            if headA == headB:
                return headA
            else:
                headA = headA.next
                headB = headB.next

        return None
