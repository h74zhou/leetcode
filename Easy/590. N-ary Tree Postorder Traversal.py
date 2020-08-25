"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        answer = []

        def traverse(node):
            if not node:
                return
            for child in node.children:
                traverse(child)
            answer.append(node.val)
        traverse(root)
        return answer
