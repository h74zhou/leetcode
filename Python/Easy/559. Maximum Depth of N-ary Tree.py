"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        # bfs solution
        if root is None:
            return 0

        queue = [root]
        count = 0
        while queue:
            temp = []
            for node in queue:
                for child in node.children:
                    temp.append(child)
            queue = temp[:]
            count += 1

        return count
