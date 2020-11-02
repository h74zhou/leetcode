"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head is None:
            return head

        # create temp for curr and the next node
        curr = head

        while curr:
            if curr.child:
                right = curr.next

                # recursively process children
                curr.next = self.flatten(curr.child)
                curr.next.prev = curr
                curr.child = None

                # loop to the end
                while curr.next:
                    curr = curr.next

                # connect the original next
                if right:
                    curr.next = right
                    curr.next.prev = curr
                    curr.child = None

            curr = curr.next

        return head


