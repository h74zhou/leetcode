"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        answer, queue = [], [root]

        while queue:
            level, levelValue = [], []
            for node in queue:
                levelValue.append(node.val)
                for child in node.children:
                    if child:
                        level.append(child)
            queue = level[:]
            answer.append(levelValue[:])

        return answer
