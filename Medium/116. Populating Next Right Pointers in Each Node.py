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
        if not root:
            return root

        q = [root]

        while q:
            temp = []
            for node in q:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            for i in range(len(q) - 1):
                leftNode, rightNode = q[i], q[i + 1]
                leftNode.next = rightNode
            q = temp[:]

        return root





