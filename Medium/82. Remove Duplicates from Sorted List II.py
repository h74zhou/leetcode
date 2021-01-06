# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head

        dum = ListNode()
        dum.next = None
        lastNonDuplicate = dum
        curr = head

        while curr:
            if curr.next is None:
                lastNonDuplicate.next = curr
                curr = curr.next
            elif curr.val != curr.next.val:
                lastNonDuplicate.next = curr
                lastNonDuplicate = curr
                curr = curr.next
            else:
                # loop until we don't see this duplicate element anymore
                lastNonDuplicate.next = None
                temp = curr.val
                while curr and curr.val == temp:
                    curr = curr.next

        return dum.next


