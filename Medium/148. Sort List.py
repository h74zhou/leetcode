# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        arr = []
        curr = head

        while curr:
            arr.append(curr.val)
            curr = curr.next

        arr.sort()

        start = ListNode()
        dummy = start
        for i in arr:
            newNode = ListNode(i)
            start.next = newNode
            start = start.next

        return dummy.next
