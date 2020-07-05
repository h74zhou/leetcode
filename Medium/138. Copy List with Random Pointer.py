"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None

        d = {}
        curr = head
        while curr:
            newNode = Node(curr.val)
            d[curr] = newNode
            curr = curr.next

        curr = head
        while curr:
            if curr.next is None:
                d[curr].next = None
            else:
                d[curr].next = d[curr.next]
            if curr.random is None:
                d[curr].random = None
            else:
                d[curr].random = d[curr.random]
            curr = curr.next

        return d[head]
