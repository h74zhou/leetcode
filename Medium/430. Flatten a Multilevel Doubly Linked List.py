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

        curr = head

        while curr:
            if curr.child:
                right = curr.next

                # recurse on the child node
                curr.next = self.flatten(curr.child)
                curr.next.prev = curr
                curr.child = None

                # move to the end of the child branch
                while curr.next:
                    curr = curr.next

                # if there was a right node before, connect
                if right:
                    curr.next = right
                    curr.next.prev = curr

            curr = curr.next

        return head






