"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root is None:
            return root

        q = [root]

        while q:
            nextlevel, currLevelLength = [], len(q)
            for i in range(currLevelLength):
                if i < currLevelLength - 1:
                    q[i].next = q[i + 1]
                if q[i].left:
                    nextlevel.append(q[i].left)
                if q[i].right:
                    nextlevel.append(q[i].right)
            q[-1].next = None
            q = nextlevel

        return root





