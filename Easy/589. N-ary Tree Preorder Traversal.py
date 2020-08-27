"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        answer = []
        if not root:
            return answer

        def traverse(node):
            if not node:
                return
            answer.append(node.val)
            for child in node.children:
                traverse(child)
        traverse(root)
        return answer
