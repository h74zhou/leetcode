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
        curr = head

        while curr:
            if curr.child:
                # save the right node
                right = curr.next

                # the front node of the i + 1 level, connect with i level
                curr.next = self.flatten(curr.child)
                curr.next.prev = curr
                curr.child = None

                # traverse the i + 1 level to the end
                while curr.next:
                    curr = curr.next

                # once you reach the end of the i + 1 level, connect it back with the original next
                if right:
                    curr.next = right
                    curr.next.prev = curr

            curr = curr.next

        return head

